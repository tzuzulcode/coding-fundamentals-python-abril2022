personas = ("Adrian","Aracelis","Agustin","Miguel")

# persona1 = personas[0]
# persona2 = personas[1]
# persona3 = personas[2]

persona1,persona2,persona3,persona4 = personas #Unpacking

print(persona1)
print(persona2)
print(persona3)
print(persona4)


def saludar(name1,name2):
    return "Hola, persona 1: "+name1,"Hola, persona 2: "+name2 # Esto es una tupla

saludo1,saludo2 = saludar(persona1,persona2)

print(saludo1)
print(saludo2)


# highest_mean = personas[0]
# others = personas[1:]

# print(highest_mean)
# print(others)

# Otra forma de realizar lo de arriba
highest_mean,second_highest_mean,*others = personas

print(highest_mean)
print(second_highest_mean)
print(others)


grades = {
    "Adrian":10,
    "Aracelis":9.9,
    "Agustin":9.7,
    "Miguel":9.6
}

# persona1,persona2,persona3,persona4 = grades.keys()
# persona1,persona2,persona3,persona4 = grades.items()
persona1,persona2,persona3,persona4 = grades.values()

print(persona1)
print(grades.items())