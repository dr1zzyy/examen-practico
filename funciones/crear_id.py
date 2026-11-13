import configuracion

# Modulo que genera id nuevas, la id siempre es un numero mayor a la id mas nueva
def generar_id():
    with open(f"grupos/lista_completa.txt", "r") as lista:
        ids_existentes = []
        for alumno in lista:
            ID,nombre = alumno.strip().split(";")
            ids_existentes.append(int(ID))
        if len(ids_existentes) == 0:
            out = 1
        else:
            out = max(ids_existentes)+1
        return out
