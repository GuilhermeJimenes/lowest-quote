from datetime import datetime
from decimal import Decimal

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Automation:
    def __init__(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        if browser == "Firefox":
            self.driver = webdriver.Firefox()
        if browser == "Edge":
            self.driver = webdriver.Edge()
        if browser == "Safari":
            self.driver = webdriver.Safari()

    def parsing_strdate(self, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%d%m%Y")

    def parsing_date(self, date):
        return datetime.strptime(date, "%d%m%Y")

    def access_quota_table(self, date):
        print("Preenchendo formulário")

        url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=exibeFormularioConsultaBoletim"
        self.driver.get(url)

        self.driver.find_element(By.XPATH, "//input[@name='RadOpcao'][@value='2']").click()
        text_field = self.driver.find_element(By.XPATH, "//input[@id='DATAINI']")
        text_field.clear()
        text_field.send_keys(date)
        self.driver.find_element(By.XPATH, "//input[@class='botao']").click()

        try:
            self.driver.find_element(By.XPATH, "//div[@class='msgErro']")
            self.driver.quit()
            print("Erro ao preencher formulário")
            exit()
        except NoSuchElementException:
            print("formulário preenchido")

        return

    def get_table_quota(self, str_date):
        if datetime(1993, 5, 27) <= self.parsing_date(str_date) <= datetime(1999, 1, 29):
            quantity_columns = 9
        else:
            quantity_columns = 7

        table = requests.get(self.driver.find_element(By.XPATH, "//a").get_attribute("href"))
        table = table.text.replace(str_date, "").replace(",", ".").split(";")
        if table[0] == "": table.pop(0)

        lowest_quote_buy = Decimal("inf")
        return table, quantity_columns, lowest_quote_buy

    def get_quota(self, str_date):
        print("pegando dados de catação")

        table, quantity_columns, lowest_quote_buy = self.get_table_quota(str_date)

        for index, symbol in enumerate(table[2::quantity_columns]):
            quote_found = Decimal(table[index * quantity_columns + 3])

            if lowest_quote_buy > quote_found:
                lowest_quote_buy = quote_found
                lowest_quota_symbol = symbol

            if symbol == "USD":
                usd_buy = quote_found

        lowest_quota_usd = Decimal(lowest_quote_buy) / Decimal(usd_buy)
        return lowest_quota_usd, lowest_quota_symbol

    def get_countrie(self, lowest_symbol):
        print("Buscando por País")

        url = "https://ptax.bcb.gov.br/ptax_internet/consultarTabelaMoedas.do?method=consultaTabelaMoedas"
        self.driver.get(url)
        table = requests.get(self.driver.find_element(By.XPATH, "//a").get_attribute("href"))
        table = table.text.split(";")
        for index, symbol in enumerate(table[8::6]):
            if symbol.strip() == lowest_symbol.strip():
                return table[index * 6 + 10].strip()

    def start(self, date):
        date = self.parsing_strdate(date)
        self.access_quota_table(date)
        lowest_quota_usd, lowest_quota_symbol = self.get_quota(date)
        countrie = self.get_countrie(lowest_quota_symbol)

        return {
            "countrie": countrie,
            "lowest_quota_symbol": lowest_quota_symbol,
            "lowest_quota_usd": float("%.9f" % lowest_quota_usd)
        }
