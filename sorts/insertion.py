def insertion(lista):
    for i in range(0, len(lista)):
        for e in range(i, 0, -1):
            if lista[e] < lista[e-1]:
                lista[e], lista[e-1] = lista[e-1], lista[e]
    return lista