horas_trabajadas = int(input("Ingrese las horas trabajadas en la semana: "))
pago_hora_normal = 20
pago_hora_extra = 25

if horas_trabajadas <= 40:
    sueldo_semanal = horas_trabajadas * pago_hora_normal
else:
    horas_extra = horas_trabajadas - 40
    sueldo_semanal = 40 * pago_hora_normal + horas_extra * pago_hora_extra

print("El sueldo semanal del trabajador es:", sueldo_semanal)
