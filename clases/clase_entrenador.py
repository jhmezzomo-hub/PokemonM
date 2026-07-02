from clases.clase_pc import Pc
from algoritmos.hash_set import HashSet
from funciones.efecto_escritura import print_animado
from time import sleep
from algoritmos.busqeuda_lineal import busqueda_lineal

class Entrenador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.pc = Pc()
        self.medallero = HashSet()
    
    def agregar_pokemon_equipo(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
        else: 
            self.pc.agregar_pokemon_pc(pokemon)
            print("Pokemon enviado al PC del Profesor Oak")
            sleep(3)

    def revisar_medallero(self):
        if not self.medallero:
            print("No posees ninguna medalla, enfrentate a algun lider de gimansio")
            sleep(5)
            return
        else:
            print_animado(f"Posees estas medallas:")
            for bucket in self.medallero.buckets:
                for i in bucket:
                    print_animado(i)
            sleep(15)

    def agregar_medallero(self, medalla):
        self.medallero.agregar_elemento(medalla)

    def ver_equipo(self):
        if not self.equipo:
            print_animado("No posees ningun pokemon, trata de atraapar alguno")
            sleep(5)
            return
        else:
            for i in self.equipo:
                print_animado(f"{i["nombre"]} - PC: {i["pc"]}")
            sleep(5)

    def buscar_lineal(self, pokemon):
        nombres = []
        for i in self.equipo:
            nombres.append(i["nombre"])
        existencia = busqueda_lineal(nombres, pokemon)
        if existencia:
            print_animado("El pokemon esta en el equipo")
            sleep(5)
            return
        else:
            print_animado("El pokemon no esta en el equipo")
            sleep(5)
            return