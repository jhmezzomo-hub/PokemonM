from time import sleep
import random, os, json
from funciones.efecto_escritura import print_animado

def cargar_medallas():
    archivo_jason = os.path.abspath("Data\\medallas.json")

    with open(archivo_jason, "r", encoding="utf-8") as medallas:
        datos = json.load(medallas)
    return datos

def desafio_gimansio(contrincante, entrenador):
    os.system("cls" if os.name == "nt" else "clear")
    medalla = contrincante
    print(f"Has entrado al gimanasio del lider y lo has desafiado")
    if random.choice([True, False]):
        print(f"Felicidades has obtenido la {medalla}")
        entrenador.agregar_medalla(medalla)
    else:
        print(f"Has perdido, prueba de nuevo en otro instante")

def dasafiar_gimansio(entrenador):
    os.system("cls" if os.name == "nt" else "clear")
    las_medallas = cargar_medallas()
    gimnasios = list(las_medallas.items())
    for i, (lider, medalla) in enumerate(gimnasios, 1):
        print_animado(f"{i} - medalla: {medalla}\nlider: {lider}")
    print_animado("Cual gimnasio deseas enfrentar? ", salto=False)
    try:
        a_desafiar = int(input())
        lider_buscado, medalla_buscada = gimnasios[a_desafiar-1]
        if not entrenador.medallero:
            os.system("cls" if os.name == "nt" else "clear")
            desafio_gimansio([lider_buscado, medalla_buscada], entrenador)
        else:
            if medalla_buscada in entrenador.medallero:
                os.system("cls" if os.name == "nt" else "clear")
                print_animado("Ya posees esta medalla")
                sleep(5)
                return
    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        if e:
            print(e)
        else:
            print("Por favor ingrese un numero dentro de los mostrados")
        sleep(5)
        dasafiar_gimansio(entrenador)