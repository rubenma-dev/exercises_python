#01) Escriba un programa que pida un año y que muestre en pantalla si es
#bisiesto o no.

año = int(input("Ingrese un año: "))

if (año%4 ==0 and año%100!=0):
    print("Es biciesto")
else:
    print("No es biciesto")
