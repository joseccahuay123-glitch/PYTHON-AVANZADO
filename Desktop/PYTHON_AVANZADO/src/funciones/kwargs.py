# crear una funcion que me permita saber de una lista de ingredientes cual es el de mayor precio
# ejemplo:
# entrada:ajo=2 , papa=3, aceite=8, 
#salida:el ingrediente de mayor precio es aceite
def ingrediente_mayor_precio(**kwargs):
    mayor_precio = 0
    ingrediente_mayor = ""
    for ingrediente, precio in kwargs.items():
        if precio > mayor_precio:
            mayor_precio = precio
            ingrediente_mayor = ingrediente
    return f"el ingrediente de mayor precio es {ingrediente_mayor}"
ingrediente = ingrediente_mayor_precio(ajo=2, papa=3, aceite=8)
print(ingrediente)
ingrediente = ingrediente_mayor_precio(ajo=2, papa=3, aceite=8, sal=1, cebolla=15)
print(ingrediente)