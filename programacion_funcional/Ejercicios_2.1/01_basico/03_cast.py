from os import system
if system ("clear") !=0: system("cls")

print("conversión de tipos")

print(int("100")+ 2) 

print(int("100" + str(2)))#convierte el numero 2 a cada y lo concatena(unir).

print(type(float("3.1416")))

#convertir un numero decimal a entero (se trunca la parte decimal)
print(int(3.1416))#elimina la parte decimal y la convierte en entero

#evaluar valores numericoz como booleanos
print(bool(3))#cualquier numero distinto a 0 es True
print(bool(0))#0 es False.
print(bool(-1))# Numeros negativos tambien son True

print(bool(""))#Una cadena vacia es False
print(bool(" "))# Una cadena con espacios es True
print(bool("False")) #Una cadena de texto

#rendodear un numero decimal 
print(round(2.51))#Redondear el decimal al numero mas cercano 
