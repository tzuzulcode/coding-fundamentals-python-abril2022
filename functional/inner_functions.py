def realizar_operacion(a,b,operacion="multiplicar"):
    def multiplicar(a,b):
        return a*b
    def sumar(a,b):
        return a+b
    if operacion=="multiplicar":
        return multiplicar(a,b)
    elif operacion=="sumar":
        return sumar(a,b)


print(realizar_operacion(5,4))
print(realizar_operacion(5,4,"sumar"))