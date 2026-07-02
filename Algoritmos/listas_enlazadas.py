class Node:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def tamaño(self):
        contador = 0
        actual = self.head
        while actual:
            contador += 1
            actual = actual.next
        return contador

    def recorrer(self):
        if self.isEmpty():
            return
        actual = self.head
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.next
        return elementos

    def agregar_nodo(self, dato):
        nuevo_nodo = Node(dato)
        if self.isEmpty():
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def eliminar_nodo(self, dato_a_eliminar):
        if self.isEmpty():
            return
        
        if self.head.dato == dato_a_eliminar:
            self.head = self.head.next
        
        actual = self.head
        anterior = None
        while actual and actual.dato != dato_a_eliminar:
            anterior = actual
            actual = actual.next
        
        if actual:
            anterior.next = actual.next
        else:
            print("Este dato no existe")

    def insertar_nodo(self, dato, dato_anterior):
        if self.isEmpty():
            return
        
        actual = self.head
        while actual and actual.dato != dato_anterior:
            actual = actual.next

        if not actual:
            print("No existe el nodo anterior al dato que quiere insertar")

        nuevo_nodo = Node(dato)
        nuevo_nodo.next = actual.next
        actual.next = nuevo_nodo

    def busar_nodo(self, dato_busacado):
        if self.isEmpty():
            return
        actual = self.head
        while actual: 
            if actual.dato == dato_busacado:
                print("Dato encontrado")
                return True
            actual = actual.next
        print("Dato no encontrado")
        return False
    
    def ordenar(self):
        if self.isEmpty():
            return
        
        intercambio = True
        while intercambio:
            intercambio = False
            actual = self.head
            while actual.next:
                if actual.dato > actual.next.dato:
                    actual.dato, actual.next.dato = actual.next.dato, actual.dato
                    intercambio = True
                actual = actual.next