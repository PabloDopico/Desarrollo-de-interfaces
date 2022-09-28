import random

puntuacion = 0
numero = 0
lista=[1,2,3]

random = random.sample(lista,2)
print(random)

if random[0]==1 or random[1]==1:
    print("¿Cuánto es la raíz cuadrada de 144?:")
    print("a) 12")
    print("b) 14")
    print("c) 16")

    print()
    respuesta = input("Respuesta: ")
    print()

    if respuesta == "a":
        puntuacion += 10
    else:
        puntuacion -= 5

if random[0]==2 or random[1]==2:
    print("¿Cuál es la capital de Madagascar?:")
    print("a) Ankara")
    print("b) Antananarivo")
    print("c) Atenas")

    print()
    respuesta = input("Respuesta: ")
    print()

    if respuesta == "b":
        puntuacion += 10
    else:
        puntuacion -= 5

if random[0]==3 or random[1]==3:
    print("¿Cuándo acabó la Segunda Guerra Mundial?:")
    print("a) 1939")
    print("b) 1941")
    print("c) 1945")
    print()
    respuesta = input("Respuesta: ")
    print()

    if respuesta == "c":
        puntuacion += 10
    else:
        puntuacion -= 5

print("Puntuacion Total:", puntuacion)
