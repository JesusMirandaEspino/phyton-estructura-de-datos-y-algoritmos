class SingleLinkedList:
    class _Nodo: # Esta es una clase Privada por el _ guin bajo
        def _init_(self, value): # Este es el constructor de la clase Nodo
            self.value = value
            self.nodo nextTo = None
    def _init_(self): # Constructor de la clase principal
        self.head = None
        self.lastOne = None
        self.sizeNodos = 0