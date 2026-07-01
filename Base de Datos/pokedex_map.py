import os, json
from Algoritmos.hash_map import HashMap

archivo_jason = os.path.abspath("pokedex.json")
pokemon_map = HashMap()

with open(archivo_jason, "r", encoding="utf-8") as pokedex:
    datos = json.load(pokedex)
    for id in datos.keys():
        pokemon_map.agregar(id, datos[id])