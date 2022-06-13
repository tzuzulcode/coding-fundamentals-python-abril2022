def imprimir_mensaje(mensaje):
    print(mensaje)


def funcion_con_funcion(nombre,edad,imprimir_mensaje):
    print("Bienvenido:",nombre,edad)
    imprimir_mensaje() 

    print("Terminamos")


nombre = "Tzuzul"
edad = 24
funcion_con_funcion("Tzuzul",24,lambda:imprimir_mensaje(f"Hola{nombre}! Edad: {edad}"))


