class HashMap:
    def __init__(self, size=15):
        self.size = size
        self.buckets = [[] for _ in range(size)] 

    def funcion_hash(self, key):
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10 

    def agregar(self, key, value):
        index = self.funcion_hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  
                return
        bucket.append((key, value))  

    def buscar(self, key):
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
                del bucket[i] 
                return

    def print_map(self):
        print("Hash Map:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")