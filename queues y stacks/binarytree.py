class binarytree:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.rama_izquierda = None
            self.rama_derecha = None
    def __init__(self):
        self.raiz = None
        self.tamano = None

    def insert(self,valor):
        nuevo_nodo = self.Nodo(valor)
        if self.raiz == None:
            self.raiz = nuevo_nodo
        else:
            def recorrer( valor, nodo ):
                if valor == nodo.valor:
                    return 'El nodo ya existe'
                elif valor < nodo.valor:
                    if nodo.rama_izquierda == None:
                        nodo.rama_izquierda = nuevo_nodo
                        return True
                    else:
                        return recorrer( valor, nodo.rama_izquierda )
                elif valor > nodo.valor:
                    if nodo.rama_derecha == None:
                        nodo.rama_derecha = nuevo_nodo
                        return True
                    else: 
                        return recorrer( valor, nodo.rama_derecha )
            recorrer( valor, self.raiz)
                
bst = binarytree()

bst.insert(45)
bst.insert(55)
bst.insert(65)
bst.insert(85)


bst.insert(45)
