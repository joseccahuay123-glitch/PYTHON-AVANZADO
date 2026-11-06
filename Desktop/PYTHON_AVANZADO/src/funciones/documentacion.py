#en la siguiente funcion deveran escribir la documentacion segun la convencion para el docdtring de funcione.
def area_rectangulo(b, a):
    """calcula el area del rectangulo
    args:
        b(int|float):este argumento sera la base del rectangulo
        a(int|float):este argumento sera la altura del rectangulo
    raises::
        los argumentos deben ser igual o menores a 0

    return:
        (int|float):el resultado de la operaciion b*h (base por altura)
   
    """
    return b * a

# funcion para hallar la potencia de un numero
def potencian (n:int,p:int)->int:
    """calcula la potencia de un numero
    args:
        n(int):este argumento sera el numero de la  base
        p(int):este argumento sera el exponente
    raises::
        los argumentos deben ser igual o menores a 0
    return:
        (int):el resultado de la operaciion n**p (base por exponente)
    """
    resultado:int=1
    for _ in range(p):
        resultado *= n
    return resultado
