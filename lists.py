# Lists: 

lista_vacia = []

lista_compras = ['Pan','Verduras','Café','Chocolate','Galletas']

lista_animales = ['Tigre','Tortuga','Gato']

lista_años = [2005,2010,2015,2020]

datos = ['Tzuzul',1231231,564.456,True]


print(lista_compras[1])
print(lista_animales[1])
print(lista_años[3])
print(datos[2])

print(datos[-1]) #Ultimo elemento
print(datos[-2]) #Penultimo elemento

lista_años.sort(reverse=True)
print(lista_años)


for i in range(5):
    print(lista_compras[i])

# For dinámico
for i in range(len(lista_compras)):
    print(lista_compras[i])

for producto in lista_compras:
    print(producto)

i = 0
while(i<len(lista_compras)):
    print(lista_compras[i])
    i+=1