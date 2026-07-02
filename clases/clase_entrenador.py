from clases.clase_pc import Pc
from algoritmos.hash_set import HashSet

class Entrenador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.pc = Pc()
        self.medallero = HashSet()
    
    def agregar_pokemon_equipo(self, pokemon):
        if len(self.equipo) <= 6:
            self.equipo.append(pokemon)
        else: 
            self.pc.agregar_pokemon_pc(pokemon)
            print("Pokemon enviado al PC del Profesor Oak")

    def revisar_medallero(self):
        if not self.medallero:
            print("No posees ninguna medalla, enfrentate a algun lider de gimansio")
        else:
            print(f"Posees estas medallas:")
            for bucket in self.medallero.buckets:
                for i in bucket:
                    print(i)

    def agregar_medallero(self, medalla):
        self.medallero.agregar_elemento(medalla)