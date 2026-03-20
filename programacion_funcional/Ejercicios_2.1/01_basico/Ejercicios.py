from os import system
if system ("clear") !=0: system("cls")

## ejercicio 1
print("\Ejercico 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en lineas separadas.")

print("Alejandra")
print("Felipe Carrillo Puerto")

### Complete aqui 

print("------------------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")

a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

### Completa aquí

print("------------------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

num_str = "12345"
num_int = int(num_str)
num_float = float(num_int)

print(num_int)
print(num_float)

decimal = 3.99
entero = int(decimal)

print(entero)  # Eliminamos la parte decimal y nos quedaria 3


### Completa aquí
print("-------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# ¡Hola! Me llamo tu_nombre y tengo tu_edad años, mido tu_altura metros

nombre = "Alejandra"
edad = 22
altura = 1.60

print(f"¡Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")


### Completa aquí

print("-------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14159         
redondeado = round(pi)  # lo redondeamos al decimal mas cerca 
resultado = redondeado // 2  

print(resultado)