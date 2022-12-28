#03) Escribir una función que calcule el factorial de un número. Por ejemplo, 5! =
#5*4*3*2*1 = 120.

def factorial(x,n):

	if(n>0):
		x=factorial(x,n-1)
		x=x*n
	else:
		x=1
	return x
 
try:
	numero = int(input("inserta un numero "))
 
	calculo=factorial(1,numero)
	print ("El factorial de %s es %s" % (numero,calculo))
except:
	print("Tiene que ser un valor numerico")