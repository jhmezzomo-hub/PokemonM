import os
from funciones.efecto_escritura import print_animado
from time import sleep
from random import choice


class Pokemon():
    def __init__(self, id, nombre, tipo, pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc