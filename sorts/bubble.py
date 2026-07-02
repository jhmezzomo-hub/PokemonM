def uso_bubble(lista):
    n = len(lista)
    for i in range(0, n):
        for e in range(0, n - i - 1):
            if e > i:
                lista[i], lista[e] = lista[e], lista[i]
    return lista