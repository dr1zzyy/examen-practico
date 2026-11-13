# Sistema de Alumnos 📚️

```El readme.md lo hice con IA, unicamente el README.md```

Programa de consola escrito en Python para registrar alumnos, guardar sus
calificaciones y consultar estadísticas de un grupo. Los datos se guardan en
archivos de texto, así que no necesitas base de datos ni instalar nada extra.

## ¿Qué hace?

- Registrar un estudiante con su nombre y 3 calificaciones (0 a 100).
- Mostrar la lista completa de alumnos.
- Consultar un alumno por su ID y ver su promedio (Aprobado / Reprobado).
- Ver estadísticas del grupo: promedio general, cuántos aprobaron y reprobaron,
  y el alumno con el promedio más alto.


Aparecerá un menú donde eliges una opción escribiendo su número y presionando
Enter.

```
[1] Registrar estudiante
[2] Ver lista de alumnos
[3] Consultar alumno
[4] Estadistica grupal
[5] Salir
```

## ¿Cómo funciona por dentro?

La idea principal es **separar el menú de la lógica**. `main.py` solo muestra el
menú y llama a las funciones; cada función vive en su propio archivo dentro de
`funciones/`.

### Estructura del proyecto

```
examen_practico/
├── main.py                  # Menú y punto de entrada del programa
├── configuracion.py         # Ajustes (grupo y promedio mínimo)
├── funciones/
│   ├── registrar_alumno.py      # Registra un alumno nuevo
│   ├── crear_id.py              # Genera un ID único
│   ├── agregar_calificaciones.py# Guarda las calificaciones
│   ├── lista_completa.py        # Lee todos los alumnos
│   ├── buscar_alumno.py         # Busca un alumno por ID
│   └── calcular_promedio.py     # Promedios individual y grupal
└── grupos/
    ├── lista_completa.txt   # Lista de todos los alumnos (ID;Nombre)
    └── 101/                 # Un archivo .txt por alumno
        ├── 1.txt
        ├── 2.txt
        └── ...
```

### ¿Cómo se guardan los datos?

Todo se guarda en texto plano, usando `;` como separador.

**Lista de alumnos** (`grupos/lista_completa.txt`), un alumno por línea:

```
1;Roman
2;Camila
3;Juan
```

**Calificaciones de un alumno** (`grupos/101/{ID}.txt`):

```
99;98;97
```

Cada vez que registras un alumno se crea su archivo `{ID}.txt` vacío y luego se
escriben sus calificaciones en él.

### El ID de cada alumno

`crear_id.py` lee la lista completa, toma el ID más alto y le suma 1. Así el
primer alumno es el `1`, el siguiente el `2`, y nunca se repiten.

### Los promedios

- **Promedio individual**: lee el archivo del alumno, saca el promedio de cada
  línea y luego el promedio de esos resultados. Si el alumno no tiene
  calificaciones, devuelve `0` para no afectar al grupo.
- **Promedio grupal**: recorre todos los alumnos, calcula su promedio, cuenta
  aprobados y reprobados (según `promedio_minimo_aprobatorio`) y encuentra el
  promedio más alto.

### Configuración

En `configuracion.py` puedes cambiar sin tocar el resto del código:

```python
grupo_predeterminado = "101"          # Carpeta del grupo a usar
promedio_minimo_aprobatorio = 70      # Nota mínima para aprobar
```

## Notas

- Se recomienda crear los grupos dentro de `grupos/` (por ejemplo `grupos/101/`)
  antes de ejecutar el programa.
- El programa limpia la consola entre acciones para mantener el menú legible.
