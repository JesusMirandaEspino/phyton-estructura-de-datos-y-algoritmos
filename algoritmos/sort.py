def selectionsort(lista):
    for i in range( 1, len(lista)):
        indice_mas_pequeno = i
        for j in range( i + 1, len(lista) ):
            if lista[j] < lista[indice_mas_pequeno]:
                indice_mas_pequeno = j
        if i != indice_mas_pequeno:
            elemento_temporal = lista[i]
            lista[i] = lista[ indice_mas_pequeno ]
            lista[indice_mas_pequeno] = elemento_temporal
    return print(lista)


list = [ 1,5,7,9,3,8,2,6 ]

selectionsort(list)