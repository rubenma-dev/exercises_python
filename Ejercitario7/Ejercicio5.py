if __name__ == '__main__':
	x = int()
	numero_mayor = int()
	vector = int()
	posicion = int()
	vector = [int() for ind0 in range(5)]
	for x in range(1,6):
		print("Ingresa un numero ",x)
		vector[x] = int(input())
	for x in range(1,6):
		if x==1:
			numero_mayor = vector[x]
		else:
			if vector[x]>numero_mayor:
				numero_mayor = vector[x]
				posicion = x
	print("El numero mayor es: ",numero_mayor)
	print("Se encuentra en la posicion: ",posicion)
