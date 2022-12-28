asignaturas = []
while True:
    notas = {}
    notas['asignatura'] = input("ingrese una asignatura: ")
    asignaturas.append(notas)
    respuesta = input(
        "desea ingresar otra asignatura?. Responda: (si/no) ").lower()
    if respuesta != "si":
        break
 
for asignatura in asignaturas:
    print("Asignatura", asignatura['asignatura'])
