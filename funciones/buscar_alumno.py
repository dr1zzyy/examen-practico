from funciones.lista_completa import lista_completa

def buscar_alumno(ID):
    
    lista = lista_completa()

    for alumno_id in list(lista):
        if alumno_id != str(ID):
            lista.pop(alumno_id)

    if len(lista) == 0:
        lista = {0 : "Alumno no encontrado"}
    return lista