import random

nombres = ["Ana", "Pedro", "Lucia", "Juan", "Maria", "Diego", "Sofia", "Miguel", "Valentina", "Andres", "Camila", "Felipe", "Carla", "Gabriel", "Laura"]
apellidos = ["Garcia", "Perez", "Gonzalez", "Hernandez", "Martinez", "Lopez", "Rodriguez", "Fernandez", "Sanchez", "Romero", "Ruiz", "Diaz", "Alvarez", "Moreno", "Torres"]

for i in range(15):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    edad = random.randint(18, 60)
    dni = random.randint(10000000, 99999999)
    genero = random.choice(['M', 'F'])
    email = f"{nombre.lower()}.{apellido.lower()}@idat.edu.pe"
    notas = sorted([random.randint(10, 20) for _ in range(4)], reverse=True)
    promedio = sum(notas) // len(notas)
    print(f"{nombre}-{apellido}-{edad}-{dni}-{genero}-{email}-{notas}-{promedio}")
