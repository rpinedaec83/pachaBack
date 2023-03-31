''' Cajero automatico 
    en python con POO'''

class Cajero_Automatico:
    def __init__(self, codigo, direccion = None) -> None:
        pass
    # def funcion, retiro, deposito

    def retiro(self, cantidad_ret,cantidad_base):
        return int(cantidad_base) - int(cantidad_ret)
    def deposito(self, cantidad_dep,cantidad_base):
        return int(cantidad_base) + int(cantidad_dep)
    


class Persona:
    def __init__(self,nombre,apellido,dni) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


class Cliente(Persona):
    __saldo = 500
    def __init__(self, nombre, apellido, dni, n_cuenta) -> None:
        super().__init__(nombre, apellido, dni)
        self.n_cuenta = n_cuenta

    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, nuevoValor):
        self.__saldo = nuevoValor

class Acreedor(Cliente):
    __saldo = 1000
    def __init__(self, nombre, apellido, dni, n_cuenta) -> None:
        super().__init__(nombre, apellido, dni, n_cuenta)

    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, nuevoValor):
        self.__saldo = nuevoValor


cliente_base = Cliente("CLI_N_001","CLI_A_001","12345678","ACC001")

acreedor_base = Acreedor("ACR_N_002","ACR_A_002","12345678","ACC002")

print("Indique la transaccion que desea realizar desde el cliente hacia el acreedor.")
input_tx = int(input("Escriba 1 para Retiro \nEscriba 2 para Despoito\n"))

if input_tx == 1:
    input_01 = int(input("Indique el importe a descontar desde el cliente hacia el acreedor:"))
    if input_01 > cliente_base.getSaldo():
        print("La cantidad ingresada excede el saldo base del cliente, ingresar un monto menor.")
        quit()
    else:
        cliente_base.setSaldo(Cajero_Automatico(cliente_base.n_cuenta).retiro(input_01,cliente_base.getSaldo()))

    print("El saldo del cliente es: {}".format(cliente_base.getSaldo()) )

elif input_tx == 2:
    input_02 = int(input("Indique el importe a añadir desde el cliente hacia el acreedor:"))

    if input_02 > cliente_base.getSaldo():
        print("La cantidad ingresada excede el saldo base del cliente, ingresar un monto menor.")
        quit()
    else:
        acreedor_base.setSaldo(Cajero_Automatico(cliente_base.n_cuenta).deposito(input_02,acreedor_base.getSaldo()))
        cliente_base.setSaldo(cliente_base.getSaldo()-input_02)

    print("El saldo del cliente es: {}".format(cliente_base.getSaldo()))
    print("El saldo del acreedor es: {}".format(acreedor_base.getSaldo()))


