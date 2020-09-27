import pandas as pd


def consultCountrie(symbol):
    print('Buscando por País')
    url_table = 'https://ptax.bcb.gov.br/ptax_internet/consultarTabelaMoedas.do?method=consultaTabelaMoedas'
    df_full = pd.read_html(url_table)[0]
    df_full = df_full.set_index('Símbolo')
    return df_full.loc[symbol].País
