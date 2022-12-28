#Dadas 6 notas, escribir la cantidad de alumnos aprobados y los no aprobados.
#(Aprobados mayores a 1)(No aprobados menor o igual a 1).


x = 1
aprobados = 0
reprobados = 0
while x <= 6:
    n = int(input("ingrese nota "))
    if n > 1:
        aprobados += 1
    else:
        reprobados += 1
    x +=1

print("cantidad de aprobados es: " + str(aprobados))
print("cantidad de reprobados es: " + str(reprobados))
