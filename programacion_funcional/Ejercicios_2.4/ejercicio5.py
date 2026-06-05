# Ejercicio 4: La cuenta de la cafetería
# Objetivo: Dada una lista de precios de las órdenes de la cafetería y deberás aplicar varias funciones de orden superior (mapa, filtrar, reducir) para calcular el total a pagar.
# Usa map(): Aplicar el 10% de descuento a cada precio
# ----------------------------------------------------------------
# map() aplica una función a un elemento CADA de una lista.
# Aquí la usarás para calcular el precio con descuento de cada bebida.
# 1.- Usa map() con una lambda para multiplicar cada precio por 0.90
#     (que equivale a quitarle el 10%).
#     Estructura: mapa(lambda precio: precio * 0.90, orden)
# 2.- Convierte el resultado en lista con list() y guárdalo en
#     la variable precios_con_descuento.
# 3.- Imprime precios_con_descuento.
# Filtro habitual(): Filtrar solo las bebidas caras (más de $25)
# ----------------------------------------------------------------
# filter() recorre una lista y se queda SOLO con los elementos
# que cumple una condición (cuando la lambda devuelve True).
# 4.- Usa filter() con una lambda para quedarte solo con los precios
#     de precios_con_descuento que sean mayores a 25.
#     Estructura: filter(lambda precio: precio > 25, precios_con_descuento)
# 5.- Convierte el resultado en lista con list() y guárdalo en
#     la variable bebidas_caras.
# 6.- Imprime bebidas_caras.
# Usa reduce(): Calcular el total a pagar
# ----------------------------------------------------------------
# reduce() combina todos los elementos de una lista en UN solo valor,
# aplicando la misma operación de izquierda a derecha.
# Para usarla primero hay que importarla:
#     from functools import reduce
# 7.- Importa reducir desde functools.
# 8.- Usa reduce() con una lambda que suma dos valores (acumulador + precio)
#     sobre la lista bebidas_caras.
#     Estructura: reducir(lambda acumulada, precio: acumulado + precio, bebidas_caras)
# 9.- Guarda el resultado en la variable total y luego imprímelo
#     con formato de 2 decimales.
from functools import reduce

orden = [25.50, 22.00, 35.75, 40.00, 18.50]

print("=== Lista original de precios ===")
print(orden)

precios_con_descuento = list(map(lambda p: round(p * 0.90, 2), orden))
print("\n=== Precios con 10% de descuento ===")
print(precios_con_descuento)

bebidas_caras = list(filter(lambda p: p > 25, precios_con_descuento))
print("\n=== Bebidas caras (más de $25 después del descuento) ===")
print(bebidas_caras)

total = reduce(lambda acumulado, precio: acumulado + precio, bebidas_caras)
print(f"\n=== Total a pagar ===")
print(f"${total:.2f}")

