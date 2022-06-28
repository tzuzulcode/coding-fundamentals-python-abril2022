thing = True

if thing:
    print("Esto es verdadero")
else:
    print("Esto no es verdadero")

if thing is None:
    print("No tiene valor")
else:
    print("Si tiene valor")

if thing is not None:
    print("Si tiene valor")
else:
    print("No tiene valor")


# Positional arguments: Se basan en la posicion. Forzosamente deben pasarse
# Default values
def saludar(nombre=None,edad=None,ciudad=None):
    if nombre is not None and edad is not None and ciudad is not None:
        print("Hola,",nombre,edad,ciudad)
    else:
        print("Hola, anonimo")

# saludar("Tzuzul",24,"CDMX")
# saludar(None,None,None)

#Usando keyword args
# saludar(edad=24,nombre="Tzuzul",ciudad="CDMX")

# Combinacion de positional args y keyword args. Primero se colocan los positional args
# saludar("Tzuzul",ciudad="CDMX",edad=24)

# Ejecutando funcion sin parametros:
saludar()

# *args
# **kwargs
# unpack

# El parametro por defecto se calcula cuando la funcion se define
# def save(data,result=[]):
#     result.append(data)
#     print(result)

# def save(data):
#     result = []
#     result.append(data)
#     print(result)

def save(data, result=None):
    if result is None:
        result = []
    result.append(data)
    print(result)

save("Tzuzul",["Willy"]) # ['Tzuzul']
save("Juanito") # ['Juanito']

# Explode/Gather
# *args -> agrupa un determinado numero de argumentos posicionales
def print_things(*args):
    print("Positional tuple",args)
    for person in args:
        print("Hola",person)

print_things("Tzuzul","Willy","Cristian","Juanito",3,2,1,True,False,15.4)


def registrar_usuario(*args,**kwargs):
    print("Nombre requerido: ",kwargs["name"])
    print("Edad requerida: ",kwargs["edad"])
    print("Demás datos", args)


# registrar_usuario("Tzuzul",24,"CDMX",["Musica","Programación","Videojuegos"])
registrar_usuario("CDMX",["Musica","Programación","Videojuegos"],edad=24,name="Tzuzul")


# kwargs -> keyword arguments
def print_kwargs(**kwargs):
    print("Keyword arguments",kwargs)
    print("Name: ",kwargs["name"])

print_kwargs(name="Tzuzul",edad=24,ciudad="CDMX",gustos=["Musica","Programación","Videojuegos"])

# mi_diccionario = {"key":"value","key2":"value2"}
mi_diccionario = {
    'key':"value",
    "key2":"value2",
    "key3":"value3"
}

mi_lista = [1,5,6,2,7]

print(mi_lista[4])

print(mi_diccionario.get("key3")) # imprime -> value2
print(mi_diccionario["key3"]) # imprime -> value2

mi_diccionario["key4"] = "value4"
print(mi_diccionario)

