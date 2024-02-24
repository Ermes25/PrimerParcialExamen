import os
os.system("cls")
os.system("color 04")

def producto():
    nombre = str(input("Ingrese el nombre del producto"))
    precio = float(input("ingrese el precio del producto"))

    try:
        if precio > 500:
            descuento = precio * 0.10
            print(f"el producto{nombre} tiene un valor de{precio}con un descuento de{descuento}")
        else :
            descuento = precio
            print(f"el producto{nombre} tiene un valor de{precio}con un descuento de{descuento}")
    except:
        print("El programa dio error")
producto()