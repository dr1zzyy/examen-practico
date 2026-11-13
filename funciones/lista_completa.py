# Devolver una lista completa dict con el id y el nombre de todos los estudiantes id:nombre
def lista_completa():
    with open(f"grupos/lista_completa.txt", "r") as lista:
        out = {}
        for line in lista:
            aid,nombre = line.strip().split(";")
            out.update({aid : nombre})
        return(out)