from archivo_alumnos import Alumno


def generar_reporte_alumnos():
    with open("alumnos.txt", "r") as archivo:
        datos = archivo.readlines()
        for i, dato in enumerate(datos):
            datos_alumno = dato.strip().split(",")
            nombre = datos_alumno[0]
            dni = datos_alumno[1]
            edad = datos_alumno[2]
            notas = list(map(float, datos_alumno[3:]))
            alumno = Alumno(nombre, dni, edad, notas)
            nota_maxima = alumno.obtener_nota_maxima()
            promedio = alumno.calcular_promedio()
            nota_minima = min(notas)
            numero = i + 1
            print(f"nro : <{numero}>  (  - Alumno: {nombre}, máxima nota : {nota_maxima}, minima nota : {nota_minima}, promedio : {promedio})")
