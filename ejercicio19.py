# Dada una pila de películas de las que se conocen su titulo, estudio cinematográfico y 
# anio de estreno, desarrollar las funciones necesarias para resolver las siguientes
# actividades: 
# a. mostrar los nombres de peliculas estrenadas en el anio 2014. 
# b. indicar cuantas peliculas se estrenaron en el anio 2018. 
# c. mostras las peliculas de marvel estudios estrenadas en el anio 2016.

from stack import Stack
pila = Stack()
contador = 0

class Pelicula:
    def __init__(self, nombre, anio, estudio):
        self.nombre = nombre
        self.anio = anio
        self.estudio = estudio
    
pelicula1 = Pelicula("Captain America: Civil War", 2016, "Marvel Studios")
pelicula2 = Pelicula("Maléfica", 2014, "Disney")
pelicula3 = Pelicula("At Eternity's Gate", 2018, "Riverstone Pictures")
pelicula4 = Pelicula("Doctor Strange", 2016, "Marvel Studios")
pelicula5 = Pelicula("Interestellar", 2014, "Paramount Pictures")
pelicula6 = Pelicula("Captain America: The Winter Soldier", 2014, "Marvel Studios")
pelicula7 = Pelicula("Black Panther", 2018, "Marvel Studios")

pila.push(pelicula1)
pila.push(pelicula2)
pila.push(pelicula3)
pila.push(pelicula4)
pila.push(pelicula5)
pila.push(pelicula6)
pila.push(pelicula7)

def estreno2014():
   while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula.anio == 2014:
            print(pelicula.nombre)

def cantidad2018(contador):
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula.anio == 2018:
            contador += 1
    return contador

def marvel2016():
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula.anio == 2016 and pelicula.estudio == "Marvel Studios":
            print(pelicula.nombre)

print("Presione: ")
print("1: para ver estrenos de 2014")
print("2: para ver cantidad de pelicular estrenadas en 2018")
print("3: Pelicular de Marvel Studios de 2016:")

numero = int(input())

if numero == 1: 
    print("En 2014 se estrenó la siguiente cartelera: ")
    estreno2014()
elif numero == 2:
    print("En 2018 se estrenaron la siguiente cantidad de películas: ")
    print(cantidad2018(contador))
elif numero == 3:
    print("Las siguientes peliculas de Marvel se estrenaron en 2016: ")
    marvel2016()

        





