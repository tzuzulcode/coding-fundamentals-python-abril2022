# Recursividad
# Recursion: Se trata de que una funcion al momento de ejecutarse se ejecute a si misma

# def repeat():
#     return repeat()

# repeat()

number1 = 0
print(number1)
number2 = 1
print(number2)

start = 3
end = 11

while(True):
    suma = number1 + number2
    number1 = number2
    number2 = suma
    start+=1

    if(start>end):
        print(suma)
        break

# def fibonacci(n):
#     if(n<=1):
#         return n # Cuando se hace return, se termina la ejecución de las funciones
#     penultimo = fibonacci(n-1)
#     antepenultimo = fibonacci(n-2)
#     return (antepenultimo + penultimo)

def fibonacci(n):
    if(n<=1):
        return n
    return (fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(10))