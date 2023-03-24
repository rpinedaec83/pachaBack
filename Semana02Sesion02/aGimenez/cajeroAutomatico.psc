Proceso cajeroAutomatico
	Operacion = -1
	nroDNI = 0
	nroCuenta1 = 9954
	nroCuenta2 = 7038
	nroCuentaOperacion = 0
	saldoInicialCta1 = 1200
	saldoInicialCta2 = 1500
	saldoCta1 = 1200
	saldoCta2 = 1500
	montoOperacion = 0
	
	Escribir "Ingrese un numero de DNI"
	Leer nroDNI
		Mientras Operacion<>0 Hacer
			Escribir "Menu - Elija una Operacion"
			Escribir "0- Salir"
			Escribir "1- Retiro"
			Escribir "2- Deposito"
			Escribir "3- Transferencia"
			Escribir "4- Consultar Saldo"
			Leer Operacion
				
			Segun Operacion Hacer

				1: Escribir "Monto que desea Retirar"
					leer montoOperacion
					Escribir "Nro de Cuenta a Retirar"
					leer nroCuentaOperacion
					si nroCuentaOperacion == nroCuenta1 Entonces
						si montoOperacion<saldoCta1 Entonces
							saldoCta1 = saldoCta1 - montoOperacion
							Escribir "Nuevo Saldo es de $" saldoCta1
						SiNo
							Escribir "No cuenta con saldo suficiente"
						FinSi
						si nroCuentaOperacion == nroCuenta2 Entonces
							si montoOperacion<saldoCta2 Entonces
								saldoCta1 = saldoCta1 - montoOperacion
								Escribir "Nuevo Saldo es de $" saldoCta1
							SiNo
								Escribir "No cuenta con saldo suficiente"
							FinSi
						FinSi
					SiNo
						Escribir"Numero de Cuenta Equivocada"
					FinSi
					
				2: Escribir "Monto que desea Depositar"
					leer montoOperacion
					Escribir "Nro de Cuenta a Depositar"
					leer nroCuentaOperacion
					si nroCuentaOperacion == nroCuenta1 Entonces
						saldoCta1 = saldoCta1 + montoOperacion
						Escribir "Nuevo Saldo es de $" saldoCta1
						si NroCuentaOperacion == nroCuenta2 Entonces
							saldoCta2 = saldoCta2 + montoOperacion
							Escribir "Nuevo Saldo es de $" saldoCta2
						FinSi
					SiNo
						Escribir"Numero de Cuenta Equivocada"
					FinSi
					
				3: Escribir "Monto que Desea Transferir"
					leer montoOperacion
					Escribir "Nro de Cuenta a Transferir"
					leer nroCuentaOperacion
					si nroCuentaOperacion == nroCuenta1 Entonces
						si saldoCta2 > montoOperacion Entonces
							saldoCta1 = saldoCta1 + montoOperacion
							saldoCta2 = saldoCta2 - montoOperacion
							Escribir "Nuevo Saldo es de $" saldoCta2
						SiNo
							Escribir "No cuenta con saldo suficiente"
						FinSi
						
						si nroCuentaOperacion == nroCuenta2 Entonces
							nroCuenta2 = NroCuentaOperacion
							si saldoCta2 > montoOperacion Entonces
								saldoCta2 = saldoCta2 + montoOperacion
								saldoCta1 = saldoCta1 - montoOperacion
								Escribir "Nuevo Saldo es de $" saldoCta1
							SiNo
								Escribir "No cuenta con saldo suficiente"
							FinSi
						FinSi
						
					SiNo
						Escribir"Numero de Cuenta Equivocada"
					FinSi
						
				4: Escribir "Nro de Cuenta a Consultar"
					leer nroCuentaOperacion
					si nroCuentaOperacion == nroCuenta1 y nroCuentaOperacion <> nroCuenta2 Entonces
						Escribir "Saldo de la cuenta " nroCuenta1 " es: $" saldoCta1
					FinSi
					si nroCuentaOperacion == nroCuenta2 y nroCuentaOperacion <> nroCuenta1 Entonces
						Escribir "Saldo de la cuenta " nroCuenta2 " es: $" saldoCta2
					FinSi
					si nroCuentaOperacion <> nroCuenta2 y nroCuentaOperacion <> nroCuenta1 Entonces
						Escribir "Numero Cuenta Equivocada"
					FinSi
			FinSegun
		FinMientras
		
		si nroCuentaOperacion <> 0 Entonces
			Escribir "Saldo Inicial de la cuenta " nroCuenta1 " es: $" saldoInicialCta1
			Escribir "Saldo Final de la cuenta " nroCuenta1 " es: $" saldoCta1
			Escribir "Saldo Inicial de la cuenta " nroCuenta2 " es: $" saldoInicialCta2
			Escribir "Saldo Final de la cuenta " nroCuenta2 " es: $" saldoCta2
		FinSi
FinProceso
