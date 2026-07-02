def particion(lista, low, high):
    pivot = lista[high]
    i = low-1 

    for e in range(low, high): 
        if lista[e] <= pivot: 
            i += 1 
            lista[i], lista[e] = lista[e], lista[i] 

    lista[i+1], lista[high] = lista[high], lista[i+1] 
    return i+1 

def quick_sort(lista, low=0, high=None):
    if high is None: 
        high = len(lista) - 1

    if low < high:
        indice_pivot = particion(lista, low, high) 
        quick_sort(lista, low, indice_pivot-1) 
        quick_sort(lista, indice_pivot+1, high)