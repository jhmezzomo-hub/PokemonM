class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, elemento):
        self.queue.append(elemento)

    def dequeue(self):
        if self.isEmpty():
            return "Queue vacio"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue vacio"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)