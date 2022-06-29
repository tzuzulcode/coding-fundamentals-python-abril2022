# Docstring pequeño
# def sumar(a,b):
#     'Suma dos numeros: a y b'

#     return a+b

# Docstring grande
def sumar(a,b):
    '''
    Suma dos numeros: a y b

    Params:
    - a: Number (Integer o Float)
    - b: Number (Integer o Float)
    '''

    return a+b

sumar(5,2)

print(sumar.__doc__)