def busqueda_binaria(lista_ordenada,buscado):
    encontrado = False # 1 operacion
    largo = len(lista_ordenada) # 2 operaciones
    mitad = largo // 2 # 2 operaciones
    if largo == 1: # 1 operacion
        if lista_ordenada[0] == buscado: # 1 operacion
            encontrado = True # 1 operacion
        else: 
            encontrado = False # 1 operacion
    elif buscado < lista_ordenada[mitad]: # 1 operacion
        encontrado = busqueda_binaria(lista_ordenada[0:mitad],buscado) # 1 operacion
    else:
        encontrado = busqueda_binaria(lista_ordenada[mitad:],buscado) # 1 operacion
    return encontrado # 2 operaciones