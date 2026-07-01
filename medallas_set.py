import os, json
from Algoritmos.hash_set import HashSet

archivo_jason = os.path.abspath("Data\\medallas.json")
medalla_set = HashSet()

with open(archivo_jason, "r", encoding="utf-8") as medallas:
    datos = json.load(medallas)
    for medalla in datos.values():
        medalla_set.agregar_elemento(medalla)

    medalla_set.print_hash_set()