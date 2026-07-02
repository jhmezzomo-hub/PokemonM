from funciones.efecto_escritura import print_animado
import os
from time import sleep

def ordenamiento(pc):
    os.system("cls" if os.name == "nt" else "clear")
    opciones = ["Alfabetico", "Por Tipo", "Por PC"]
    for i, opcion in enumerate(opciones, 1):
        print_animado(f"{i} - {opcion}")
    print_animado("Como desea organizar la PC? (-1 para salir) ", salto=False)
    try:
        ordenar_como = int(input())
        if pc.linked_list.isEmpty():
            os.system("cls" if os.name == "nt" else "clear")
            print_animado("No hay elementos en el pc para ordenar")
            sleep(5)
            return
        elif ordenar_como == -1:
            return
        elif ordenar_como == 1:
            os.system("cls" if os.name == "nt" else "clear")
            pc.bubble_alfabetico()
            print_animado("Ya esta ordenado alfabeticamente")
            sleep(5)
            return
        elif ordenar_como == 2:
            os.system("cls" if os.name == "nt" else "clear")
            pc.insertion_tipo()
            print_animado("Ya esta ordenado por tipo")
            sleep(5)
            return
        elif ordenar_como == 3:
            os.system("cls" if os.name == "nt" else "clear")
            pc.quick_pc()
            print_animado("Ya esta ordenado por PC")
            sleep(5)
            return
        else:
            raise Exception
    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        print(e)
        print("Abstengase a contestar con alguna de las opciones mostradas")
        sleep(2)
        ordenamiento()