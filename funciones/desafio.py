from time import sleep
import random, os, json

def cargar_medallas():
    archivo_jason = os.path.abspath("Data\\medallas.json")

    with open(archivo_jason, "r", encoding="utf-8") as medallas:
        datos = json.load(medallas)
    return datos

def desafio_gimansio(contrincante, entrenador):
    medalla = contrincante
    print(f"Has entrado al gimanasio del lider y lo has desafiado")
    if random.choice([True, False]):
        print(f"Felicidades has obtenido la {medalla}")
        entrenador.agregar_medalla(medalla)
    else:
        print(f"Has perdido, prueba de nuevo en otro instante")

def dasafiar_gimansio(entrenador):
    las_medallas = cargar_medallas()
    gimnasios = list(las_medallas.items())
    for i, (lider, medalla) in enumerate(gimnasios, 1):
        print(f"{i} - medalla: {medalla}\nlider: {lider}")
    try:
        a_desafiar = int(input(f"Cual gimnasio deseas enfrentar?\n"))
        lider_buscado, medalla_buscada = gimnasios[a_desafiar-1]
        if not entrenador.medallero:
            desafio_gimansio([lider_buscado, medalla_buscada], entrenador)
        else:
            if medalla_buscada in entrenador.medallero:
                raise Exception
    except Exception as e:
        print("Por favor ingrese un numero dentro de los mostrados")
        sleep(5)
        dasafiar_gimansio(entrenador)

dasafiar_gimansio()