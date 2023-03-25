hora = input("Ingrese la hora en formato HH:MM:SS: ")
hora_siguiente = ""
if len(hora) == 8 and hora[2] == ":" and hora[5] == ":":
    horas = int(hora[:2])
    minutos = int(hora[3:5])
    segundos = int(hora[6:])
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59 or segundos < 0 or segundos > 59:
        print("Hora inválida.")
    else:
        if segundos == 59:
            segundos = 0
            if minutos == 59:
                minutos = 0
                if horas == 23:
                    horas = 0
                else:
                    horas += 1
            else:
                minutos += 1
        else:
            segundos += 1

        hora_siguiente = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        print(f"La hora siguiente es: {hora_siguiente}")
else:
    print("Formato de hora inválido. Debe ser en formato HH:MM:SS.")
