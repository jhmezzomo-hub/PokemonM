def busqueda_lineal(lista,buscado):
    encontrado = False # 1 operacion
    for i in lista: # n operaciones
        if i == buscado: # n operaciones
            encontrado = True # 1 operacion
            break # 1 operacion
    return encontrado # 1 operaciones