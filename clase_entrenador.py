from clase_pc import PcOak

class Entrenador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.pc = PcOak()
    
    def agregar_pokemon_equipo(self, pokemon):
        if len(self.equipo) <= 6:
            self.equipo.append(pokemon)
        else: 
            self.pc.agregar_pokemon_pc(pokemon)
            print("Pokemon enviado al PC del Profesor Oak")