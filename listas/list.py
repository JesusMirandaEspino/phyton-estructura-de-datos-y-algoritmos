#TODO Lista de datos

class SingleLinkedList:
    class _Nodo: # Esta es una clase Privada por el _ guin bajo
        
        def _init_(self, value): # Este es el constructor de la clase Nodo
            self.value = value
            self.nodo nextTo = None
            
    def _init_(self): # Constructor de la clase principal
        self.head = None
        self.lastOne = None
        self.sizeNodos = 0
        
        # Metodo para mostrar los datos de la lista
        def __str__(self):
            # Muestra los elementos de la SingleLinkedList
            array = []
            actual_nodo = self.head
            while actual_nodo != None:
                array.append(actual_nodo.value)
                actual_nodo = actual_nodo.nodo_nextTo
            return str(array) + "Tamaño: " + str(self.sizeNodos)    