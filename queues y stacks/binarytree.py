class binarytree:
    class _Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.rama_izquierda = None
            self.rama_derecha = None
    def __init__(self):
        self.raiz = None
        self.tamano = None
        
