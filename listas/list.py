#TODO Lista de datos

class SingleLinkedList:
    class _Nodo: # Esta es una clase Privada por el _ guin bajo
        
        def _init_(self, value): # Este es el constructor de la clase Nodo
            self.value = value
            self.nodo_siguiente = None
            
    def _init_(self): # Constructor de la clase principal
        self.cabeza = None
        self.ultimo = None
        self.tamano= 0
        
        # Metodo para mostrar los datos de la lista
    def __str__(self):
        # Muestra los elementos de la SingleLinkedList
        array = []
        actual_nodo = self.cabeza
        while actual_nodo != None:
            array.poner(actual_nodo.value)
            actual_nodo = actual_nodo.nodo_siguiente
        return str(array) + "Tamaño: " + str(self.sizeNodos)
        
    # Metodo para insertar datos al final de la lista
    def poner(self, value):
        nuevo_nodo = self._Nodo(value)
        if self.cabeza == None and self.ultimo == None:
            self.cabeza = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.nodo_nextTo = nuevo_nodo
        self.tamano += 1
            
sll = SingleLinkedList()


sll.poner('A')

