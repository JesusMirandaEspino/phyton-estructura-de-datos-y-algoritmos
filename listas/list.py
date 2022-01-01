#TODO Lista de datos

class SingleLinkedList:
    class _Nodo:
        
        def __init__(self, valor):
            self.valor = valor
            self.nodo_siguiente = None
            
    def __init__(self): # Constructor de la clase principal
        self.cabeza = None
        self.cola = None
        self.tamano= 0
        
    # Metodo para mostrar los datos de la lista
    def __str__(self):
        # Muestra los elementos de la SingleLinkedList
        array = []
        nodo_actual = self.cabeza
        while nodo_actual != None:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + "Tamaño: " + str(self.tamano)
    
    # Metodo para insertar datos al inicio de la lista
    def prepend(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.nodo_siguiente = self.cabeza
        self.tamano += 1 
    
    # Metodo para insertar datos al final de la lista
    def append(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1

    # Metodo para sacar el primer elemento de la lista
    def shift(self):
        if self.tamano == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
        self.tamano -= 1
        return print( nodo_eliminado.valor ) 

sll = SingleLinkedList()


sll.prepend('A')
sll.prepend('B')
sll.prepend('C')
print(sll)

sll.shift()
print(sll)