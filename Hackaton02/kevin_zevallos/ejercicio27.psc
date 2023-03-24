Algoritmo ejercicio27
    suma <- 0
    cantidad <- 0
	Escribir "Ingrese un número positivo: "
    Leer numero 
    Mientras numero > 0 Hacer
        suma <- suma + numero
        cantidad <- cantidad + 1
		Escribir "Ingrese otro número positivo (o escriba 0 par salir): "
        Leer numero 
    Fin Mientras
    Si cantidad > 0 Entonces
        media <- suma / cantidad
        Escribir "La media de los números ingresados es: ", media
    Sino
        Escribir "No se ingresaron números positivos"
    Fin Si
FinAlgoritmo