#!/usr/bin/python
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
        

