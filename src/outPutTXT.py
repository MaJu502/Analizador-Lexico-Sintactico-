def generarOUT(nombreArchivo, data):

    with open(nombreArchivo + ".txt", "w") as f:
        for line in data:
            f.write(line)