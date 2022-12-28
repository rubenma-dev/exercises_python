#Escribir un programa que visualice en pantalla los números pares entre 1 y 25

x = 0

while x <= 25:
    x += 1
    if x % 2 == 0:
        print(x)