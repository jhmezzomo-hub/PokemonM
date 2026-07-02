from algoritmos.listas_enlazadas import *
from algoritmos.stack import Stack
from funciones.efecto_escritura import print_animado
import os
from time import sleep

class Pc():
    def __init__(self):
        self.nodo = Node()
        self.linked_list = SingleLinkedList()
        self.stack = Stack()

    def mostrar_pc(self):
        os.system("cls" if os.name == "nt" else "clear")
        pokemones = self.linked_list.recorrer()
        for i in pokemones:
            print_animado(i)

    def agregar_pokemon_pc(self, pokemon):
        poke_node = self.nodo(pokemon)
        self.linked_list.agregar_nodo(poke_node)

    def hacer_trasnferencia(self):
        self.mostrar_pc()
        print_animado("Que pokemon desea transferir? (-1 para salir) ", salto=False)
        try: 
            pokemon = int(input())
            print_animado("Tranfiriendo Pokemon al Profesor Oak...")
            self.linked_list.eliminar_nodo(pokemon)
            if self.stack.size() < 5:
                self.stack.push(pokemon)
            else:
                self.stack.pop()
                self.stack.push(pokemon)
            print_animado("Pokemon tramferido con exito")
            sleep(5)
            return
        except Exception as e:
            os.system("cls" if os.name == "nt" else "clear")
            if e:
                print(e)
            else:
                print("Abstengase de poner el numero de alguno de los pokemons mostrado")
            sleep(5)
            self.hacer_trasnferencia()

    def deshacer_transferencia(self):
        os.system("cls" if os.name == "nt" else "clear")
        print_animado(f"Este es el ultimo pokemon transferido: {self.stack.peek()}")
        print_animado("Desea recuperarlo? S/N ", salto=False)
        try:
            decision = str(input())
            if decision.capitalize() == "N":
                return
            elif decision.capitalize() == "S":
                print_animado("Recuperando ultimo pokemon transferido...")
                pokemon = self.stack.pop()
                self.linked_list.agregar_nodo(pokemon)
            else:
                raise Exception
        except Exception as e:
            os.system("cls" if os.name == "nt" else "clear")
            if e:
                print(e)
            else:
                print("Abstengase a responder con S o N por favor")
            sleep(5)
            self.deshacer_transferencia()

    def bubble_alfabetico(self):
        pokemones = self.linked_list.recorrer()
        from sorts.bubble import uso_bubble
        uso_bubble(pokemones)

    def insertion_tipo(self):
        pass

    def quick_pc(self):
        pass

    