import requests
from decimal import Decimal


# Segunda pagina
def consultBulletin(driver, date_Formated, jumps):
    print('pegando dados de catação')
    url_table = driver.find_element_by_xpath(
        '//a').get_attribute('href')
    table = requests.get(url_table)
    table = table.text.replace(date_Formated, '').replace(',', '.').split(';')

    lowestQuota_symbol = 'x'
    lowestQuote_buy = Decimal('inf')
    usd_buy = '1'

    # Tratando dados
    for item in table[3::jumps]:
        quote = Decimal(table[table.index(item) + 1])
        if lowestQuote_buy > quote:  # pega a moeda com menor cotação e seu simbolo
            lowestQuote_buy = quote
            lowestQuota_symbol = item
        if item == 'USD':  # pega o valor do Dolar
            usd_buy = quote

    print("valor final: ", lowestQuote_buy)
    return lowestQuote_buy, usd_buy, lowestQuota_symbol
