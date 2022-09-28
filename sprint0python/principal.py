from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2

print()
print("\t\tMENU\n")
print("a) Función 1 Fibonacci")
print("b) Función 2 Fibonacci")
print()

opcion = input('Elige opción: ')
while (opcion != 'a') & (opcion != 'b'):
    opcion = input("La opción debe ser a o b: ")
print()

if(opcion=="a"):
    print("Teclea número:")
    n = input()
    print (funcion_fibonacci(float(n)))
else:
    print("Teclea número: ")
    n2 = input()
    print (funcion_fibonacci2(float(n2)))


