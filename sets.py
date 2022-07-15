conjunto_vacio = set()

numeros_pares = {0,2,4,6,"tzuzul",True,True,True}

print(numeros_pares)

print(set('palabra'))

lista_colores = ["rojo","verde","azul","azul","morado","rojo"]


conjunto_colores = set(lista_colores)
print(conjunto_colores)

print(len(conjunto_colores))

conjunto_colores.add("verde")
conjunto_colores.remove("azul")
conjunto_colores.add("naranja")

print(conjunto_colores)


for color in conjunto_colores:
    print(color)

print("azul" in conjunto_colores)

ingredientes = {
    "tacos":{"carne","salsa","limon","piña"},
    "pizza":{"harina","huevo","jitomate","queso","pepperoni"},
    "pasta":{"harina","jitomate","especias"},
}

for name,ing in ingredientes.items():
    # Nombre de comidas que contienen harina y jitomate
    if 'harina' in ing and "jitomate" in ing:
        print(name)

for name,ing in ingredientes.items():
    # Nombre de comidas que son veganas (No contienen: carne, huevo, queso, pepperoni)
    # if not 'carne' in ing and not "huevo" in ing and not "queso" in ing:
    
    # Usando interseccion
    # if not ing & {'carne','huevo','queso','pepperoni'}:
    if not ing.intersection({'carne','huevo','queso','pepperoni'}):
        print(name)

all_ingredients = set()
for name,ing in ingredientes.items():
    # Union
    # all_ingredients = all_ingredients | ing
    all_ingredients |= ing

    # Diferencia: -
    # Diferencia simétrica: ^
    # Subconjunto: <
    # Superconjunto: >

print(all_ingredients)
