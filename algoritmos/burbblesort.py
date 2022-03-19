def burbblesort(lista):
    for i in range( len(lista) - 1, 0, -1  ):
        cambio_terminado = True
        for j in range(i):
            if lista[j] > lista[j + 1]:
                elemento_temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = elemento_temporal
                cambio_terminado = False
        if cambio_terminado == True:
            break;
    return print(lista)


list = [ 1,5,7,9,3,8,2,6 ]
            
burbblesort(list)      
