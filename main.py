import os
from time import sleep
from funciones.efecto_escritura import print_animado

def main():
    opciones = ["Ver Pokédex", "Ver Equipo Principal", "Ver PC", "Ver Medallas", 
                "Capturar nuevo Pokémon", "Ordenar PC", "Buscar Pokémon en Equipo",
                "Enviar Pokémon al Centro Pokémon", "Transferir Pokémon al Profesor Oak",
                "Deshacer última transferencia", "Desafiar Líder de Gimnasio",
                "Salir del sistema"]
    os.system("cls" if os.name == "nt" else "clear")
    print_animado("Bienvenido a Pokemon M!")
    sleep(2)
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        for i, opcion in enumerate(opciones, 1):
            print_animado(f"{i} - {opcion}")

        try:
            print_animado("Opcion: ", salto=False)
            opcion_elegida = int(input())
            if opcion_elegida == 1:
                from pokedex_map import mostrar_pokedex
                mostrar_pokedex()
            elif opcion_elegida == 2:
                pass
            elif opcion_elegida == 3:
                pass
            elif opcion_elegida == 4:
                pass
            elif opcion_elegida == 5:
                pass
            elif opcion_elegida == 6:
                pass
            elif opcion_elegida == 7:
                pass
            elif opcion_elegida == 8:
                pass
            elif opcion_elegida == 9:
                pass
            elif opcion_elegida == 10:
                pass
            elif opcion_elegida == 11:
                pass
            else:
                exit()
        except Exception as e:
            os.system("cls" if os.name == "nt" else "clear")
            print(e)
            print("Inserte numeros dentro de las opciones elegidas")
            sleep(3)

main()