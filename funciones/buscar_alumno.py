from funciones.lista_completa import lista_completa

# Buscar un alumno por su ID
def buscar_alumno(ID):

    # Se obtiene la lista completa de alumnos con ID y NOMBRE
    lista = lista_completa()

    # Comparar cada ID en la lista con el ID que necesitamos
    # Si no coinciden entonces no es el alumno que estamos buscando
    # Entonces se elimina de la lista
    # El for se repite hasta dejar unicamente en la lista al alumno buscado
    for alumno_id in list(lista):
        if alumno_id != str(ID):
            lista.pop(alumno_id)

    # Si la lista queda vacia entonces no se encontro al alumno
    if len(lista) == 0:
        lista = {0 : "Alumno no encontrado"}
        
    return lista