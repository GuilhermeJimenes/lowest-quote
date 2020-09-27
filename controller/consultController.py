# import time
from decimal import Decimal
from model.consultBulletin import consultBulletin
from model.consultForm import consultForm


def consultController(driver, date_Formated):
    url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=exibeFormularioConsultaBoletim"
    driver.get(url)
    # time.sleep(20)

    if 1993 <= int(date_Formated[-4:]) <= 1998:
        jumps = 9
    else:
        jumps = 7

    consultForm(driver, date_Formated)
    lowestQuota_buy, usd_buy, lowestQuota_symbol = consultBulletin(driver, date_Formated, jumps)
    lowestQuota_usd = Decimal(lowestQuota_buy)/Decimal(usd_buy)

    return lowestQuota_usd, lowestQuota_symbol




