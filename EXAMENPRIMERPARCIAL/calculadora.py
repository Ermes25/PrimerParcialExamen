import os
os.system("cls")
os.system("color 09")

def calculadora ():
    num1 = int(input("Digite su numero"))
    num2 = int(input("Digite otro numero"))
    try:
        opcion = int(input("Elige el operador que usaras 1.suma 2.resta 3.multiplicar 4.dividir"))
        if opcion == 1:
            resultado = num1 +  num2
            print(f"el resultado de {num1} + {num2} = {resultado}")
        if opcion == 2:
            resultado = num1 - num2
            print(f"el resultado de {num1} - {num2} = {resultado}")
        if opcion == 3:
            resultado = num1 * num2
            print(f"el resultado de {num1} * {num2} = {resultado}")
        if opcion == 4:
            resultado = num2 / num2
            print(f"el resultado de {num2} + {num1} = {resultado}")

        else:
            print("No conocemos esa opcion intentelo de nuevo")
    except:
        print("Hubo un gran Error Lo sentimos")

calculadora()
    