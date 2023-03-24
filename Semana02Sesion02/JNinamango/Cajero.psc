Algoritmo Cajero
	Operacion = 9999
	Saldo_Cuenta1 = 450
	Saldo_Cuenta2 = 450
	NroCuenta1 = 0//456 numero aceptado
	
	
	Escribir "Digite su numero de cuenta"
	Leer NroCuenta1
	
	Si NroCuenta1 == 456 Entonces
			Mientras Operacion <> 0 Hacer
				Escribir "Escoga la opcion"
				Escribir "(0)Salir"
				Escribir "(1)Retiro"
				Escribir "(2)Deposito"
				Escribir "(3)Transferencia"
				Leer Operacion
				
				SaldoPrevioATransaccion = Saldo_Cuenta1
				montoTransaccion = 0
				
				Segun Operacion Hacer
					1:
						Escribir "Monto que desea retirar"
						Leer montoTransaccion
						
						Si montoTransaccion > Saldo_Cuenta1 Entonces
							Escribir "No cuenta con esa cantidad"
						SiNo
							Saldo_Cuenta1 = Saldo_Cuenta1 - montoTransaccion

						Fin Si
						
					2:
						Escribir "Monto que desea depositar"
						Leer montoTransaccion
						Saldo_Cuenta1 = Saldo_Cuenta1 + montoTransaccion
						
					3:
						Escribir "Monto que desea transferir"
						Leer montoTransaccion
						
						Si montoTransaccion > Saldo_Cuenta1 Entonces
							Escribir "No cuenta con esa cantidad"
						SiNo
							Saldo_Cuenta1 = Saldo_Cuenta1 - montoTransaccion
							Saldo_Cuenta2 = Saldo_Cuenta1 + montoTransaccion
							Escribir "Saldo cuenta transferida: " Saldo_Cuenta2
						Fin Si

					De Otro Modo:
						Escribir "Opcion invalida"
				Fin Segun
				
				Escribir "Saldo previo a transaccion: " SaldoPrevioATransaccion
				Escribir "Saldo actual: " Saldo_Cuenta1
				Escribir "---------------------" 
				
		Fin Mientras
	SiNo
		Escribir  "Numero equivocado"
Fin Si


	

	
	
FinAlgoritmo
