class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, agregado): 
        self.stack.append(agregado) 
    
    def pop(self):
        if self.isEmpty():
            return print("Stack vacio, no se puede eliminar nada")
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack vacio, no se puede observar nada"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)