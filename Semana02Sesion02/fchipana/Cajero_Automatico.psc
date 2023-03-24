Proceso Cajero_Automatico
	
	respuesta = ""
	numero_cuenta = ""
	acc_01 = 10000
	acc_02 = 5000
	
Mientras  respuesta <> "Salir"
	Escribir "Ingrese su numero de cuenta o escriba SALIR para detener el programa. "
	Leer numero_cuenta
	
	Segun numero_cuenta Hacer
		"cuenta1":
			saldo_actual = acc_01
			saldo_actual_otro = acc_02
			tx = 0
			Escribir "Indique la transaccion a realizar:"
			Escribir "Digita 1 para Retiro"
			Escribir "Digita 2 para Deposito"
			Escribir "Digita 3 para Transferencia"
			Leer tx
			
			Segun tx Hacer
				1:
					rpta_tx = tarea_retiro(saldo_actual)
					acc_01 = acc_01+ rpta_tx
				2:
					rpta_tx = tarea_deposito(saldo_actual)
					acc_01 = acc_01+ rpta_tx
				3:
					rpta_tx = tarea_transferencia(saldo_actual,saldo_actual_otro)
					acc_01 = acc_01- rpta_tx
					acc_02 = acc_02+ rpta_tx
					
				De Otro Modo:
					Escribir "Opcion No valida."
			Fin Segun			
			
		"cuenta2":
			saldo_actual = acc_02
			saldo_actual_otro = acc_01
			tx = 0
			Escribir "Indique la transaccion a realizar:"
			Escribir "Digita 1 para Retiro"
			Escribir "Digita 2 para Deposito"
			Escribir "Digita 3 para Transferencia"
			Leer tx
			
			Segun tx Hacer
				1:
					rpta_tx = tarea_retiro(saldo_actual)
					acc_02 = acc_02+ rpta_tx
				2:
					rpta_tx = tarea_deposito(saldo_actual)
					acc_02 = acc_02+ rpta_tx
				3:
					rpta_tx = tarea_transferencia(saldo_actual,saldo_actual_otro)
					acc_02 = acc_02- rpta_tx
					acc_01 = acc_01+ rpta_tx
					
				De Otro Modo:
					Escribir "Opcion No valida."
			Fin Segun	
		"SALIR":
			respuesta = "Salir"
		De Otro Modo:
			escribir "Numero de cuenta no existe."
	Fin Segun
	
FinMientras

	
FinProceso


Funcion retiro <- tarea_retiro(saldo_ini Por Referencia) 
	cantidad = 0
	Escribir "Ingrese la cantidad a retirar:"
	Leer cantidad
	
	si cantidad <=saldo_ini
		escribir "Retiro aprobado por " cantidad
		saldo_fin = saldo_ini - cantidad
		Escribir "Su saldo actual es " saldo_fin
		retiro = (cantidad	- (cantidad * 2))
	SiNo
		Escribir "Cantidad ingresada excede el saldo actual."
		retiro = cantidad
	FinSi

FinFuncion

Funcion deposito <- tarea_deposito(saldo_ini Por Referencia) 
	cantidad = 0
	Escribir "Ingrese la cantidad a depositar:"
	Leer cantidad
	
	si cantidad > 0
		escribir "Deposito aprobado por " cantidad
		saldo_fin = saldo_ini + cantidad
		Escribir "Su saldo actual es " saldo_fin
		deposito = cantidad
	SiNo
		Escribir "Cantidad deposito no puede ser 0."
		deposito = cantidad
	FinSi
	
FinFuncion

Funcion transferencia <- tarea_transferencia(saldo_acc1 Por Referencia,saldo_acc2 Por Referencia) 
	cantidad = 0
	Escribir "Ingrese la cantidad a transferir:"
	Leer cantidad
	
	si cantidad <=saldo_acc1
		escribir "Trasnferencia aprobada por " cantidad
		saldo_origen = saldo_acc1 - cantidad
		saldo_destino = saldo_acc2 + cantidad
		Escribir "El saldo de cuenta origen es " saldo_origen
		Escribir "El saldo de cuenta destino es " saldo_destino
		transferencia = cantidad
	SiNo
		Escribir "Cantidad ingresada excede el saldo actual."
		retiro = cantidad
	FinSi
	
FinFuncion




