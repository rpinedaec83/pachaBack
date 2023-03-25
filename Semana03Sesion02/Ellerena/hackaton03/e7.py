horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en la semana: "))
pago_hora_normal = 20
pago_hora_extra = 25

if horas_trabajadas <= 40:
    sueldo_semanal = horas_trabajadas * pago_hora_normal
else:
    horas_extras = horas_trabajadas - 40
sueldo_semanal = 40 * pago_hora_normal + horas_extras * pago_hora_extra

print("Su sueldo semanal es:", sueldo_semanal)