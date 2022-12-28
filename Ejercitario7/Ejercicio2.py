#02) Escriba un programa que pida un número entero mayor que cero y que
#muestre en pantalla sus divisores(agregar los divisores en una lista para luego
#imprimir en pantalla

def main():
    print("DIVISORES")
    numero = int(input("Escriba un número entero mayor que cero: "))

    if numero <= 0:
        print("El numero no es mayor que cero")
    else:
        print(f"Los divisores de {numero} son ", end="")
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end=" ")


if __name__ == "__main__":
    main()