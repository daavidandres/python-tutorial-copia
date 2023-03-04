import tabulate
# Crear un programa que lea una tabla con los nombres, edad,
# sexo y notas de algoritmia de un curso de alumnos de un
# colegio. El programa debe calcular e imprimir con base en
# estos datos estadísticas fundamentales (promedio, moda,
# porcentajes, etc).
# Desafío secreto:
# Descubre como mejorar el programa considerando más cosas que
# tus compañeros.
# Puedes añadir sistemas que, con base en lo calculado,
# impriman una conclusión lógica al
# usuario

# Creamos una clase para modelar un "Alumno":
class Alumno:
    def __init__(self, nombre, edad, sexo, notas_algoritmica):
        self.Nombre = nombre
        self.Edad = edad
        self.Sexo = sexo
        self.notas_algoritmica = notas_algoritmica
        self.aplazado = True

    def ___str___(self):
        return self.Nombre, self.Edad, self.Sexo, self.notas_algoritmica


# Definición de funciones
def tipoint(inputprompt):
    while 1:
        try:
            outputvar = int(input(inputprompt))
            return outputvar
        except ValueError:
            continue


# Declaración de variables y lista
promptEdad = "Ingrese la edad: "
promptNota = "Ingrese la nota de algorítmica: "
promptN = "Ingrese el número de alumnos del curso: "
Alumnos = []
auxNombre = ""
auxEdad = 0
auxSexo = ""
auxNota = 0

# Input del usuario
N = tipoint(promptN)
X = Alumno
for i in range(N):
    auxNombre = input("Ingrese el nombre del alumno: ")
    auxEdad = tipoint(promptEdad)
    auxSexo = input("Ingrese el sexo (sólo M o F)")
    while auxSexo != "M" and auxSexo != "F":
        print("Error.")
        auxSexo = input("Ingrese el sexo (sólo M o F)")
    auxNota = tipoint(promptNota)
    Alumnos.append(Alumno(auxNombre, auxEdad, auxSexo, auxNota))
print(tabulate(Alumnos, headers=[]))