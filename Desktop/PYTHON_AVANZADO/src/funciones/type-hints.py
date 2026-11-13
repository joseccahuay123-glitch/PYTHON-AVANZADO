# crear una funcion que cuyos parametros seran un entero, una lista de enteros y flotantes y la funcion retornara una lista de enteros o flotantes.

def lista_de_enteros_yflotantes(n:int, l:list[int|float])->list[int|float]:
    resultado:list[int | float] = []
    for i in l:
        resultado.append(i)
    return resultado
print(lista_de_enteros_yflotantes(5, [1, 2, 3]))