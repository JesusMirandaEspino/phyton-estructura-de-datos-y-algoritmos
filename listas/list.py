#TODO Lista de datos

class SingleLinkedList:
    class _Nodo: # Esta es una clase Privada por el _ guin bajo
        
        def _init_(self, value): # Este es el constructor de la clase Nodo
            self.value = value
            self.nodo_nextTo = None
            
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
        
        # Metodo para insertar datos al final de la lista
        def appendNodo(self, value):
            new_nodo = self.Nodo(value)
            if self.head == None and self.lastOne == None
                self.head = new_nodo
                self.lastOne = new_nodo
            else:
                self.lastOne.nodo_nextTo = new_nodo
            self.sizeNodos += 1
            
sll = SingleLinkedList()

sll.append('A')
sll.append('B')
sll.append('C')
sll.append('D')

print(sll)