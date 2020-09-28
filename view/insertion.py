def Insertion():
    while True:
        try:
            data_s = input("Digite uma data, obedecendo o seguinte formato YYYYMMDD: ").strip()
            year = int(data_s[0:4])
            month = int(data_s[4:6])
            day = int(data_s[6:8])
            if len(data_s) != 8:
                raise ValueError('quantidade de caracteres incorreta')
            if year < 1984:
                raise ValueError('O ano deve ser acima de 1983')
        except ValueError as e:
            print("Valor inválido: ", e)
        else:
            break
    return year, month, day
