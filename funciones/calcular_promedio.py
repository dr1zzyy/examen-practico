import configuracion

from funciones.buscar_alumno import buscar_alumno

def promedio_individual(usuario_id):

    with open(f"grupos/{configuracion.grupo_predeterminado}/{usuario_id}.txt", "r") as alumno:
        contenido = alumno.read().strip()

        if not contenido:
            print(f"Alumno ({usuario_id}) no cuenta con calificaciones en el sistema")
            return 1


        sumatoria_total = 0
        ciclos = 0
        for linea in contenido.splitlines():
            calif = linea.strip().split(";")
            sumatoria = 0
            for calificacion in calif:
                sumatoria += int(calificacion)
            promedio = sumatoria/len(calif)

            ciclos += 1
            sumatoria_total += promedio

        promedio_total_individual = round(sumatoria_total/ciclos)

        return promedio_total_individual

def promedio_grupal():
    
    repetir = True
    id_counter = 1

    promedios = {}

    while repetir == True:

        try:
            promedio = promedio_individual(id_counter)
            promedios.update({id_counter : promedio})
            id_counter += 1
        except FileNotFoundError:
            repetir = False
            break

    promedio_grupal = sum(promedios.values())/len(promedios)

    alumno_id, prom_max = max(promedios.items(),key=lambda x: x[1])

    alumno = buscar_alumno(alumno_id)

    ID, nombre = alumno.popitem()

    print(f"⭐️ -> Promedio mas alto de ({ID}){nombre} -- {round(prom_max)}")

    return round(promedio_grupal)
