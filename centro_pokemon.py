from Algoritmos.queue import Queue
from time import sleep

def centro_pokemon(equipo):
    for pokemon in equipo:
        Queue.enqueue(pokemon)
    sleep(1)
    while not Queue.isEmpty():
        Queue.dequeue()
        sleep(1)
    print("Tu equipo a restaurado toda su salud")