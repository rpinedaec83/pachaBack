Algoritmo PiNilakantha
	op = 9999
	salcuen1 = 450
	salcuen2 = 450
	numcuen1 = 0
	Escribir "Escriba su numero de cuenta"
	Leer numcuen1
	
	Si numcuen1 = 456 Entonces
		Mientras op = 0 Hacer
			Escribir "Escoga la opcion"
			Escribir "(0)Salir"
			Escribir "(1)Retiro"
			Escribir "(2)Deposito"
			Escribir "(3)Transferencia"
			Leer op
			saldop = salcuen1
			monto = 0
			
			Segun op Hacer
				1:
					Escribir "Monto a retirar"
					Leer monto
					
					Si monto > salcuen1 Entonces
						Escribir "Saldo insuficiente ingrese otra cantidad"
					SiNo
						salcuen1 = salcuen1 - monto
						
					Fin Si
					
				2:
					Escribir "Monto a depositar"
					Leer monto
					salcuen1 = salcuen1 + monto
					
				3:
					Escribir "Monto a transferir"
					Leer monto
					
					Si monto > salcuen11 Entonces
						Escribir "Saldo insuficiente ingrese otra cantidad"
					SiNo
						salcuen1 = salcuen1 - monto
						salcuen2 = salcuen1 + monto
						Escribir "Saldo cuenta transferida: " salcuen2
					Fin Si
					
				De Otro Modo:
					Escribir "Opción invalida"
			Fin Segun
			
			Escribir "Saldo inicial: " saldop
			Escribir "Saldo actual: " salcuen1
			
		Fin Mientras
	SiNo
		Escribir  "Número no existente"
	Fin Si
FinAlgoritmo
