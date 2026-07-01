class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] 

    def funcion_hash(self, value):
        return sum(ord(char) for char in value) % self.size

    def agregar_elemento(self, value):
        index = self.funcion_hash(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def buscar_elemento(self, value):
        index = self.funcion_hash(value)
        bucket = self.buckets[index]
        return value in bucket

    def eliminar(self, value):
        index = self.funcion_hash(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_hash_set(self):
        print("Hash Set:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")