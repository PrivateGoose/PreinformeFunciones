def definirprimo(a):
    cont=0
    contp=0
    while cont <= a :
        cont += 1
        if a % cont == 0:
            contp += 1

    if  contp>2:
            print("El número no es primo")
    else:
            print("El número es primo")

a=int(input("Numero a evaluar: "))
definirprimo(a)