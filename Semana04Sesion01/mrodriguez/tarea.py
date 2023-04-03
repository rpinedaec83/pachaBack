class ATM:
    def __init__(self, code=None, address=None):
        self.code = code
        self.address = address

    def operations(
        self, option, startingAmount, withdrawalAmount=None, depositAmount=None
    ):
        if option == 1:  # retiro
            return startingAmount - withdrawalAmount
        elif option == 2:  # depósito
            return startingAmount + depositAmount


class Person:
    def __init__(self, name, lastname, idCard):
        self.name = name
        self.lastname = lastname
        self.idCard = idCard


class Customer(Person):
    __balance = 500  # saldo

    def __init__(self, name, lastname, idCard, accountNumber=None):
        super().__init__(name, lastname, idCard)
        self.accountNumber = accountNumber

    def getBalance(self):
        return self.__balance

    def setBalance(self, newValue):
        self.__balance = newValue


class Creditor(Person):
    __balance = 1000

    def __init__(self, name, lastname, idCard, accountNumber=None):
        super().__init__(name, lastname, idCard)
        self.accountNumber = accountNumber

    def getBalance(self):
        return self.__balance

    def setBalance(self, newValue):
        self.__balance = newValue


customer1 = Customer(
    name="Mari",
    lastname="Ro",
    idCard="12345678",
    accountNumber="003202301410410",
)

creditor1 = Creditor(
    name="Jane",
    lastname="Doe",
    idCard="74859641",
    accountNumber="001205301410420",
)

print("MENÚ DE TRANSACCIONES")
print("Elige una opción:")
print("1 = Retirar, 2 = Depositar, 3 = Salir")
option = None
while option is None:
    try:
        option = int(input("Opción: "))
        if option == 1:
            account = None
            while account is None or customer1.accountNumber != account:
                account = input("Ingresar tu número de cuenta (003202301410410): ")
                if customer1.accountNumber == account:
                    print(f"Hola {customer1.name}!")
                    value = None
                    while value is None:
                        try:
                            value = int(input("Ingresa monto a retirar: "))

                            if value > customer1.getBalance():
                                print("Saldo insuficiente.")
                            else:
                                print(f"Saldo inicial: ${customer1.getBalance()}")
                                customer1.setBalance(
                                    ATM().operations(
                                        option, customer1.getBalance(), value, None
                                    )
                                )
                                print(f"Saldo actual: ${customer1.getBalance()}")

                        except ValueError:
                            print(f"Ingresa número entero")
                else:
                    print(f"Verifica número de cuenta")
        elif option == 2:
            account = None
            while account is None or creditor1.accountNumber != account:
                account = input(
                    "Ingresar número de cuenta de acreedor (001205301410420): "
                )
                if creditor1.accountNumber == account:
                    value = None
                    while value is None:
                        try:
                            value = int(
                                input(
                                    f"Ingresa monto a depositar a {creditor1.name} {creditor1.lastname}: "
                                )
                            )
                            if value > customer1.getBalance():
                                print("Saldo insuficiente.")
                            else:
                                print(
                                    f"Saldo inicial acreedor: ${creditor1.getBalance()}"
                                )
                                creditor1.setBalance(
                                    ATM().operations(
                                        option, creditor1.getBalance(), None, value
                                    )
                                )
                                print(
                                    f"Saldo actual acreedor: ${creditor1.getBalance()}"
                                )
                                print(f"My saldo inicial: ${customer1.getBalance()}")
                                customer1.setBalance(
                                    ATM().operations(
                                        1, customer1.getBalance(), value, None
                                    )
                                )
                                print(f"My saldo actual: ${customer1.getBalance()}")

                        except ValueError:
                            print(f"Ingresa número entero")
                else:
                    print(f"Verifica número de cuenta")
        elif option == 3:
            print(f"Saliendo... Bye")
        else:
            print(f"Opción no válida")
    except ValueError:
        print(f"Debe ingresar opción: 1, 2 o 3")
