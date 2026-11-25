# ejercicio para map()
## recuerde map sirve para trasformar todos los elementos 
## Ejercicio 1: tienes una lista de numeros y quieres obtener una nueva lista con el (elevado a 3) de cada numero.
numeros:list[int]=[1,2,3,4]
nueva_lista=list(map(lambda e:e**3,numeros))
print (nueva_lista)

def cubo(e):
    return e**3
map(cubo,numeros)

#ejercicio para filter()
## Ejercicio 2: Tienes una lista de temparaturas (algunos bajo cero). filtrar la lista para quedarte solo con las temperaturas positivas (mayores a o)
temp:list[int|float]=[-2,10,0,-20,-1,-10,18,23.0]
nueva_temp=list(filter(lambda t:t>0,temp))
print(f"las temperaturas mayores a cero son: {nueva_temp}")

# ejercicio combinado map() y filter ()
##  Tienes una lista de numeros. Primero filtra para quedarte solo con los numeros pares. luego usa, map para multiplicarlos por 10 los numeros pares.
list_numeros:list[int]=[1,2,3,4,5,6,7]
lista_nueva=list(filter(lambda t:t %2==0,list_numeros))
print(f"los numeros pares son: [lista_nueva]")
numeros_multiplicado=list(map(lambda n:n*10,lista_nueva))
print(numeros_multiplicado)

# REFACTORIZACION: Es una tecnica para mejor o hacer mas optimo el codigo
num:list[int]=[2,3,4,5,6,7,9,12,15,17,18]
print([n*10 for n in num if n%2==0]) 