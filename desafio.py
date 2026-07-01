from medallas_set import cargar_medallas

def desafio_gimansio(gimansio):
    victoria = False
    lider, medalla = gimansio
    print(f"Has entrado al gimanasio del lider {lider} y lo has desafiado")
    #Iria la instancia de combate
    if victoria:
        print(f"Felicidades has obtenido la {medalla}")

def dasafiar_gimansio():
    i = 1
    medallas = cargar_medallas()
    for bucket in medallas.buckets:
        if bucket:
            for medalla in bucket:
                print(f"{i} - {medalla}")
                i += 1

dasafiar_gimansio()