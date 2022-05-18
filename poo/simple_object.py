class Animal:
    pass # Indica que queremos una clase vacia

class Gato:
    # nombre = "Michi"

    # Constructor: Función que inicializa el futuro objeto
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color

# Creando un objeto de animal: Creamos un objeto vacio

gato = Animal()
gato.nombre = "Garfield"
print(gato.nombre)

gato2 = Animal()
gato2.color = "blanco"
print(gato2.color)

gato3 = Animal()
print(gato3)

numero1 = 1
numero2 = 2

print(gato is gato2)

print(numero1 is numero2)


# Creando gatos:
gato4 = Gato("Volador","Amarillo")
print(gato4.nombre)
print(gato4.color)

gato5 = Gato("Algodon","Blanco")
print(gato5.nombre)

print(gato5.color)

# a = 1
# b=1
# print(id(a) == id(b)) #Verdadero
# a=2
# b=2
# print(a is b) # Verdadero

# print(a.__dir__)
# print(b.__dir__)