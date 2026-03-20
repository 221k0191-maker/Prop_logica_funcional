from os import system
if system ("clear") !=0: system("cls")


#La funcion imput() recibe un mensaje que se muestra al usuario
nombre = input("Hola, ¿como te llamas?\n")
print(f"Hola{nombre}, encantada de cnocerte")

#Ten en cuenta que la funcion input() devuleve un string
#As que si queremos obtener un numero se debe convertir el string a un numero
age = input("¿Cuantos años tiene?\n")
age = int(age)
print(f("Tienes{age} años")
      
#La funcion input() tambien puede decolver multiples valores
#Para hacerlo, el usuario debe separar los valores con una coma
print("Obtener multiples valores a lo ver")
country, city = input("¿En que ciudad y pais vives=\n".split()
                      
print(f"Vives en {country}, {city})
