"""Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Se
desea calcular el jornal diario de acuerdo con los siguientes puntos:
1. la tarifa de las horas diurnas es de 5 euros,
2. la tarifa de las horas nocturnas es de 8 euros,
3. caso de ser domingo, la tarifa se incrementará en 2 euros el turno
diurno y 3 euros el turno nocturno.
El procedimiento a seguir es:
1. Leer nombre del turno, horas trabajadas (HT) y día de la semana.
2. Si el turno es nocturno, aplicar la fórmula JORNAL = 8*HT.
3. Si el turno es diurno, aplicar la fórmula JORNAL = 5*HT.
4. Si el día es domingo:
•turno diurno JORNAL = (5 + 2)* ht,
•turno nocturno JORNAL =(8 +3)* HT"""

nombre = input("Ingrese Nombre: ")
turno = str(input("Ingrese Turno (dia o noche): "))
HT = int(input("Ingrese horas trabajadas: "))
print("1. lunes")
print("2. Martes")
print("3. Miercoles")
print("4. Jueves")
print("5. Viernes")
print("6. Sabado")
print("7. Domingo")
dia = input("Dia de la semana trabajado: ")


if turno == "noche":
    JORNAL = (8*HT)
elif turno == "noche" and dia==7:
    JORNAL = ((8+3)*HT)
elif turno == "dia" and dia==7:
    JORNAL = ((5+2)*HT)
else:
    JORNAL = 5*HT

print("El trabajador " + str(nombre) + " trabaja en el turno de "+str(turno)+" y gana "+ str(JORNAL)+(" Euros"))