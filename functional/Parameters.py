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