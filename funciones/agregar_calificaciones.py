import configuracion

# Modulo y funcion que agrega las calificaciones a un usuario ya registrado
# Requiere del id del usuario y una lista de calificaciones (datos)
def agg_calificaciones(usuario_id, lista):
    # Abrir el archivo en "a" append
    with open(f"grupos/{configuracion.grupo_predeterminado}/{usuario_id}.txt", "a") as alumno:
        formato = ""

        # For para agregar uno por uno cada calificacion separando con ";" al final de cada una, al llegar a la ultima calificacion
        # ya no se agrega ";"
        for indice, calificacion in enumerate(lista):
            if indice == len(lista) - 1:
                # En caso de que sea la ultima calificacion se agrega sin ";"
                formato += f"{calificacion}\n"
            else:
                # Primera o segunda calificacion se agregan al formato con ";" al final
                formato += f"{calificacion};"
        formato += "\n"
        
        alumno.write(formato)
