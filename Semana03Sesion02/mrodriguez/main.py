import miModulo

# modulo.funcion(valor)
# miModulo.greeting("from main")

# age = miModulo.getInfo("Writte your age")

# print(f"your age is {age} years")

# name = input("Write your name ")
# age = input("Write your age ")

# int: entero
# f: para dar formato de string (template string)
# print(f"your age is: {age} years and its middle is {int(age)/2}")
# print("your age is: " + age + " years and its middle is " + str(int(age)/2))
# print("your age is:", age, "years and its middle is", int(age)/2)

# exception: para mostrar errores
# try:
#     age = int(input("Please enter your age"))
#     print(f"Your age is:  {age}")
# except Exception as ex:
#     print("An error occurred", ex)
# finally:
#     print("Thanks for using the program")

# exception: para mostrar errores, con while
# while True:
#     try:
#         x = int(input("Please enter a number "))
#         print(f"The number is: {x}")
#         break
#     except ValueError:
#         print("You have to enter a number...")

# Condicional IF/ELSE
# grade = int(input("Write your grade "))
# if grade >= 14:
#     print(f"You pass with {grade}")
# else:
#     print(f"Sorry, you don't pass with {grade}")

# Like SWITCH
# option = int(input("Enter your option in number "))

# if option == 1:
#     print(f"You choose option {option}")
# elif option == 2:
#     print(f"You choose option {option}")
# elif option == 3:
#     print(f"You choose option {option}")
# elif option == 4:
#     print(f"You choose option {option}")
# else:
#     print(f"You choose other option")


# sum = 0
# i = 1
# while i <= 100:
#     sum += i  # sum = sum + i
#     i += 1
#     # ver donde se coloca print
#     # print(f"The sum is: {sum}")
# print(f"The sum is: {sum}")

# LISTAS - FOR
# list = ["avion", "autos", "barcos", "moto", "bicicleta"]
# for transport in list:
#     print(f"You are using {transport}")
#     if transport == "autos":
#         break  # cuando sea autos se corta

# FOR
# for value in range(0, 10, 2):
#     print(value)
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# conjetura de Collatz
# par: /2
# impar: *3 +1

# 16 --> 16/2 = 8/2 = 4/2 = 2/2 = 1+3 = 4
# 17 --> 17*3+1 = 52/2 = 26/2 = 13*3+1 = 40/2 = 20/2 = 10/2 = 5*3+1 = 16/2 = 8/2 = 4/2 = 2/2 = 1*3+1
# 1       2   3      4        5
number = int(input("Enter a number: "))
steps = 0

while number != 1:
    steps += 1
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    continue

print(f"The step number until 4 --> 2 --> 1 is: {steps}")
