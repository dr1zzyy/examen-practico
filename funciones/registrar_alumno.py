import configuracion

from funciones.crear_id import generar_id
from funciones.agregar_calificaciones import agg_calificaciones

grupo = configuracion.grupo_predeterminado

def registrar(nombre, calificaciones):
    usuario_id = generar_id()
    with open(f"grupos/{configuracion.grupo_predeterminado}/{usuario_id}.txt", "w") as grupo:
        grupo.write("")
    with open(f"grupos/lista_completa.txt", "a") as grupo:
        grupo.write(f"{usuario_id};{nombre}" + "\n")

    agg_calificaciones(usuario_id, calificaciones)

    return print(f"✅️ Alumno -{nombre}- registrado correctamente con el id ({usuario_id})")