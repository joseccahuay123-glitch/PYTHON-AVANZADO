# crear un programa asigne un puntaje a cada letra del abecedario y que una funcion me permita saber la letra que tenga menor puntaje y mayor puntaje y la media
def asignar_puntaje():
    # Asignar puntaje a cada letra del abecedario
    puntajes = {}
    for i in range(26):
        letra = chr(97 + i)  # Letras minúsculas de 'a' a 'z'
        puntajes[letra] = i + 1  # Puntaje de 1 a 26
    return puntajes