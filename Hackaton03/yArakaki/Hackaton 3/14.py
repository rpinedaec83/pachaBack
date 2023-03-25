num = int(input("Ingrese un número entre 1 y 10: "))

if num <= 1:
    print("El número no es primo")
elif num <= 3:
    print("El número es primo")
elif num % 2 == 0 or num % 3 == 0:
    print("El número no es primo")
else:
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            print("El número no es primo")
            break
        i += 6
    else:
        print("El número es primo")
