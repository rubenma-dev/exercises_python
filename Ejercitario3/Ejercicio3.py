#Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un
#número negativo

numero = int(input("Ingrese un numero: "))
while numero > 0:
    print("el cuadrado de " + str(numero) + " es: " + str(numero**2))
    numero = int(input("Ingrese un numero: "))
