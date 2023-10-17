mes = int(input("Mês: "))
dia = int(input("Dia: "))
if dia == 22 and mes == (1, 2 or 3):
    print("Verão")
else:
    if dia == 20 and mes == (4, 5 or 6):

        print("Outono")
    else:
        if dia == 21 and mes == (7, 8 or 9):
            print("Inverno")
        else:
            if dia == 23 and mes == (10, 11 or 12):

                print("Primavera")
            else:
                print("Não existe")


