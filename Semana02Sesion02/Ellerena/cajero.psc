Proceso Cajero

	saldoI = 1000
	saldoR = 0
	saldoF = 0
	Ncuenta = 0
	retiro = 0
	deposito = 0
	Dcuenta = 0
	Escribir "Hola, a que cuenta desea entrar ? "
	Escribir "Digita 1 entrar a cuenta de ahorros 1"
	Escribir "Digita 2 entrar a cuenta de ahorros 2 "
	
	Leer  operacion
	Segun operacion Hacer
		1:
			
			Escribir "Uste a entrado a la cuenta de ahorros 1 "
		2:
			
			Escribir "Uste a entrado a la cuenta de ahorros 2"
	FinSegun
	
	
	Escribir "Digite su numero de cuenta"
	Leer Ncuenta
	
	si Ncuenta > 15  y Ncuenta < 17 Entonces
		Escribir "su numero es incorrecto "
	SiNo
		Escribir "su numero de cuenta es correcto "
		
		Escribir "Dime la operacion que deseas realizar"
		Escribir "Pulsa 1 para retiro"
		Escribir "Pulsa 2 para deposito"
		Escribir "Pulsa 3 para tranferencia"
		Escribir "Pulsa 4 para cancelar operacion"
		
		Leer  operacion
		Segun operacion Hacer
			1:
				Escribir "Ingrese el monto a retirar"
				Leer retiro
				si retiro <1000 y retiro >= 0 Entonces
					
					Escribir "su retiro de " retiro " se realizo con exito"
					saldoR = saldoI - retiro
					Escribir "su saldo restante es de " saldoR
				SiNo
					Escribir "No puede retirar plata q no tiene"
						
				FinSi
				
			2:
				Escribir  "ingrese el numero de cuenta"
				Leer Dcuenta
				
				Escribir "ingrese la cantidada a depositar"
				Leer deposito
				
				saldoF = deposito + saldoI
				Escribir "su salfo final es de " saldof
				
			3:
				Escribir  "ingrese el numero de cuenta "
				Leer Dcuenta
				
				Escribir "Ingrese el monto a retirar"
				Leer retiro
				si retiro <1000 y retiro >= 0 Entonces
					
					Escribir "su transacción de " retiro " se realizo con exito"
					saldoR = saldoI - retiro
					Escribir "su saldo restante es de " saldoR
				SiNo
					Escribir "No puede transferir plata q no tiene"
					
				FinSi
		FinSegun
	FinSi
	
	
	
FinProceso
