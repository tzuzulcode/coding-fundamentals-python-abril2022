# First-class: Podemos asignar funciones a variables, usar funciones como argumentos, hacer return de una funcion, etc..

# 1. Definición de la función
def saludar():
    print("Hola")

def saludar_alegremente():
    print("Hola, amigo!!!")

# 2. Ejecución de la función
saludar()


def decir_nombre(nombre,funcion):
    funcion()
    print(nombre)

decir_nombre("Tzuzul",saludar)
decir_nombre("Tzuzul",saludar_alegremente)

print(type(decir_nombre))


def calculate_mean(data,*args):
    suma = 0
    for number in data:
        suma+=number

    mean = suma / len(data)

    print(args)
    results = [mean]
    for function in args:
        results.append(function(mean))

    return results
    # return format(mean)

def format_2f(number):
    return f"{number:.2f}" # f-string

def format_3f(number):
    return f"{number:.3f}" # f-string


original,original_3f,original_2f = calculate_mean([4,6,4,8,7,1],format_3f,format_2f)

print(original)
print(original_2f)
print(original_3f)


# Cree una función que acepte cualquier cantidad de números como argumentos posicionales e imprima la suma de esos números. Recuerda que podemos usar la sumfunción para sumar los valores en un iterable.
# Cree una función que acepte cualquier cantidad de argumentos posicionales y de palabras clave, y que los imprima al usuario. Su salida debe indicar qué valores se proporcionaron como argumentos posicionales y cuáles se proporcionaron como argumentos de palabras clave.
# Imprime el siguiente diccionario con los siguientes formatos:
'''
 country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
 }

- Name: "Germany"
- Population: "83 million"
- Capital: "Berlin"
- Currency: "Euro"

Name -> Germany
Population -> 83 million
Capital -> Berlin
Currency -> Euro

'''
