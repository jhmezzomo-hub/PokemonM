import os
from time import sleep
from funciones.efecto_escritura import print_animado
from clases.clase_entrenador import Entrenador
from clases.clase_pc import Pc

def main():
    entrenador = Entrenador()
    pc = Pc()
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
                os.system("cls" if os.name == "nt" else "clear")
                entrenador.ver_equipo()
            elif opcion_elegida == 3:
                os.system("cls" if os.name == "nt" else "clear")
                pc.mostrar_pc()
            elif opcion_elegida == 4:
                os.system("cls" if os.name == "nt" else "clear")
                entrenador.revisar_medallero()
            elif opcion_elegida == 5:
                os.system("cls" if os.name == "nt" else "clear")
                pass
            elif opcion_elegida == 6:
                os.system("cls" if os.name == "nt" else "clear")
                from funciones.ordenamiento import ordenamiento
                ordenamiento(pc)
            elif opcion_elegida == 7:
                os.system("cls" if os.name == "nt" else "clear")
                pass
            elif opcion_elegida == 8:
                os.system("cls" if os.name == "nt" else "clear")
                from funciones.centro_pokemon import centro_pokemon
                centro_pokemon()
            elif opcion_elegida == 9:
                os.system("cls" if os.name == "nt" else "clear")
                pc.hacer_trasnferencia()
            elif opcion_elegida == 10:
                os.system("cls" if os.name == "nt" else "clear")
                pc.deshacer_transferencia()
            elif opcion_elegida == 11:
                os.system("cls" if os.name == "nt" else "clear")
                from funciones.desafio import dasafiar_gimansio
                dasafiar_gimansio(entrenador)
            else:
                os.system("cls" if os.name == "nt" else "clear")
                exit()
        except Exception as e:
            os.system("cls" if os.name == "nt" else "clear")
            print(e)
            print("Inserte numeros dentro de las opciones elegidas")
            sleep(3)

main()