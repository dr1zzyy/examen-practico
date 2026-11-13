import configuracion

def agg_calificaciones(usuario_id, lista):

    with open(f"grupos/{configuracion.grupo_predeterminado}/{usuario_id}.txt", "a") as alumno:
        formato = ""
        for indice, calificacion in enumerate(lista):
            if indice == len(lista) - 1:
                formato += f"{calificacion}\n"
            else:
                formato += f"{calificacion};"
        formato += "\n"
        alumno.write(formato)
