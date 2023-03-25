def get_day(number):
    days = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    if number < 1 or number > 7:
        return "Número inválido"
    else:
        return days[number-1]

# Ejemplo de uso
number = int(input("Ingresa un número del 1 al 7: "))
day = get_day(number)
print(f"El número {number} corresponde al día {day}")
