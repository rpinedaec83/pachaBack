Algoritmo sin_titulo
	//6.-Hacer un algoritmo en Pseint para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, 
	//se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora.
		HorasExtra <- 0;
		sueldo <- 0;
		
		Escribir "Ingresar horas trabajadas:";
		Leer HorasTrab;
		
		si (HorasTrab < 40) entonces
			sueldo <- HorasTrab * 20;
			Escribir "El sueldo que le corresponde esta semana es de: ",sueldo;
		SiNo
			HorasExtra <- HorasTrab - 40;
			sueldo <- (HorasTrab - HorasExtra) * 20;
			Escribir "El sueldo que le corresponde esta semana es de: ",sueldo + (HorasExtra * 25);
		FinSi
		

FinAlgoritmo
