import configuracion

def generar_id():
    with open(f"grupos/lista_completa.txt", "r") as lista:
        ids_existentes = []
        for alumno in lista:
            ID,nombre = alumno.strip().split(";")
            ids_existentes.append(int(ID))
        out = max(ids_existentes)+1
        return out
