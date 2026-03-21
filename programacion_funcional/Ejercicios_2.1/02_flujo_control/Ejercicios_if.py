from os import system
if system ("clear") !=0: system("cls")
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print("El mayor es:", num1)
elif num2 > num1:
    print("El mayor es:", num2)
else:
    print("Ambos números son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre cero)

num1 = float(input("\nIntroduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

anio = int(input("\nIntroduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Por favor, introduce tu edad: "))

if edad >= 0 and edad <= 2:
    print("Categoría: Bebé")
elif edad >= 3 and edad <= 12:
    print("Categoría: Niño")
elif edad >= 13 and edad <= 17:
    print("Categoría: Adolescente")
elif edad >= 18 and edad <= 64:
    print("Categoría: Adulto")
elif edad >= 65:
    print("Categoría: Adulto mayor")
else:
    print("Edad no válida")
