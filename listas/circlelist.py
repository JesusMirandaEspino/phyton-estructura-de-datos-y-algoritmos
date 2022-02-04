class circleLinkeList:
    class _Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.nodo_siguiente = None
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = None
    # Muestra los elementos de la lista
    def __str__(self):
        array = []
        nodo_actual = self.cabeza
        pivote = True
        contador = self.tamano
        while contador != 0:
            if pivote != False or nodo_actual != self.cabeza:
                array.append(nodo_actual.valor)
                nodo_actual = nodo_actual.nodo_siguiente
                pivote = False
                contador -= 1
            else:
                break
        return str(array) + ' Tamaño: ' + str(self.tamano)

    # Agrega un elemento al inicio de la lista
    def prepend(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cola.nodo_siguiente = nuevo_nodo
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
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cola = nuevo_nodo
        self.tamano += 1

    # Elimina el primer elemento de la lista
    def shift(self):
        if self.tamano == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            self.cola.nodo_siguiente = self.cabeza
            nodo_eliminado.nodo_siguiente = None
            self.tamano -= 1
            return print(nodo_eliminado.valor)

    # Elimina el ultimo elemento de la lista
    def pop(self):
        if self.tamano == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_actual = self.cabeza
            nueva_cola = nodo_actual
            contador = self.tamano
            while contador != 0:
                if nodo_actual.nodo_siguiente != self.cabeza:
                    nueva_cola = nodo_actual
                    nodo_actual = nodo_actual.nodo_siguiente
                else:
                    break
            self.cola = nueva_cola
            self.cola.nodo_siguiente = self.cabeza
            self.tamano -= 1
            return print(nodo_actual.valor)

    # Obtiene un nodo dado un indice
    def get(self, indice):
        if indice == self.tamano - 1:
            print(self.cola.valor)
            return self.cola
        elif indice == 0:
            print(self.cabeza.valor)
            return self.cabeza
        elif not (indice >= self.tamano or indice < 0):
            nodo_actual = self.cabeza
            contador = 0
            while contador != indice:
                nodo_actual = nodo_actual.nodo_siguiente
                contador += 1
                print(nodo_actual.valor)
                return nodo_actual
        else:
            return None

    # Metodo para actualizar un valor atravez de un indice
    def update(self, indice, valor):
        nodo_objetivo = self.get(indice)
        if nodo_objetivo != None:
            nodo_objetivo.valor = valor
        else:
            return None

    # Metodo para inserta un valor dentro de un incide elegido
    def insert(self, indice, valor):
        if indice == self.tamano - 1:
            return self.append(valor)
        elif not (indice >= self.tamano or indice < 0):
            nuevo_nodo = self._Nodo(valor)
            nodos_anteriores = self.get(indice)
            nodos_siguientes = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_siguiente = nodos_siguientes
            self.tamano += 1
        else:
            return None

    # Saca un elemento de donde sea de la lista dado el indice
    def remove(self, indice):
        if indice == 0:
            return self.shift()
        elif indice == self.tamano - 1:
            return self.pop()
        elif not (indice >= self.tamano or indice < 0):
            nodos_anteriores = self.get(indice - 1)
            nodo_removido = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nodo_removido.nodo_siguiente
            nodo_removido.nodo_siguiente = None
            self.tamano -= 1
            return nodo_removido
        else:
            return None
