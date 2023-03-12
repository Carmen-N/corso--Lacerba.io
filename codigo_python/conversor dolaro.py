menu = """


Binevenido al conversor de mondeas


1 - Pesos colombianos 
1 - Pesos argentinos 
3 - Pesos mexicanos 
Elige una opciòn: """


opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuàntos pesos argentinos  tienes? ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 46)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolores")
if opcion == 2:
    pesos = input("Cuàntos pesos mexicanos tienes? ")
    pesos = float(pesos)
    valor_dolar = 95
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolores")

if opcion == 3:
    pesos = input("Cuàntos pesos colombianos tienes? ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolores")

else:
    print('Ingresa una opciòn correcta per favor ')
