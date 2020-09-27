import requests


# Segunda pagina
def consultBulletin(driver, date_Formated, jumps):
    print('pegando dados de catação')
    url_table = driver.find_element_by_xpath(
        '//a').get_attribute('href')
    table = requests.get(url_table)
    table = table.text.replace(date_Formated, '').replace(',', '.').split(';')

    lowestQuota_symbol = 'x'
    lowestQuota_buy = 'inf'
    usd_buy = '1'

    # Tratando dados
    for item in table[3::jumps]:
        buy = table[table.index(item) + 1]
        if lowestQuota_buy > buy:  # pega a moeda com menor cotação e seu simbolo
            lowestQuota_buy = buy
            lowestQuota_symbol = item
        if item == 'USD':  # pega o valor do Dolar
            usd_buy = buy

    return lowestQuota_buy, usd_buy, lowestQuota_symbol
