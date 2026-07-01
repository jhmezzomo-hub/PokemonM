import os, json
from Algoritmos.hash_map import HashMap

def cargar_pokedex():
    archivo_jason = os.path.abspath("Data\\pokedex.json")
    pokemon_map = HashMap()

    with open(archivo_jason, "r", encoding="utf-8") as pokedex:
        datos = json.load(pokedex)
        for id in datos.keys():
            pokemon_map.agregar(id, datos[id])
    
    return pokemon_map