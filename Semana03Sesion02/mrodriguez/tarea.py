# Conjetura de Collatz
number = int(input("Enter a number: "))
steps = 0

while number != 1:
    steps += 1
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    continue

print(f"The number of steps to 4 --> 2 --> 1 is: {steps}")
