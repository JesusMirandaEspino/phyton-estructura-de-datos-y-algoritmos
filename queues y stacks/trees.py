class Tree:
    class Csll:
        class Nodo:
            def __init__(self, valor, padre):
                self.valor = valor
                self.padre = padre
                self.hijo = None
                self.nodo_siguiente = None
        def __init__(self):
            self.cabeza = None
            self.cola = None
            self.tamano = 0
            
        def append(self, valor, padre):
            nuevo_nodo = self.Nodo(valor, padre)
            if self.cabeza == None and self.cola == None:
                self.cabeza = nuevo_nodo
                self.cola = nuevo_nodo
                self.cola.nodo_siguiente = self.cabeza
            else:
                self.cola.nodo_siguiente = nuevo_nodo
                nuevo_nodo.nodo_siguiente = self.cabeza
                self.cola = nuevo_nodo
            self.tamano += 1
            
    def __init__(self):
        self.raiz = None
        self.tamano = 0
        