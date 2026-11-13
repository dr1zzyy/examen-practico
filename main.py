import funciones
import configuracion
from configuracion import promedio_minimo_aprobatorio as promedio_min

from funciones.registrar_alumno import registrar
from funciones.agregar_calificaciones import agg_calificaciones
from funciones.calcular_promedio import promedio_individual, promedio_grupal
from funciones.lista_completa import lista_completa
from funciones.buscar_alumno import buscar_alumno

import os

# Borrar todo en consola
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# Print para mostrar el menu
def mostrar_menu():
    print("┌───────────────────────────────────────────┐")
    print("│            SISTEMA DE ALUMNOS       [📚️]  │")
    print("├───────────────────────────────────────────┤")
    print("│                             │             │")
    print("│[1] Registrar estudiante     │             │")
    print("│[2] Ver lista de alumnos     │             │")
    print("│[3] Consultar alumno         │             │")
    print("│[4] Estadistica grupal       │[5] Salir -> │")
    print("│_____________________________│_____________│")
    print("└───────────────────────────────────────────┘")
    print()


# menu principal
def menu():
    while True:
        limpiar()
        mostrar_menu()
        seleccion = input("Elige una opcion > ")

        if seleccion == "1":
            calificaciones = []
            nombre = input(">> Ingresa el nombre del alumno a registar: ")

            for i in range(1,4):
            
                calificacion = int(input(f">> Ingresa la calificacion numero ({i}): "))
                if not (0 <= calificacion <= 100):
                    print("Estas ingresando una calificacion invalida. No se enviara el registro.")
                calificaciones.append(calificacion)
                    
            if any(c > 100 or c < 0 for c in calificaciones):
                continue
                    

            if nombre == "":
                print("Ingresa un nombre")
                continue

            print("\b>> Registrando....")
            print("────────────────────────────────────────────")
            registrar(nombre, calificaciones)
            print("────────────────────────────────────────────")
            input("\nEnter para volver...")
            

        elif seleccion == "2":

            print("\n>> Lista de alumnos....")

            lista = lista_completa()

            print("────────────────────────────────────────────")
            for alumno in lista.keys():
                print(f"{alumno} - {lista[alumno]}")
            print("────────────────────────────────────────────")
            input("\nEnter para volver...")

        elif seleccion == "3":
            ID = input(">> Ingresa el id del alumno: ")
            print(">> Buscando alumno....")
            
            alumno = buscar_alumno(ID)
            promedio = promedio_individual(ID)

            print("──", "✅️ Aprobado"if promedio>=promedio_min else "❌️ Reprobado","─────────────────────────────────────────")
            for value in alumno.keys():
                print(f"{value} - {alumno[value]}")
                print(f"Promedio: {promedio} ")
            print("────────────────────────────────────────────────────────")
            input("\nEnter para volver...")

        elif seleccion == "4":
            print(">> Obteniendo promedio grupal....")
            lista = lista_completa()
            print("──────────────────────────────────────────────────────────────")
            promedio = promedio_grupal()
            print(f"👤 -> {len(lista)} alumnos en el grupo {configuracion.grupo_predeterminado}")
            if promedio>=promedio_min:
                print("──✅️ En regla──────────────────────────────────────────")
            else:
                print("❌️ Promedio bajo──────────────────────────────────────────")
            print(f"Promedio general del grupo: {promedio}")
            print("──────────────────────────────────────────────────────────────")
            input("\nEnter para volver...")
        elif seleccion == "5":
            limpiar()
            print("Saliendo del sistema.")
            break
        else:
            print(f"Seleccion invalida: '{seleccion}'")
            input("Enter para volver...")


menu()