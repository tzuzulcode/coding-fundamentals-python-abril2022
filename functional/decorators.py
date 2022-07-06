# Decorator: Es una función que toma como entrada una función y devuelve otra función


def function_details(func):
    def get_details(*args,**kwargs):
        print("Function name:",func.__name__)
        print("Positional args: ",args)
        print("Keyword args: ", kwargs)
        result = func(*args,**kwargs)
        print("Result:", result)
        return result

    return get_details

def format_2f(func):
    def format_number(*args,**kwargs):
        result = func(*args,**kwargs)

        return f"{result:.2f}"

    return format_number

# def decirHola(name):
#     print("Hola,",name)

# details = function_details(decirHola) #Usando decorador

# details("Tzuzul")

@function_details
def decirHola(name):
    print("Hola,",name)


# Reto: Convertir esto en la sintaxis de arriba
@format_2f
@function_details
def sumar(a,b):
    return a+b

# decirHola("Tzuzul")
print(sumar(a=5,b=10))

# Solucion del reto:
# details = function_details(sumar)

# format_number = format_2f(details)

# print(format_number(a=5,b=10))