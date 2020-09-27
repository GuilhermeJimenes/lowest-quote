# import time
from selenium.common.exceptions import NoSuchElementException
from model.chrome import finish


# Primeira pagina
def consultForm(driver, date_Formated):
    print('Preenchendo formulário')

    driver.find_element_by_xpath(
        "//input[@name='RadOpcao'][@value='2']").click()
    textField = driver.find_element_by_xpath(
        "//input[@id='DATAINI']")
    textField.clear()
    textField.send_keys(date_Formated)
    driver.find_element_by_xpath(
        "//input[@class='botao']").click()

    # verifica se existe dados para a data buscada
    try:
        driver.find_element_by_xpath(
            "//div[@class='msgErro']")
        print("x")
        finish(driver)
    except NoSuchElementException:
        print("formulário preenchido")

    return
