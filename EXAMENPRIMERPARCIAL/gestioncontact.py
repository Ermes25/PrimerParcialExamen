import os
os.system("cls")
os.system("color 0d")
class contacto:
    def __init__(self,nombre,numerodetelefono):
        self.nombre = nombre
        self.numerodetelefono = numerodetelefono

    def persona(self):
        print (f"saludos {self.nombre} tu numero de telefono es {self.numerodetelefono}")

persona1 =contacto("Ernesto Gamez","82334996")
persona1.persona()
persona2 = contacto("Isamar Mena","75592120")
persona2.persona()