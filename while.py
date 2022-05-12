repeticion = 0 # Declarar una variable de control

while(repeticion<5): # Ponemos la condición de repetición
    #repeticion = repeticion + 1
    print(repeticion) # Realizar el codigo necesario
    repeticion += 1 # Aumentar variable de control
    
for i in range(5):
    print(i)

repeticion = 0
while(True): # Ciclo infinito
    print("Repetición")
    if(repeticion==10):
        break # Termina el ciclo
    repeticion+=1

while(True):
    print("Ingresa una opción:")
    print("01. Calcular cuadrado")
    print("02. ")
    print("03. ")
    print("q (quit). Terminar programa")
    opc = input("Digita tu opción: ")
    if(opc=="q" or opc=="quit"):
        break

    elif(opc=="1"): # %: operador
        number = int(input("Ingresa un número"))
        if(number%2==0): # Evalua si number es par
            print(number**2) # ** indica elevar a cierta potencia
            continue
    
    print("Continue no funcionó")