from datetime import date


def Insertion():
    while True:
        try:
            data_s = input("Digite uma data, obedecendo o seguinte formato YYYYMMDD: ").strip()
            year = int(data_s[0:4])
            month = int(data_s[4:6])
            day = int(data_s[6:8])
            if year < 1984:
                raise ValueError('O ano deve ser acima de 1983')
            if len(data_s) != 8:
                raise ValueError('quantidade de caracteres errada')
            date_complete = date(year, month, day)
            date_Formated = date_complete.strftime("%d%m%Y")
        except ValueError as e:
            print("Valor inválido: ", e)
        else:
            break
    # data_s = input("Digite uma data, obedecendo o seguinte formato YYYYMMDD: ").strip()
    # year = int(data_s[0:4])
    # month = int(data_s[4:6])
    # day = int(data_s[6:8])
    # date_complete = date(year, month, day)
    # date_Formated = date_complete.strftime("%d%m%Y")
    return date_Formated
