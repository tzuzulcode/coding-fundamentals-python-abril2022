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

class Felino(Animal):
    def __init__(self, color, size, has_eyes, paws, texture, whiskers):
        super().__init__(color, size, has_eyes, paws, texture)
        self.whiskers = whiskers

class Robot:
    pass

class Zombi:
    pass

class Cat(Felino,Robot,Zombi): # Sub clase

    lifes = 7
    has_tough_tongue = True

    def __init__(self, color, size, has_eyes, paws, texture,whiskers, has_hair):
        Felino.__init__(self,color, size, has_eyes, paws, texture, whiskers)
        Zombi.__init__(self)
        Robot.__init__(self)
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


michi = Cat("White","30cm",True,4,"Soft",True, True)

michi.jump()

print(michi.color)
print(michi.whiskers)
print(michi.has_hair)

