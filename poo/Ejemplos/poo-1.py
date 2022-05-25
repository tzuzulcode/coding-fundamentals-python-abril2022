class Person:
    def __init__(self, name, edad, ciudad, auto):
        self.name = name
        self.edad = edad
        self.ciudad = ciudad
        self.auto = auto

    def saludar(self):
        print("Hola, mi nombre es "+self.name)

class School:
    alumnos = []

    def inscribir_alumno(self, alumno):
        if(isinstance(alumno,Person)):
            self.alumnos.append(alumno)
        else:
            print("Eso no es un alumno")

    def pasar_lista(self):
        print("Pasando lista:")
        for alumno in self.alumnos:
            print(alumno.name)



tzuzul = Person("Tzuzul",24,"Ciudad de México",True)
cristian = Person("Cristian",22,"Bogotá",True)
emilia = Person("Emilia",23,"Buenos Aires",True)

list_of_people = [tzuzul,cristian,emilia]

print(tzuzul)
print(cristian)
print(emilia)


suma = 0
auto = 0
for person in list_of_people:
    # print(person.name)
    person.saludar()
    suma += person.edad
    if(person.auto):
        auto+=1

promedio = suma/len(list_of_people)

print("Promedio de edad: ", promedio)
print("Personas con auto: ", auto)

school = School()

school.inscribir_alumno(tzuzul)
school.inscribir_alumno(cristian)
school.inscribir_alumno(emilia)
school.inscribir_alumno(5)

school.pasar_lista()