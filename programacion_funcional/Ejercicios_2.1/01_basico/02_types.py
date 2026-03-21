from os import system
if system ("clear") !=0: system("cls")


"""
El comando `type()` devuelve el tipo de un objeto de Python
"""


print("init:")#Enteros (numeros sin parte decimal)
print(type(10))
print(type(0))#El numero 0 tambien es un numero entero
print(type(-5))#Numero entero negativo
print(type(7238424723784278934789239874))

print("float:")#Numeros decimales (de punto flotante)
print(type(3.14))
print(type(1.0))
print(type(1e3))

print("complex:")#Numeros complejos
print(type(1+2j))

print("str:") #cadenas de texto
print(type("Hola"))
print(type(""))
print(type("123"))#Aunque paresca un numero, esta entre comillas, por lo que es un texto
print(type("""
  Multilinea
"""))
           
print("bool:")#Valores booleanos (True and False)
print(type(True))
print(type(False))
print(type(1<2))

print("Nonetype:") #Representa la ausencia del valor
print(type(None)) #'None' Es un tipo espacial en python que reresenta sin valor
           