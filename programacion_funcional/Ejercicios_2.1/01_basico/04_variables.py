from os import system
if system ("clear") !=0: system("cls")

#Para asignar el nombre de la variable solo hace falta poner el nombre de la variables y asignarla
my_name ="Alejandra"
print(my_name)#imprime el valor de la variable my_name

age = 22
print(age)#imprime le valor de la variable age

#No es necesario seclarar explicitamente el tipo de variable
name = "Alejandra"
print(type(name)#Muestra el tipo de dato de la variable name (str)
      
name = 32
print(type(name)#Ahora la variable tiene un numero entero (int)
 #Tipado fuerte:Python no realiza conversiones de tipo automaticas

 #f-string (literal de candea de formato)
 print(f"Hola {my_name}, tengo{age + 5} años")

 #No recomendada forma de asignar variables 
 name, age, city = "Alejandra", 22, "FCP"

 #Conversion de nombres de variables
 mi_nombre_de_variable = "ok" #snake_case
 nombre = "ok"

 miNombreDeVariable = "no-recomendado"#camelcase
 MiNombreDeVariable = "no-recomendado"#PascalCase
minombredevariable = "no-recomendado"#Todo junto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14#upper_case-->constante

is_user_logged_in: bool = True
print(is_user_logged_in)

name:str = "Alejandra"
print(name)

