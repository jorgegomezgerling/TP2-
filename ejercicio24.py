# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone
# de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila.
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece.
# c. determinar en cuantas películas participó la Viuda Negra (Black Widow)
# d. mostrar todos los personajes cuyos nombres empiezan con C, D y G.

from stack import Stack

pila = Stack()
pila_aux = Stack()

class Personaje:
    def __init__(self, nombre, participaciones):
        self.nombre = nombre
        self.participaciones = participaciones

personaje1 = Personaje("Groot", 1)
personaje2 = Personaje("Iron Man", 10)
personaje3 = Personaje("Captain America", 9)
personaje4 = Personaje("Thor", 8)
personaje5 = Personaje("Rocket Raccoon", 6)
personaje6 = Personaje("Black Widow", 8)
personaje7 = Personaje("Hulk", 7)
personaje8 = Personaje("Spider-man", 5)

def marvel():
    pila.push(personaje1)
    pila.push(personaje2)
    pila.push(personaje3)
    pila.push(personaje4)
    pila.push(personaje5)
    pila.push(personaje6)
    pila.push(personaje7)
    pila.push(personaje8)

def reordenar():
    while pila.size() > 0:
        pila_aux.push(pila.pop())

def posicion():
    contador = 1
    while pila_aux.size() > 0:
        dato = pila_aux.pop()
        if dato.nombre == "Rocket Raccoon" or dato.nombre == "Groot":
            print(dato.nombre, " se encuentra la posicion: ", contador)
        contador = contador + 1

def cantidad():
    while pila.size() > 0:
        dato = pila.pop()
        if dato.participaciones > 5:
            print(dato.nombre, " participó en ", dato.participaciones, " peliculas.")

def cantidad_bw():
    while pila.size() > 0:
        dato = pila.pop()
        if dato.nombre == "Black Widow":
            print(dato.nombre, " participó en ", dato.participaciones, " peliculas.")

def letras():
    while pila.size() > 0:
        dato = pila.pop()
        for letra in dato.nombre:
            if letra[0] in ["C", "D", "G"]:
                print(dato.nombre)

marvel()
#letras()
#cantidad_bw()
#cantidad()
reordenar()
posicion()

