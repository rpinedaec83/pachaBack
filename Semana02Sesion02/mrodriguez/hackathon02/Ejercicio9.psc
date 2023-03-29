Proceso Ejercicio9
	//Hacer un algoritmo en Pseint para determinar
	//el aumento de un trabajador,
	//se debe tomar en cuenta que
	//si ganaba m�s de $2000 tendr� un aumento del 5%,
	//si generaba menos de $2000 su aumento ser� de un 10%.

	nuevoSueldo = 0
	Escribir "Ingresar sueldo: "
	leer sueldo

	si sueldo > 2000 Entonces
		nuevoSueldo = sueldo + (sueldo*0.05)
		Escribir "Nuevo sueldo: " nuevoSueldo
	SiNo
		si sueldo <= 2000 Entonces
			nuevoSueldo = sueldo + (sueldo*0.1)
			Escribir "Nuevo sueldo: " nuevoSueldo
		FinSi
	FinSi
FinProceso
