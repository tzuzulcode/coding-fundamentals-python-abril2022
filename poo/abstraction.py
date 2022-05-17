# Alumnos: alumnos, materias o calificaciones

# Calcular las calificaciones de los alumnos que toman materias
calificaciones = [1,2,3,4,5]

# Definiendo la clase
class Alumno:
    # Atributos:
    boleta_numero = 123
    nombre = "Tzuzul"
    edad = 24
    ciudad = "Ciudad de México"
    calificaciones = [10,10,10,10]

    # Métodos:
    def calcular_promedio(self):
        suma = sum(self.calificaciones)
        promedio = suma/len(self.calificaciones)
        print(promedio)


# Instanciando una clase (creando un objeto)
tzuzul = Alumno()

print(tzuzul.nombre)
print(tzuzul.ciudad)

tzuzul.calificaciones.append(5)

tzuzul.calcular_promedio()
