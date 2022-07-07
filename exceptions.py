# Exceptions: Errores de sintaxis, errores lógicos

lista = [1,2,3]

while True:
    option = input("Position [q to quit]: ")
    if option=="q":
        break
    posicion = 0
    try:
        posicion = int(option)
        print(lista[posicion])
        # raise ZeroDivisionError
    except IndexError:
        print("Posicion incorrecta de la lista. Colocaste:",posicion)
    except ValueError:
        print("Ingresa un nùmero valido. Ingresaste: ",option)
    except Exception as error: #Esto es util, si no sabemos que error podamos tener
        print("Exception: ", error.__class__.__name__)
        print("Algo salio mal: ", error)
    # except:


# Este codigo ya no se ejecuta:
print("Mensaje oculto")