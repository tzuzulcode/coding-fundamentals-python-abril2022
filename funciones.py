alumnos1 = [1,2,3,4,5,3,1,3,5,6,3,1]

alumnos2 = [8,7,8,9,7,9,8,6,9,10]

alumnos3 = [6,7,8,9,10]


suma = 0
for alumno in alumnos1:
    suma += alumno

resultado = suma/len(alumnos1)
print(resultado)

suma = 0
for alumno in alumnos2:
    suma += alumno

resultado = suma/len(alumnos1)
print(resultado)

suma = 0
for alumno in alumnos3:
    suma += alumno

resultado = suma/len(alumnos1)
print(resultado)


#camelCase
#def calcularPromedio():


#1. Definir la funcion
#snake_case
def calcular_promedio(lista):
    print(lista)
    print("Ejecución de la función")
    suma = 0
    for numero in lista:
        suma += numero

    resultado = suma/len(lista)
    print(resultado)

print("Esto no es parte de la funcion")

#2. Ejecutando la funcion
calcular_promedio(alumnos1)
calcular_promedio(alumnos2)
calcular_promedio(alumnos3)


# Utilizando return
def sumar(p1,p2):
    print(resultado)
    resultado_suma = p1 + p2
    resultado_suma2 = p1 + p2 + 5
    print(resultado_suma)

    return resultado_suma,resultado_suma2



res_sum = sumar(10,5) # Toda la expresión tiene el valor de: resultado_suma

print(res_sum)

# calculo_impuesto = res_sum * 0.16

# print(calculo_impuesto)