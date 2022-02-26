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
        
        
    def insert(self, valor, padre):
        if self.raiz == None:
            self.raiz = self.Csll()
            self.raiz.append(valor, None)
        else:
            nodo_actual = self.raiz.cabeza
            def recorrer( nodo, nodo_prueba = None ):
                nodo_aux = nodo.padre
                if valor == padre:
                    return False
                elif nodo.valor == padre:
                    if nodo.hijo == None:
                        nodo.hijo = self.Csll()
                        nodo.hijo.append(valor, nodo)
                        self.tamano += 1
                        return True
                    else:
                        nodo.hijo.append(valor.nodo)
                        self.tamano += 1
                        return True
                else:
                    if nodo.hijo != None:
                        if nodo.hijo.cabeza.valor == nodo_prueba:
                            if nodo.valor == self.raiz.cabeza.valor:
                                return False
                            elif nodo.nodo_siguiente.valor != nodo_aux.hijo.cabeza.valor:
                                return recorrer( nodo.nodo_siguiente, nodo.valor )
                            else:
                                return recorrer( nodo.padre, nodo.nodo_siguiente.valor )
                        else:
                            return recorrer( nodo.hijo.cabeza, nodo.hijo.cabeza.valor )
                    elif nodo.nodo_siguiente.valor != nodo_aux.hijo.cabeza.valor:
                        return recorrer( nodo.nodo_siguiente, nodo.valor )
                    else:
                        return recorrer( nodo.padre, nodo.nodo_siguiente.valor )
            return recorrer( nodo_actual )
    
    def fin(self, valor):
        nodo_actual = self.raiz.cabeza
        def recorrer(nodo,  nodo_prueba = None ):
            nodo_aux = nodo.padre
            if nodo.valor == valor:
                return nodo.valor
            elif nodo.hijo != None:
                if nodo.hijo.cabez.valor == nodo_prueba:
                    if nodo.valor == self.raiz.cabeza.valor:
                        return 'No exite el nodo buscado'
                    elif nodo.nodo_siguiente.valor != nodo_aux.hijo.cabeza.valor:
                        return recorrer( nodo.nodo_siguiente, nodo.valor )
                    else:
                        return recorrer( nodo.padre, nodo.nodo_siguiente.valor )
                else:
                    return recorrer( nodo.hijo.cabeza, nodo.hijo.cabeza.valor  )
            elif nodo.nodo_siguiente.valor != nodo_aux.hijo.cabeza.valor:
                return recorrer( nodo.nodo_siguiente, nodo.valor )
            else:
                return recorrer( nodo.padre, nodo.nodo_siguiente.valor )
        nodo_encontrado = recorrer( nodo_actual )
        return print( nodo_encontrado )
            
        