## crear una funcion que resiva 5 numeros enteros y que retorne solo una lista de numeros pares, tener en cuenta las anotaciones
def numeros_pares(n1: int, n2: int, n3: int, n4: int, n5: int) -> list[int]:
    numeros: list[int] = [n1, n2, n3, n4, n5]
    pares: list[int] = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares


# Ejemplo de uso
resultado = numeros_pares(2, 5, 8, 11, 14)
print(resultado)

def suma (a:int,b:int)->  int:
    return a + b
print(suma(34, 67))

def login(user="",passw=""):
    return "bienvenido al sistema"
print(login(passw="11111",user="admin"))