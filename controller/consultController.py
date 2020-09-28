# import time
from decimal import Decimal
from model.consultBulletin import consultBulletin
from model.consultForm import consultForm
from datetime import date


def consultController(driver, year, month, day):
    url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=exibeFormularioConsultaBoletim"
    driver.get(url)
    # time.sleep(20)

    date_complete = date(year, month, day)
    date_Formated = date_complete.strftime("%d%m%Y")

    if date(1993, 5, 27) <= date_complete <= date(1999, 1, 29):
        jumps = 9
    else:
        jumps = 7

    consultForm(driver, date_Formated)
    lowestQuote_buy, usd_buy, lowestQuota_symbol = consultBulletin(driver, date_Formated, jumps)
    lowestQuota_usd = Decimal(lowestQuote_buy)/Decimal(usd_buy)

    return lowestQuota_usd, lowestQuota_symbol




