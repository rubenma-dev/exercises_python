
class Calculadora:
	def __init__(self):
		self.calculadora=[]

	# menu del programa
	def menu(self):
		print()
		menu=[
			['Calculadora'],
			['1. Suma dos numeros'],
			['2. Resta dos numero'],
			['3. Multiplicar dos numeros'],
			['4. Dividir dos numeros'],
			['5. Salir del sistema']
		]

		for x in range(6):
			print(menu[x][0])

		opcion=int(input("Introduzca la opción deseada: "))
		if opcion==1:
			self.suma()
		elif opcion==2:
			self.resta()
		elif opcion==3:
			self.multiplicar()
		elif opcion==4:
			self.dividir()
		elif opcion==5:
			print("Saliendo del sistema ...")
			exit()

		# volvemos a llamar al menú
		self.menu()


	def suma(self):
		print("Suma de numeros")
		num1=int(input("Introduzca un numero: "))
		num2=int(input("Introduzca otro numero: "))
		print("La suma es: ", + int(num1+num2))


	def resta(self):
		print("Resta de numeros")
		num1=int(input("Introduzca un numero: "))
		num2=int(input("Introduzca otro numero: "))
		print("La resta es: ", + int(num1-num2))
		

	def multiplicar(self):
		print("Multiplicacion de numeros")
		num1=int(input("Introduzca un numero: "))
		num2=int(input("Introduzca otro numero: "))
		print("La Multiplicacion es: ", + int(num1*num2))
		


	def dividir(self):
		print("Division de Numeros")
		num1=int(input("Introduzca un numero: "))
		num2=int(input("Introduzca otro numero: "))
		print("La Division es: ", + int(num1/num2))	



# bloque principal
agenda=Calculadora()
agenda.menu()