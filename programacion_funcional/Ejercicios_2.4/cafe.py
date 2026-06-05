def preparar_cafe():
    return "cafe"

def ordenar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe()for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupo = ordenar_cafe(10)

print(cafe_para_grupo)

