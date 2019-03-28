def potbase(a,b):
    Resultado=a**b
    print("El reslutado es ",Resultado )
a=float(input("Digite el valor a ingresar como base: "))
b=float(input("Digite el valor a ingresar como potencia: "))
c=float(input("Digite la siguiente base: "))
d=float(input("Digite la siguiente potencia: "))
x1=a**b
x2=c**d
potbase(a,b)

potbase(c,d)
if x1>x2:
     print("La primera potencia es mayor: ")
else:
     print("La segunda potencia es menor: ")