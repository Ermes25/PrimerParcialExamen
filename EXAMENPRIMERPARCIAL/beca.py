import os
os.system("cls")
os.system("color 04")

def beca(nota):
    if nota >= 95:
        return True
    else:
        return False

nombre= input("Ingrese su nombre")
nota_estudiante = float(input("ingrese tu nota"))

if beca(nota_estudiante):
    print(f"felicidades {nombre} tienes una beca")
else:
    print(f"lo sentimos {nombre} no tienes una beca")