'''
closure: Es una función que se genera dinámicamente por otra funcion y ambas
puede cambiar y recordar los valores de las variables que fueron creadas
fuera de la funcion
'''

def saludar(saludo):
    # decir_frase() solo esta disponible para ejecutarse dentro de saludar()
    def decir_frase():

        def otra_funcion():
            print(saludo)

        otra_funcion()
        return "Una persona dijo: "+saludo
    
    return decir_frase


func1 = saludar("Hola")
func2 = saludar("Hola2")

print(func1())
print(func2())