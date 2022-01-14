class DoubleLinkedList:
    class _Nodo:
        def __init__( self, valor ):
            self.valor = valor
            self.nodo_anterior = None
            self.nodo_siguiente = None
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0
        
    # Muestra los elementos de la lista
    def __str__(self):
        array = []
        nodo_actual = self.cabeza
        while nodo_actual != None:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + "Tamaño: " + str(self.tamano)
    
    # Agrega un elemento al principio de la listas
    def prepend(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cabeza.nodo_anterior = nuevo_nodo
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamano += 1
        
    # Agrega un elemento al final de la lista    
    def append(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = self.cola
            self.cola = nuevo_nodo      
        self.tamano += 1
        
    # Elimina el primer elemento de la lista
    def shift(self):
        if self.tamano == 0:
            self.cabeza = None
            self.cola = None
        elif self.cabeza != None:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
            self.tamano -= 1
            return print(nodo_eliminado.valor)
        else:
            return None
        
dll = DoubleLinkedList()

dll.prepend('A')
dll.append('B')
dll.prepend('C')
dll.append('D')

dll.shift()

print(dll)