def add_second(time):
    time_list = time.split(":")
    hour = int(time_list[0])
    minute = int(time_list[1])
    second = int(time_list[2])
    second += 1
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == 24:
        hour = 0
    return f"{hour:02}:{minute:02}:{second:02}"

# Ejemplo de uso
time = "23:59:59"
new_time = add_second(time)
print(f"La hora dentro de un segundo es {new_time}")
