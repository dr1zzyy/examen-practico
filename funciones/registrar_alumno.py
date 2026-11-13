import configuracion

from funciones.crear_id import generar_id
from funciones.agregar_calificaciones import agg_calificaciones

grupo = configuracion.grupo_predeterminado

# Modulo encargado de registrar a un estudiante usando un nombre y una lista de calificaciones

def registrar(nombre, calificaciones):
    #Primero se genera su id
    usuario_id = generar_id()

    #Se crea su archivo
    with open(f"grupos/{configuracion.grupo_predeterminado}/{usuario_id}.txt", "w") as grupo:
        grupo.write("")
    #Se agrega a la lista_completa.txt
    with open(f"grupos/lista_completa.txt", "a") as grupo:
        grupo.write(f"{usuario_id};{nombre}" + "\n")

    #Se cargan sus calificaciones
    agg_calificaciones(usuario_id, calificaciones)
    
    return print(f"✅️ Alumno -{nombre}- registrado correctamente con el id ({usuario_id})")