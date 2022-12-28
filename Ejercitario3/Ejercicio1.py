
x = 1
positivo = 0
negativo = 0
ceros = 0
while x <= 10:
    n = int(input("ingrese numero "))
    if n > 0:
        positivo += 1
    elif n < 0:
        negativo += 1
    else:
        ceros += 1
    x +=1

print("cantidad de positivos es: " + str(positivo))
print("cantidad de negativos es: " + str(negativo))
print("cantidad de ceros es: " + str(ceros))