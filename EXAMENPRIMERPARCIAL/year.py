import os
os.system("cls")
os.system("color 0a")


def persona():
    edad = int(input("ingresa tu edad"))
    try:
        if edad > 18:
            print("eres mayor de edad")
        else:
            print("no eres mayor de edad")
    except:
        print("hubo un error en el codigo")
persona()