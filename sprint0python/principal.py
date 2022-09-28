from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2
import time

print()
print("\t\tMENU\n")
print("a) Función 1 Fibonacci")
print("b) Función 2 Fibonacci")
print()

opcion = input('Elige opción: ')
while (opcion != 'a') & (opcion != 'b'):
    opcion = input("La opción debe ser a o b: ")
print()

if opcion == 'a':
    print("Teclea número:")
    n = input()
    start = time.time()  # Comienza a contar
    print(funcion_fibonacci(float(n)))
    end = time.time()  # Termina de contar
    elapsed = end - start
    print('El tiempo de ejecución ha sido :' + str(elapsed) + ' s')

else:
    print("Teclea número: ")
    n2 = input()
    start = time.time()
    print(funcion_fibonacci2(float(n2)))
    end = time.time()
    elapsed = end - start
    print('El tiempo de ejecución ha sido :' + str(elapsed) + ' s')
