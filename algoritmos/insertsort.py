def insertionsort(lista):
    for i in range( 1, len(lista)):
        while lista[ i - 1 ] > lista[i] and 1 > 0:
            elemento_temporal = lista[i]
            lista[i] = lista[ i - 1 ]
            lista[ i - 1 ] = elemento_temporal
            i = i - 1
    return print(lista)


list = [ 1,5,7,9,3,8,2,6 ]

insertionsort(list)


