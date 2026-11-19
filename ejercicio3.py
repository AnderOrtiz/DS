def maximo_recursivo(lista):
    if len(lista) == 1:
        return lista[0]
    
    cabeza = lista[0]
    max_del_resto = maximo_recursivo(lista[1:])
    
    if cabeza > max_del_resto:
        return cabeza
    else:
        return max_del_resto


print(f"El máximo de [11,24,10,28,32] es: {maximo_recursivo([11,24,10,28,32])}")