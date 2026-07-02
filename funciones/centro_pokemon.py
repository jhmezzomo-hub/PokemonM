from algoritmos.queue import Queue
from time import sleep
from funciones.efecto_escritura import print_animado

def centro_pokemon(equipo):
    for pokemon in equipo:
        Queue.enqueue(pokemon)
    sleep(1)
    while True:
        print_animado("cuarando...")
        while not Queue.isEmpty():
            Queue.dequeue()
            sleep(1)
        break
    print_animado("Tu equipo a restaurado toda su salud")
    sleep(5)
    return