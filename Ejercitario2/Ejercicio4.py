"""Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quiere calcular de forma automática el precio que debe cobrar a sus
clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar
gratis, si tiene entre 4 y 18 años debe pagar 10.000 Gs. y si es mayor de 18 años,
15.000 Gs."""""


edad = int(input("Introduce tu edad: "))
if edad < 4:
    print("Entra gratis")
elif edad <= 18:
    print("El precio de la entrada es 10.000 Gs")
else:
    print("El precio de la entrada es 15.000 Gs")
