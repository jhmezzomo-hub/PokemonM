from Algoritmos.listas_enlazadas import *

class Pc():
    def __init__(self):
        self.nodo = Node()
        self.linked_list = SingleLinkedList()

    def agregar_pokemon_pc(self, pokemon):
        poke_node = self.nodo(pokemon)
        self.linked_list.agregar_nodo(poke_node)