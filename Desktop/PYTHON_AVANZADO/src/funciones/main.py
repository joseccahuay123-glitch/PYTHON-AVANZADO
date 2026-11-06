# crear un programa que me permita mostrar mensajes personalizados, crear un funcion similar a la funcion print de python
def mi_print(mensaje:str):
    texto=f"""
--------------------------------------------------
{mensaje}
--------------------------------------------------
"""
    print(texto)

print(f"este es mi mensaje personalisado")
mi_print("este es otro texto")