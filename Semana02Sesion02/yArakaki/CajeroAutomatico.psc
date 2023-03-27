Algoritmo CajeroAutomatico
	
	Definir cuenta1, cuenta2, opcion, monto, transferencia Como Real
	
	cuenta1 <- 0
	cuenta2 <- 0
	
	Repetir
		Escribir "Bienvenido al Cajero Automatico"
		Escribir "1. Consultar saldo"
		Escribir "2. Retirar dinero"
		Escribir "3. Depositar dinero"
		Escribir "4. Transferir dinero"
		Escribir "5. Salir"
		Leer opcion
		
		Segun opcion Hacer
			1: Escribir "Saldo cuenta 1: ", cuenta1
				Escribir "Saldo cuenta 2: ", cuenta2
			2: Escribir "¿De qué cuenta desea retirar? (1 o 2)"
				Leer cuenta
				Escribir "Ingrese el monto a retirar"
				Leer monto
				Si cuenta = 1 Entonces
					Si monto <= cuenta1 Entonces
						cuenta1 <- cuenta1 - monto
						Escribir "Retiro exitoso"
					SiNo
						Escribir "Fondos insuficientes"
					FinSi
				SiNo
					Si monto <= cuenta2 Entonces
						cuenta2 <- cuenta2 - monto
						Escribir "Retiro exitoso"
					SiNo
						Escribir "Fondos insuficientes"
					FinSi
				FinSi
			3: Escribir "¿A qué cuenta desea depositar? (1 o 2)"
				Leer cuenta
				Escribir "Ingrese el monto a depositar"
				Leer monto
				Si cuenta = 1 Entonces
					cuenta1 <- cuenta1 + monto
					Escribir "Deposito exitoso"
				SiNo
					cuenta2 <- cuenta2 + monto
					Escribir "Deposito exitoso"
				FinSi
			4: Escribir "Ingrese el monto a transferir"
				Leer transferencia
				Si transferencia <= cuenta1 Entonces
					cuenta1 <- cuenta1 - transferencia
					cuenta2 <- cuenta2 + transferencia
					Escribir "Transferencia exitosa"
				SiNo
					Escribir "Fondos insuficientes"
				FinSi
		FinSegun
		
	Hasta que opcion = 5
	
FinAlgoritmo
