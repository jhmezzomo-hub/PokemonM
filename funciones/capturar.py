import os
from funciones.efecto_escritura import print_animado
from time import sleep
from pokedex_map import cargar_pokedex
from random import randint

def capturar_pokemon():
        os.system("cls" if os.name == "nt" else "clear")
        print_animado("Bienvenido al metodo de captura")
        sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        print_animado("Capturando Pokemon...")
        sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        pokemones = cargar_pokedex()
        capturado = randint(1,15)
        os.system("cls" if os.name == "nt" else "clear")
        poke_capturado = pokemones.buscar(str(capturado))
        print_animado(f"Has capturado un {poke_capturado["nombre"]}")
        sleep(5)
        return poke_capturado