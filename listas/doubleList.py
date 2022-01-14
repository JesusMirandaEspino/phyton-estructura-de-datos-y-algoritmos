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