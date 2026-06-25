import os, json

class PokemonHashMap:
    def __init__(self, size=15):
        self.size = size
        self.buckets = [[] for _ in range(size)] 

    def funcion_hash(self, key):
        numeric_sum = sum(int(char) for char in key if char.isdigit()) #Suma todos los numeros de la llave siempre y cuando sean numeros
        return numeric_sum % 10 

    def agregar(self, key, value):
        index = self.funcion_hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  #Actualiza la llave
                return
        bucket.append((key, value))  #Lo agrega en caso de no existir

    def buscar(self, key):
        #Busca el valor segun la key
        index = self.funcion_hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None 

    def eliminar(self, key):
        index = self.funcion_hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  #Con del eliimina el conjunto llave/valor
                return

    def print_map(self):
        print("Hash Map:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

archivo_jason = os.path.abspath("pokedex.json")
pokemon_map = PokemonHashMap()

with open(archivo_jason, "r", encoding="utf-8") as pokedex:
    datos = json.load(pokedex)
    for id in datos.keys():
        pokemon_map.agregar(id, datos[id])