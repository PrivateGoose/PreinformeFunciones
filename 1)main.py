def contimpares(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
n=int(input("Digite un número entero que quiera contar"))
contimpares(n)

a=input("Desea volver a intentarlo? y/n: ")
if a=="y":
    while a!="n":
        b=int(input("Digite un nuevo valor a contar: "))
        contimpares(b)
        a=input("Desea volver a intentarlo de nuevo? y/n: ")
        if a=="n":
            print("Gracias por usar el programa, su tiempo es valorado.")