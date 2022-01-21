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
    
    # Agrega un elemento al principio de la listas
    def prepend(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cabeza.nodo_anterior = nuevo_nodo
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamano += 1
        
    # Agrega un elemento al final de la lista    
    def append(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = self.cola
            self.cola = nuevo_nodo      
        self.tamano += 1
        
    # Elimina el primer elemento de la lista
    def shift(self):
        if self.tamano == 0:
            self.cabeza = None
            self.cola = None
        elif self.cabeza != None:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
            self.tamano -= 1
            return print(nodo_eliminado.valor)
        else:
            return None
        
    # Elimina el ultimo elemento de la lista
    def pop(self):
        if self.tamano == 0:
            self.cabeza = None
            self.cola = None
        else: 
            nodo_eliminado = self.cola
            self.cola = nodo_eliminado.nodo_anterior
            self.cola.nodo_siguiente = None
            self.cola.nodo_anterior = None
            self.tamano -= 1
            return print(nodo_eliminado.valor)
    # Obtiene un nodo dado un indice
    def get(self, indice):
        if indice == self.tamano - 1:
            print(self.cola.valor)
            return self.cola
        elif indice == 0:
            print( self.cabeza.valor)
            return self.cabeza
        elif not ( indice >= self.tamano or indice < 0):
            indice_balanceado = int(self.tamano / 2)
            if indice <= indice_balanceado:
                nodo_actual = self.cabeza
                contador = 0
                while contador != indice:
                    nodo_actual = nodo_actual.nodo_siguiente
                    contador += 1
                print(nodo_actual.valor)
                return nodo_actual    
            else:
                nodo_actual = self.cola
                contador = self.tamano -1
                while contador != indice:
                    nodo_actual = nodo_actual.nodo_anterior
                    contador -= 1
                print(nodo_actual.valor)
                return nodo_actual 
        else:
            return None
        
    # Metodo para actualizar un valor atravez de un indice
    def update( self, indice, valor ):
        nodo_objetivo = self.get(indice)
        if nodo_objetivo != None:
            nodo_objetivo.valor = valor
        else:
            return None
    
    # Metodo para insertar elementos
    def insert(self, indice, valor):
        if indice == self.tamano - 1:
            return self.append(valor)
        elif not( indice >= self.tamano or indice < 0):
            nuevo_nodo = self._Nodo(valor)
            nodos_anteriores = self.get(indice)
            nodos_siguientes = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = nodos_anteriores
            nuevo_nodo.nodo_siguiente = nodos_siguientes
            nodos_siguientes.nodo_anterior = nuevo_nodo
            self.tamano += 1
        else:
            return None
        
    # Saca un elemento de donde sea de la lista dado el indice
    def remove(self, indice):
        # Saca un elemento de donde sea de la linkedlist dado un indice
        if indice == 0:
            return self.shift()
        elif indice == self.tamaño - 1:
            return self.pop()
        elif not (indice >= self.tamaño or indice < 0):
            nodo_removido = self.get(indice)
            nodos_anteriores = nodo_removido.nodo_anterior
            nodos_siguientes = nodo_removido.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nodos_siguientes
            nodos_siguientes.nodo_anterior  = nodos_anteriores
            nodo_removido.nodo_anterior = None
            nodo_removido.nodo_siguiente = None
            self.tamaño -= 1
            return nodo_removido
        else:
            return None

        
        
dll = DoubleLinkedList()

dll.prepend('A')
dll.append('B')
dll.prepend('C')
dll.append('D')

print(dll)

dll.shift()

print(dll)

dll.pop()

print(dll)


dll.get(1)

print(dll)


dll.insert(1, 'M')

print(dll)

dll.remove(1)

print(dll)