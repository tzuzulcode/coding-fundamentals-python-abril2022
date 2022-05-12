tupla = (1,2,3,4,5)

lista = [1,2,3,4,5]


print(tupla[0])

print(lista[0])

#tupla[0] = 35 #No podemos modificar la tupla
lista[0] = 35

for element in lista:
    print(element)

for element in tupla:
    print(element)


lista.append(6) # Agrega un elemento a la lista la final
lista.pop() # Retira un elemento al final
pos_3 = lista.pop(3) # Retira un elemento en el indice 3 de la lista
print(pos_3)

#lista.sort() #Ordena la lista original
lista_ordenada = sorted(lista)
print(lista_ordenada)

tupla_ordenada = sorted(tupla)
print(tupla_ordenada)

lista_mix = ["hola",2,3,4,True]

lista_mix.sort()