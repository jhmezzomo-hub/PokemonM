from medallas_set import cargar_medallas
from time import sleep

def desafio_gimansio(contrincante):
    victoria = False
    medalla = contrincante
    print(f"Has entrado al gimanasio del lider y lo has desafiado")
    #Iria la instancia de combate
    if victoria:
        print(f"Felicidades has obtenido la {medalla}")

def dasafiar_gimansio():
    medallas = []
    las_medallas = cargar_medallas()
    for bucket in las_medallas.buckets:
        if bucket:
            for medalla in bucket:
                medallas.append(medalla)

    try:
        for i, e in enumerate(medallas, 1):
            print(f"{i} - {e}")
        a_desafiar = int(input(f"Cual gimansio deseas enfrentar?\n"))
        contrincante = las_medallas.buscar_elemento(medallas[a_desafiar-1])
        desafio_gimansio(contrincante)
    except Exception as e:
        print("Por favor ingrese un numero dentro de los mostrados")
        print(e)
        dasafiar_gimansio()

dasafiar_gimansio()