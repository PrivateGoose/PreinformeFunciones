def primoHermano(a):
    cont=0
    contp=0
    if a%6==0 or a==6:
        print("Su número no es válido")
    else:
        while cont<=a+1:
            cont+=1
            if (a+1)%cont==0:
                contp+=1

        if contp>2 :

            print("Su número no es primo hermano")

        else:
            print("Su número es primo hermano")



a=int(input("Digite su número deseado a evaluar: "))
primoHermano(a)