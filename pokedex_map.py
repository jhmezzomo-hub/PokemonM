import os, json
from algoritmos.hash_map import HashMap
from funciones.efecto_escritura import print_animado
from time import sleep

def cargar_pokedex():
    archivo_jason = os.path.abspath("Data\\pokedex.json")
    pokemon_map = HashMap()

    with open(archivo_jason, "r", encoding="utf-8") as pokedex:
        datos = json.load(pokedex)
        for id in datos.keys():
            pokemon_map.agregar(id, datos[id])
    
    return pokemon_map

def mostrar_pokedex():
    os.system("cls" if os.name == "nt" else "clear")
    pokedex = cargar_pokedex()
    for bucket in pokedex.buckets:
        for pokemon in bucket:
            id, datos = pokemon
            print_animado(f"{id} - {datos["nombre"]}")
    
    try:
        print_animado("Seleccione el ID(numero) del pokemon cuya informacion desea saber(-1 para salir): ", salto=False)
        mas_info = int(input())
        if mas_info == -1:
            return
        informacion = pokedex.buscar(str(mas_info))
        if informacion:
            print_animado(f"Nombre: {informacion["nombre"]}\nTipo: {informacion["tipo"]}\nPC: {informacion["pc"]}")
            print_animado("Desea ver otro pokemon? S/N", salto=False)
            continuar = input()
            if continuar == "S":
                mostrar_pokedex()
            elif continuar == "N":
                return
            else: raise Exception
        sleep(5)
    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        print(e)
        print_animado("Por favor solo ingrese alguno de las opciones mostradas")
        sleep(2)
        mostrar_pokedex()

    return