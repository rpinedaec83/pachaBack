//Hacer un algoritmo en Pseint para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora.
Proceso Ejercicio06
	Definir horas_trabajadas,sueldo_semanal Como Entero
	sueldo_base=20
	sueldo_extra=25
	Escribir "Ingrese horas trabajadas en la semana "
	Leer horas_trabajadas
	Si horas_trabajadas>40 Entonces
		sueldo_semanal=horas_trabajadas*sueldo_extra
	SiNo
		sueldo_semanal=horas_trabajadas*sueldo_base
	Fin Si
	Escribir "El total que gana el trabajador por semana es: " sueldo_semanal
	
FinProceso
