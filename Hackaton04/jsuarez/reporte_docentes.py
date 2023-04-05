def generar_reporte_docentes():
    with open("docentes.txt", "r") as archivo:
        datos = archivo.readlines()
        for dato in datos:
            datos_docente = dato.strip().split(",")
            nombre = datos_docente[0]
            dni = datos_docente[1]
            edad = datos_docente[2]
            print(f"Docente: {nombre}, Edad: {edad}, DNI: {dni}")
