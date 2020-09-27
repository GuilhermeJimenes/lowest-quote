from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def Chrome():
    option = Options()
    option.headless = True
    # remova o conteúdo dos parênteses para rodar o chrome em primeiro plano
    driver = webdriver.Chrome(options=option)
    return driver


def finish(driver):
    driver.quit()
    exit()
