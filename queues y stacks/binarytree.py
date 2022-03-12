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
            
            
    def find( self, valor ):
        def recorrer( valor, nodo):
            if valor == nodo.valor:
                return nodo.valor
            elif valor < nodo.valor:
                if nodo.rama_izquierda == None:
                    return 'No existe el elemnto buscado'
                else:
                    return recorrer( valor, nodo.rama_izquierda )
            else:
                if nodo.rama_derecha == None:
                    return 'No existe el elemento buscado'
                else:
                    return recorrer( valor, nodo.rama_derecha)
        nodo_encontrado = recorrer( valor, self.raiz )
        return print( nodo_encontrado )
    
    
    def delete( self, valor ):
            def recorrer( valor, nodo, nodo_anterior ):
                
                if valor == nodo_anterior:
                    
                    if nodo.rama_izquierda == None and nodo.rama_derecha == None:
                        if nodo_anterior.rama_izquierda != None:
                            if nodo_anterior.rama_izquierda.valor ==  nodo.valor:
                                nodo.anterio.rama_izquierda = None
                                
                        if nodo_anterior.rama_derecha != None:
                            if nodo_anterior.rama_derecha.valor ==  nodo.valor:
                                nodo.anterio.rama_derecha = None
                        nodo = None
                        
                    elif nodo.rama_izquierda == None and nodo.rama_derecha != None:
                        
                        if nodo.anterior.rama_izquierda != None:
                            if nodo_anterior.rama_izquierda.valor ==  nodo.valor:
                                nodo_anterior.rama_izquierda = nodo.rama_derecha
                                
                        if nodo_anterior.rama_derecha != None:
                            if nodo_anterior.rama_derecha.valor ==  nodo.valor:
                                nodo_anterior.rama_derecha = nodo.rama_derecha
                                
                    elif nodo.rama_derecha == None and nodo.rama_izquierda != None:
                        
                        if nodo.anterior.rama_izquierda != None:
                            if nodo_anterior.rama_izquierda.valor ==  nodo.valor:
                                nodo_anterior.rama_izquierda = nodo.rama_izquierda
                                
                        if nodo_anterior.rama_derecha != None:
                            if nodo_anterior.rama_derecha.valor ==  nodo.valor:
                                nodo_anterior.rama_derecha = nodo.rama_izquierda
                    else:
                        nodo_comodin = None
                        nodo_anterior = nodo
                        nodo = nodo.rama_derecha
                        
                        while nodo.rama_izquierda != None:
                            nodo_comodin = nodo
                            nodo = nodo.rama_izquierda
                        nodo_anterior.valor = nodo.valor
                        if nodo.rama_derecha != None:
                            nodo_comodin.rama_izquierda = nodo.rama_derecha
                        else:
                            nodo_comodin.rama_izquierda = None
                        nodo = None
                elif valor < nodo.valor:
                    if nodo.rama_izquierda == None:
                        return 'No existe el elemento buscado'
                    else:
                        return recorrer( valor, nodo.rama_izquierda, nodo)
                else:
                    if nodo.rama_derecha == None:
                        return 'No existe el elemento buscado'
                    else:
                        return recorrer( valor, nodo.rama_derecha, nodo)
            recorrer( valor, self.raiz, self.raiz )
            
    def preoder(self):
        contenedor = []
        def recorrer(nodo):
            contenedor.append(nodo.valor)
            if nodo.rama_izquierda != None:
                recorrer( nodo.rama_izquierda )
            if nodo.rama_derecha != None:
                recorrer( nodo.rama_derecha )
        recorrer( self.raiz )
        return print( contenedor )
                        
    def inorder( self ):
        contenedor = []
        def recorrer(nodo):
            if nodo.rama_izquierda != None:
                recorrer( nodo.rama_izquierda )
            contenedor.append( nodo.valor )
            if nodo.rama_derecha != None:
                recorrer( nodo.rama_derecha )
        recorrer( self.raiz )
        return print( contenedor )
                            
                            
bst = binarytree()

bst.insert(45)
bst.insert(55)
bst.insert(65)
bst.insert(85)


bst.find(75)

bst.delete(45)