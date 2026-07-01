import os, json
from Algoritmos.hash_set import HashSet

archivo_jason = os.path.abspath("medallas.json")
pokemon_map = HashSet()

with open(archivo_jason, "r", encoding="utf-8") as medallas:
    datos = json.load(medallas)
    for medalla in datos.values():
        pokemon_map.agregar_elemento(medalla)