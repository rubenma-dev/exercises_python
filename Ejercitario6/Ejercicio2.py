#Detectar y corregir los errores del siguiente programa que aplica el iva a una factura:
base = int(input('Introduce la base imponible de la factura: '))

def aplica_iva(base, iva = 10):
 base = base * iva
 return base

print(aplica_iva(base))
