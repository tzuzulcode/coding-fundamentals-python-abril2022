diccionario = {
    "key":"Valor",
    True:"Valor boolean",
    (1,2,3):"Tupla de numeros",
    "datos":{
        "name":"Tzuzul"
    }
}

print(diccionario[(1,2,3)])

dict_user = dict(name="Tzuzul",age=24,city="CDMX")
print(dict_user)

user = [['name','Tzuzul'],['age',24],['city','CDMX']]

dict_user = dict(user)
print(dict_user)

dict_user["age"] = 50
print(dict_user)

print(dict_user.get("name"))

# combined = {**diccionario,**dict_user} # Crea un diccionario nuevo con el contenido de los anteriores
diccionario.update(dict_user) # Modifica el diccionario original
del diccionario["datos"]
print(diccionario)

print('datos' in diccionario)

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,6,8,9,10]
print(lista1<=lista2)

dict_a = {"uno":1,"dos":2}
dict_b = {"dos":2,"uno":1}

print(dict_a==dict_b)

# Dictionary comprehension
numbers_list = [1,1,2,4,7,8,4,3,1,7,8,8,1,4,5,9]

# {key_expression: value_expression for expression in iterable}
conteo = {number: numbers_list.count(number) for number in numbers_list}

print(conteo)

frase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eu magna lectus. Sed eleifend purus nisi, sed facilisis mi sagittis non. Proin odio augue, malesuada ut hendrerit quis, tincidunt at orci. Donec nec diam at sapien finibus semper vel ac sapien. Etiam lobortis tellus et consequat pharetra. Phasellus consequat sapien id metus rhoncus, in iaculis ex commodo. Curabitur sapien tellus, congue quis sollicitudin efficitur, scelerisque non ipsum. Suspendisse mauris quam, faucibus id viverra non, aliquam non urna. Nam sodales convallis viverra. Morbi elit arcu, facilisis quis ultrices vel, hendrerit et mauris. Curabitur convallis sapien in ex fringilla vulputate. Morbi ipsum eros, pulvinar ac placerat et, tempor in odio. Donec vel urna quis ipsum varius interdum. Donec suscipit quam congue risus auctor viverra. Maecenas sed ex tincidunt, hendrerit nibh in, posuere leo. Donec blandit tortor vel ligula vestibulum, ut finibus mauris euismod."

frase = frase.split(" ")
print(frase)

conteo_palabras = {palabra: frase.count(palabra) for palabra in frase}

print(conteo_palabras)