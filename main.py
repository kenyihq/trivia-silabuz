import os

# Trivia 1
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

# Clase 3
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

# Clase 4
def reto2_1():
  x = int(input("Ingrese su edada: "))
  x = [i for i in range(1, x+1)]
  print(x)

def reto2_2():
  x = int(input("Ingrese su edad: "))
  x = [i for i in range(1, x+1) if i%2!=0]
  print(x)

def reto2_3():
  x = int(input("Ingrese un número: "))
  factorial = 1
  for i in range(1, x):
    factorial += i*factorial
  print(factorial)

#Clase 5
def reto3_1():
  x = int(input("Ingrese un número del 1 al 12: "))
  if x in range(13):
    x = [i*x for i in range(1, 13)]
  else:
    x = x, "no es una opcion dentro del rango permitido"
  print(x)

def reto3_2():
    filas = int(input("Ingrese el número de filas: "))
    x = 0
    while x <= filas:
        print("*" * x)
        x += 1
def reto3_3():
  x = int(input("Ingresu un valor: "))
  x = [i for i in range(1, x*2+1, 2)]
  print(x)

def reto3_4():
  while(True):
    x = int(input("Ingrese numero par: "))
    if x%2!=0:
      break

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
    print("6. Reto - Juego y comparto")
    print("7. Reto - Desafio mi lógica")
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
            os.system("clear")
            print("Elegiste RETOS")
            print("INVENTO MIS REGLAS")
            print("Clase 3 - Silabuz\n")
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
        elif opcion == '6':
            os.system("clear")
            print("Elegiste RETOS")
            print("JUEGO Y COMPARTO")
            print("Clase 4 - Silabuz\n")
            print("Elije un ejercicio:")
            print("1. Reto 1")
            print("2. Reto 2")
            print("3. Reto 3")
            print("\nby Tutankadev\n")
            reto = input("Ingresa el numero de ejercicio: ")
            if reto == '1':
              reto2_1()
              break
            elif reto == '2':
              reto2_2()
              break
            elif reto == '3':
              reto2_3()
              break
            else:
              print("Elija una opción válida")
              run()
              break
        elif opcion == '7':
            os.system("clear")
            print("Elegiste RETOS")
            print("DESAFIO MI LÓGICA")
            print("Clase 5 - Silabuz\n")
            print("Elije un ejercicio:")
            print("1. Reto 1")
            print("2. Reto 2")
            print("3. Reto 3")
            print("4. Reto 4")
            print("\nby Tutankadev\n")
            reto = input("Ingresa el numero de ejercicio: ")
            if reto == '1':
              reto3_1()
              break
            elif reto == '2':
              reto3_2()
              break
            elif reto == '3':
              reto3_3()
              break
            elif reto == '4':
              reto3_4()
              break
            else:
              print("Elija una opción válida")
              run()
              break
        else:
            print("Elija una opción válida")
            run()
            break

if __name__ == '__main__':
  run()