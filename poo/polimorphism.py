class Animal:
    def __init__(self,nombre, sonido, patas, plumas, pelaje):
        self.nombre = nombre
        self.sonido = sonido
        self.patas = patas
        self.plumas = plumas
        self.pelaje = pelaje

    def hacer_sonido(self):
        print(self.sonido,self.sonido,self.sonido)

class Gato(Animal):
    def __init__(self, nombre, patas, pelaje):
        super().__init__(nombre, "Miau", patas,False, pelaje)

class Perro(Animal):
    def __init__(self, nombre, patas, pelaje):
        super().__init__(nombre, "Guau", patas, False, pelaje)

class Pato(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre, "Cuack", patas, True, False)

    def volar(self):
        print("Volando...")

class Buho(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre, "Cuack", patas, True, False)

    def volar(self):
        print("Volando...")

class Gallina(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre, "Pio", patas, True, False)



perro = Perro("Toby",4,True)
gato = Gato("Michi",4,True)
gallina = Gallina("Turuleca",2)
pato = Pato("Donald",2)


# Polimorfismo:
animales = [perro, gato, gallina, pato]
lista = [1212,23.456,"Hola"]

perros = [perro]
gatos = [gato]

for animal in animales:
    animal.hacer_sonido()
    volar = getattr(animal,"volar",None)
    if callable(volar):
        animal.volar()