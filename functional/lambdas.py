# Lambda o Anonymous function: Función que se expresa como una sentencia
# Las funciones tienen nombre, mientras que los lambda no

# Statement

# variable1 = 10

# for number in [1,2,3,4,5]:

def str_to_int(str):
    return int(str)

# lambda str: int(str)

def calcular_promedio(data,func):
    suma = 0

    for number in data:
        suma += func(number)

    return suma/len(data)


numbers = ['1','2','3','4']
print(calcular_promedio(numbers,str_to_int))
print(calcular_promedio(numbers,lambda str: int(str)))
print(calcular_promedio(numbers,lambda str: float(str)))

lambda1 = lambda a,b:a+b
lambda2 = lambda a,b,c:a+b+c

print(lambda1(5,6))
print(lambda2(5,6,7))