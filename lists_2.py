tupla = (1,2,3,4,5,6,7,8,9,10)
numbers = list(tupla)
print(numbers)

lista = [1,2,3,4,5]

# Slice
#lista[inicio,condicion final,pasos]
print(numbers[0:5:2]) # Primeras cinco posiciones de dos en dos
print(numbers[:5:2]) # Primeras cinco posiciones de dos en dos
print(numbers[::2]) # Saltos de dos en dos
print(numbers[::3]) # Saltos de tres en tres
print(numbers[::4]) # Saltos de cuatro en cuatro


print(numbers[::-2]) # Saltos de dos en dos, en reversa
print(numbers[7:0:-2]) # Desde la pos. 7 hasta la 1 con saltos de dos en dos, en reversa


# DUplicar items
print(['Tzuzul']*10)
print(['Tzuzul','Juanito']*2)
print('abc'*10)

del numbers[6]
print(numbers)

# Comprehension
# Generar una lista de numeros del 1 al 100
numbers_list = []
# numbers_list.append(1)
# numbers_list.append(2)
# numbers_list.append(3)
# numbers_list.append(4)
# Posible solución 1:
# for i in range(1,101):
#     numbers_list.append(i)

# Posible solución 2:
# numbers_list = list(range(1,101))

# Posible solución 3:
# List comprehension
# [expresion for item in iterable]
# numbers_list = [number for number in range(1,101)]
# numbers_list = [number+1 for number in range(100)]

# print(numbers_list)

# Lista de 10 de zeros:
lista_zeros = [0 for _ in range(10)]
print(lista_zeros)

# Lista de pares
# lista_pares = [number for number in range(100) if number % 2 == 0]
# lista_pares = list(range(100))[::2]
lista_pares = [number for number in range(0,100,2)]
print(lista_pares)

# Generando matriz
# matriz = [[row,col] for row in range(1,10,3) for col in range(row,row+3)]
size = 3
matriz = [[col for col in range(row,row+size)] for row in range(1,(size**2)+1,size)]
print(matriz)