# ejercicio usando la tecnica *args crear una funcion que me permita identificar numeros pares de n cantidad de numeros la funcion debera retornar una lista con los numeros pares identificados
def num_pares(*args)->list[int]:
    pares: list[int] = []
    for i in args:
        if i % 2 == 0:
            pares.append(i)
    return pares    
print(num_pares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(num_pares(11, 12, 13, 14, 15, 16, 17, 18, 19, 20))