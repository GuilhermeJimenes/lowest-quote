from controller.consultController import consultController
from model.chrome import Chrome, finish
from model.consultCountrie import consultCountrie
from view.insertion import Insertion
from view.show import show


def webScraping():
    year, month, day = Insertion()
    driver = Chrome()
    lowestQuota_usd, lowestQuota_symbol = consultController(driver, year, month, day)
    countrie = consultCountrie(lowestQuota_symbol)
    show(lowestQuota_symbol, countrie, lowestQuota_usd)
    finish(driver)
