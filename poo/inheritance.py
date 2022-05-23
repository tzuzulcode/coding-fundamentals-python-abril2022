# Convención: Nombrar las clases con mayúsculas
class Animal: # Super clase
    def __init__(self, color, size, has_eyes, paws, texture):
        self.color = color
        self.size = size
        self.has_eyes = has_eyes
        self.paws = paws
        self.texture = texture

    def eat(self):
        print("Comiendo...")

    def reproduce(self):
        pass

class Cat(Animal): # Sub clase

    lifes = 7
    has_tough_tongue = True

    def __init__(self, color, size, has_eyes, paws, texture, has_hair):
        super().__init__(color, size, has_eyes, paws, texture)
        # self.color = color
        # self.size = size
        self.has_hair = has_hair
        

    def jump(self):
        print("Jumping...")
    def purr(self):
        print("Purr purrr")
    def climb(self):
        print("Climbing")

# Completar esta sub-clase
class Dog(Animal):
    pass

print(issubclass(Cat, Animal))


michi = Cat("White","30cm",True,4,"Soft",True)

print(michi.color)