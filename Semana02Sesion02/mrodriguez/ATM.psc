Proceso ATM
	//	Maritza Rodriguez
	Cuenta1= 123
	Cuenta2 = 987
	Saldo1 = 100
	Saldo2 = 200
	SaldoActual1 = 0
	SaldoActual2 = 0
	Operacion = 0
	Retiro = 0
	Deposito = 0
	Transferencia = 0

	Mientras Operacion<>4 Hacer
		Escribir "***********************"
		Escribir "MEN� DE TRANSACCIONES"
		Escribir "Elige una opci�n:"
		Escribir "1 = Retirar"
		Escribir "2 = Depositar"
		Escribir "3 = Transferir"
		Escribir "4 = Salir"

		leer Operacion
		Segun Operacion Hacer
			1:
				Escribir "Escr�be tu n�mero de cuenta: " Cuenta1 " o " Cuenta2
				leer Cuenta

				si Cuenta == Cuenta1 Y Saldo1<>0
					Escribir "Monto a retirar"
					leer Retiro
					si Retiro <= Saldo1
						SaldoActual1 = Saldo1 - Retiro
						Escribir "Saldo inicial: s/" Saldo1
						Escribir "Saldo actual: s/" SaldoActual1
					SiNo
						Escribir "Saldo insuficiente: s/" Saldo1
					FinSi
				SiNo
					si Cuenta == Cuenta2 Y Saldo2<>0
						Escribir "Monto a retirar"
						leer Retiro
						si Retiro <= Saldo2
							SaldoActual2 = Saldo2 - Retiro
							Escribir "Saldo inicial: s/" Saldo2
							Escribir "Saldo actual: s/" SaldoActual2
						SiNo
							Escribir "Saldo insuficiente: s/" Saldo2
						FinSi
					SiNO
						si Cuenta <> Cuenta1 O Cuenta <> Cuenta2
							Escribir "N�mero de cuenta incorrecto"
						FinSi
					FinSi
				FinSi
			2:
				Escribir "Escr�be n�mero de cuenta a depositar: " Cuenta1 " o " Cuenta2
				leer Cuenta

				si Cuenta = Cuenta1
					Escribir "Monto a depositar"
					leer Deposito
					SaldoActual1 = Saldo1 + Deposito
					Escribir "Monto depositado a cuenta " Cuenta ": s/" Deposito
					Operacion = 4
				SiNo
					si Cuenta == Cuenta2
						Escribir "Monto a depositar"
						leer Deposito
						SaldoActual2 = Saldo2 + Deposito
						Escribir "Monto depositado a cuenta " Cuenta ": s/" Deposito
						Operacion = 4
					SiNO
						si Cuenta <> Cuenta1 O Cuenta <> Cuenta2
							Escribir "N�mero de cuenta incorrecto"
						FinSi
					FinSi
				FinSi
			3:
				Escribir "Escr�be tu n�mero de cuenta: " Cuenta1 " o " Cuenta2
				leer Cuenta

				si Cuenta == Cuenta1
					Escribir "Cuenta destino"
					leer Cuenta
					si Cuenta <> Cuenta1 Y Cuenta = Cuenta2
						Escribir "Monto a transferir"
						leer Transferencia
						si Transferencia <= Saldo1
							SaldoActual1 = Saldo1 - Transferencia
							Escribir "Monto transferido a cuenta " Cuenta ": s/" Transferencia
							Escribir "Saldo inicial: s/" Saldo1
							Escribir "Saldo actual: s/" SaldoActual1
						SiNo
							Escribir "Saldo insuficiente: s/" Saldo1
						finSI
					SiNo
						Escribir "N�mero de cuenta destino incorrecto"
					finSI
				SiNo
					si Cuenta == Cuenta2
						Escribir "Cuenta destino"
						leer Cuenta
						si Cuenta <> Cuenta2 Y Cuenta = Cuenta1
							Escribir "Monto a transferir"
							leer Transferencia
							si Transferencia <= Saldo2
								SaldoActual2 = Saldo2 - Transferencia
								Escribir "Monto transferido a cuenta " Cuenta ": s/" Transferencia
								Escribir "Saldo inicial: s/" Saldo2
								Escribir "Saldo actual: s/" SaldoActual2
							SiNo
								Escribir "Saldo insuficiente: s/" Saldo2
							finSI
						SiNo
							Escribir "N�mero de cuenta destino incorrecto"
						finSI
					SiNo
						Escribir "N�mero de cuenta incorrecto"
					FinSi
				FinSi
			4:
				Escribir "Saliendo..."
			De Otro Modo:
				Escribir "Opci�n No V�lida"
		Fin Segun
	Fin Mientras
FinProceso
