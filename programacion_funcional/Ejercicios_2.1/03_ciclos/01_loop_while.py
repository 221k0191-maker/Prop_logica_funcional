from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while:")

#bucle con una simple condicion 
contador = 0

while contador <=5:
    print (contador)
    contador += 1 #es super importante para evitar un bucle infinito

#utilizando la palabra break, para romper el bucle
print("\n Bucle while con while:")
contador = 0

while True: 
    print(contador)
    contador +=1 
    if contador == 5:
        break #sale del bucle

#continue,que lo hace es saltar esa iteracion en concreto
#y continuar con el bucle 
print("\n Bucle con continue:")
contador = 0
while contador < 10:
    contador +=1

    if contador % 2 == 0:
        continue
    print(contador)

#else, esta condicion cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

    #pedirle al usuario un numero que tiene
    #que ser positivo si no, no le dejamos en paz
    numero = -1
    while numero < 0:
        numero = int(input("Escribe un numero positivo: "))
        if numero < 0:
           print("El numero debe ser positivo. Intenta otra vez")

    print("El número que has introduciodo es {número}")

    numero = -1
    while numero < 0:
        try:
            numero = int(input("Escribe un numero positivo"))
            if numero< 0:
                print("El numero debe ser positivo. Intenta otra vez")
        except:
            print("Lo que introduces deve ser un numero!")

    print(f"El número que has introduciodo es {numero}")

