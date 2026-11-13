import configuracion

from funciones.buscar_alumno import buscar_alumno
from funciones.lista_completa import lista_completa

# Para obtener el promedio individual de cada alumno
def promedio_individual(usuario_id):

    # Se abre el archivo {ID} del alumno
    with open(f"grupos/{configuracion.grupo_predeterminado}/{usuario_id}.txt", "r") as alumno:
        # Se lee todo el contenido
        contenido = alumno.read().strip()

        # Si no hay ninguna linea entonces el alumno no tiene calificaciones subidas
        # Igualmente regresamos 0 para que no afecte al resto de promedios si es que 
        # se estan sacando promedios generales
        if not contenido:
            print(f"⚠️ Alumno ({usuario_id}) no cuenta con calificaciones en el sistema")
            return 0

        # sumatoria de todas las calificaciones
        sumatoria_total = 0
        # cantidad de calificaciones
        ciclos = 0
        for linea in contenido.splitlines():
            calif = linea.strip().split(";")
            sumatoria = 0
            for calificacion in calif:
                sumatoria += int(calificacion)
            promedio = sumatoria/len(calif)

            ciclos += 1
            sumatoria_total += promedio

        # Sacar promedio y redondeamos
        promedio_total_individual = round(sumatoria_total/ciclos)

        return promedio_total_individual


# Obtener promedio general

def promedio_grupal():

    id_list = []

    # Obtener la lista completa ID y NOMBRE
    lista = lista_completa()

    # Agregar solo los id a la lista id_list
    for linea in lista.keys():
        id_list.append(linea)

    promedios = {}

    aprobados = 0
    reprobados = 0

    # Por cada id en id_list verificar su promedio y agregarlos a promedios id:promedio

    for element in id_list:

        try:
            promedio = promedio_individual(element)
            promedios.update({element : promedio})

            if promedio >= configuracion.promedio_minimo_aprobatorio: aprobados+=1
            else: reprobados +=1

            
        except FileNotFoundError:
            repetir = False
            break

    # Obtener promedio grupal
    promedio_grupal = sum(promedios.values())/len(promedios)
    # Buscar cual es el promedio mas alto y a que id esta unida
    alumno_id, prom_max = max(promedios.items(),key=lambda x: x[1])
    # Buscar al alumno con esa id
    alumno = buscar_alumno(alumno_id)
    
    ID, nombre = alumno.popitem()

    print(f"✅️ -> Alumnos aprobados: {aprobados}")
    print(f"❌️ -> Alumnos reprobados: {reprobados}")

    print(f"⭐️ -> Promedio mas alto de ({ID}){nombre} -- {round(prom_max)}")

    return round(promedio_grupal)
