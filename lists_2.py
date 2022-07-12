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

# Comprehension