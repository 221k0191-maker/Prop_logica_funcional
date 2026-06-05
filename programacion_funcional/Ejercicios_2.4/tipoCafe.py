#Ejercicio 2: Ordenar tipo de café 
#Objetivo : Ordenar distintos tipos de cafe 

def preparar_cafe_americano():
   return "cafe americano"

def preparar_cafe_olla():
   return "cafe olla"
   
def ordenar_cafe(prepara_cafe, numero_tazas):
   tazas_cafe = [prepara_cafe() for _ in range(numero_tazas)]
   return tazas_cafe

cafe_grupo_a = ordenar_cafe(preparar_cafe_americano,10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_olla, 12)

print (cafe_grupo_a, cafe_grupo_b)
