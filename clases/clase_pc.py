from algoritmos.listas_enlazadas import *
from algoritmos.stack import Stack

class Pc():
    def __init__(self):
        self.nodo = Node()
        self.linked_list = SingleLinkedList()
        self.stack = Stack()

    def agregar_pokemon_pc(self, pokemon):
        poke_node = self.nodo(pokemon)
        self.linked_list.agregar_nodo(poke_node)

    def hacer_trasnferencia(self, pokemon):
        print("Tranfiriendo Pokemon al Profesor Oak...")
        self.linked_list.eliminar_nodo(pokemon)
        if self.stack.size() < 5:
            self.stack.push(pokemon)
        else:
            self.stack.pop()
            self.stack.push(pokemon)

    def deshacer_transferencia(self):
        print("Recuperando ultimo pokemon transferido...")
        pokemon = self.stack.pop()
        self.linked_list.agregar_nodo(pokemon)

    def bubble_alfabetico(self):
        pokemones = self.linked_list.recorrer()
        from sorts.bubble import uso_bubble
        uso_bubble(pokemones)

    def insertion_tipo(self):
        pass