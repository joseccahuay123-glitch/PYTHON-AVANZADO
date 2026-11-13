## crear una funcion tipo closureque me permita ingresar nombre y apellido y me retorne un mensaje con ambos datos.
def creador(nombre:str):
    def apellido(apellido:str):
        return f"tu nombre es: {nombre} y tu apellido es {apellido}"
    return apellido
alumno1 = creador("david")  # :def apellido(apellido):return
alumno2 = creador("noemi")
print(alumno1("goliat"))  
print(alumno2("maykel"))  
## usando closure crean una funcion multiplicador que reciba por parametro el factor que devuelva una funcion que permita multiplicar cualquier numero por el factor 
def multiplicador(factor:int):
    def multiplicar(numero:int):
        return numero * factor
    return multiplicar
por_dos = multiplicador(2)
por_tres = multiplicador(3) 
print(por_dos(5))  
print(por_tres(5))