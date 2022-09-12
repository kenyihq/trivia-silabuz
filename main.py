
def ejercicio_1():
    palabra = input("Ingresa una palabra: ")
    numero = int(input("Ingresa el número de veces que se repetirá: "))
    x = 0
    while x < numero:
        print(palabra)
        x += 1


def ejercicio_2():
    x = 0
    while x <= 10:
        if x == 5:
            print("Boom!")
        else:
          print(x)
        x += 1


def ejercicio_3():
    filas = int(input("Ingrese el número de filas: "))
    x = 0
    while x <= filas:
        print("+" * x)
        x += 1


def ejercicio_4():
    filas = int(input("Ingrese el número de filas: "))
    x = 0

    while x < filas:
        contador = 0
        while contador <= x:
            print("+", end=" ")
            contador += 1
        print(" ")
        x += 1

def reto_1():
  x = int(input("Ingrese el primer número: "))
  y = int(input("Ingrese el segundo número: "))
  print((x+y)/2)

def reto_2():
  x = int(input("Ingrese el primer número: "))
  y = int(input("Ingrese el segundo número: "))
  print(x**y)

def reto_3():
  x = int(input("Ingrese el primer número: "))
  print(x**0.5)

def reto_4():
  x = int(input("Ingrese el primer número: "))
  y = int(input("Ingrese el segundo número: "))
  print((x**2+ y**2)**(1/2))

def run():
    print("B I E N V E N I D O\n")
    print("Mi primer programa en Python")
    print("Clase 2 - Silabuz\n")
    print("Elije un ejercicio:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Reto - Invento mis reglas")
    print("\nby Tutankadev\n")
    opcion = input("Ingresa el numero de ejercicio: ")
    while True:
        if opcion == '1':
            ejercicio_1()
            break
        elif opcion == '2':
            ejercicio_2()
            break
        elif opcion == '3':
            ejercicio_3()
            break
        elif opcion == '4':
            ejercicio_4()
            break
        
        elif opcion == '5':
            print("Elegiste RETOS")
            print("Mi primer programa en Python")
            print("Clase 2 - Silabuz\n")
            print("Elije un ejercicio:")
            print("1. Reto 1")
            print("2. Reto 2")
            print("3. Reto 3")
            print("4. Reto 4")
            print("\nby Tutankadev\n")
            reto = input("Ingresa el numero de ejercicio: ")
            if reto == '1':
              reto_1()
              break
            elif reto == '2':
              reto_2()
              break
            elif reto == '3':
              reto_3()
              break
            elif reto == '4':
              reto_4()
              break
            else:
              print("Elija una opción válida")
              run()
              break
        else:
            print("Elija una opción válida")
            run()
            break
