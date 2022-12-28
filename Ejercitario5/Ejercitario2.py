#Escribir un programa que pregunte al usuario los números ganadores de un sorteo, los
#almacene en una lista y los muestre por pantalla ordenados de menor a
#mayor.

my_lyst = []
for i in range(6):
    my_lyst.append(int(input("Introduce un numero ganador: ")))
my_lyst.sort()
print("Los numeros ganadores son " + str(my_lyst))