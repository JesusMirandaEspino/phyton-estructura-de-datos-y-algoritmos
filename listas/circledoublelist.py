class circleDoubleLinkeList:
    class _Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.nodo_anterior = None
            self.nodo_siguiente = None
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = None
        