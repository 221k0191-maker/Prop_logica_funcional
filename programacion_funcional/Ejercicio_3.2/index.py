from pyswip import Prolog
from datetime import datetime

#### CONEXIÓN CON PROLOG

prolog = Prolog()
prolog.consult("carreras.pl")


#### CUESTIONARIO

print("    SISTEMA EXPERTO DE ORIENTACION VOCACIONAL")
print("       Instituto Tecnologico Superior de FCP")
print("       Motor: Prolog  │  Controlador: Python")
print("\nBienvenido(a)")
nombre = input("Ingresa tu nombre completo: ").strip()

print(f"\nHola {nombre}, responde el siguiente cuestionario con si (s) o no (n).\n")

preguntas = {
    "programacion": "¿Te gusta programar? (s/n): ",
    "matematicas": "¿Te gustan las matemáticas? (s/n): ",
    "tecnologia": "¿Te interesa la tecnología? (s/n): ",
    "resolucion_problemas": "¿Disfrutas resolver problemas? (s/n): ",
    "logica": "¿Te gusta el razonamiento lógico? (s/n): ",

    "estadistica": "¿Te gusta la estadística? (s/n): ",
    "analisis_datos": "¿Te interesa analizar datos? (s/n): ",
    "investigacion": "¿Te gusta investigar? (s/n): ",

    "liderazgo": "¿Te consideras líder? (s/n): ",
    "organizacion": "¿Eres organizado? (s/n): ",
    "negocios": "¿Te gustan los negocios? (s/n): ",
    "comunicacion": "¿Te gusta comunicar ideas? (s/n): ",
    "gestion": "¿Te interesa administrar recursos? (s/n): ",

    "optimizacion": "¿Te gusta mejorar procesos? (s/n): ",
    "procesos": "¿Te interesa el funcionamiento de procesos? (s/n): ",
    "analisis": "¿Te gusta analizar situaciones y buscar soluciones? (s/n): ",

    "quimica": "¿Te gusta la química? (s/n): ",
    "biologia": "¿Te gusta la biología? (s/n): ",
    "calidad": "¿Te interesa el control de calidad? (s/n): ",

    "servicio_social": "¿Te gusta ayudar a las comunidades? (s/n): ",
    "trabajo_equipo": "¿Te gusta trabajar en equipo? (s/n): ",
    "gestion_social": "¿Te interesa el desarrollo social? (s/n): ",

    "innovacion": "¿Te gusta innovar? (s/n): ",
    "emprendimiento": "¿Te gustaría emprender un negocio? (s/n): "
}


#### CAPTURA DE RESPUESTAS (MAP + INMUTABILIDAD)

respuestas = tuple(
    map(
        lambda item: item[0]
        if input(item[1]).strip().lower() == "s"
        else None,
        preguntas.items()
    )
)

#### FILTRADO (FILTER)

perfil = list(
    filter(
        lambda x: x is not None,
        respuestas
    )
)


#### CONSULTA A PROLOG

perfil_prolog = "[" + ",".join(perfil) + "]"

consulta = f"recomendar({perfil_prolog}, Carrera, Puntaje)"

resultados = list(prolog.query(consulta))



#### MOSTRAR RESULTADOS

if resultados:

    mejor = max(
        resultados,
        key=lambda x: x["Puntaje"]
    )

    nombres = {
        "sistemas": "Ingeniería en Sistemas Computacionales",
        "ciencia_datos": "Ingeniería en Ciencia de Datos",
        "administracion": "Ingeniería en Administración",
        "industrial": "Ingeniería Industrial",
        "alimentarias": "Ingeniería en Industrias Alimentarias",
        "desarrollo_comunitario": "Ingeniería en Desarrollo Comunitario",
        "gestion_empresarial": "Ingeniería en Gestión Empresarial"
    }

    print("\n" + "=" * 50)
    print(f"RESULTADOS DE: {nombre.upper()}")
    print("=" * 50)

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"\nFecha y hora de evaluación: {fecha}")

    print(
        f"\nCarrera recomendada: "
        f"{nombres.get(str(mejor['Carrera']), str(mejor['Carrera']))}"
    )

    print(f"Puntaje obtenido: {mejor['Puntaje']} coincidencias")

    print("\nRanking completo:")

    ranking = sorted(
        resultados,
        key=lambda x: x["Puntaje"],
        reverse=True
    )

    for r in ranking:
        carrera = str(r["Carrera"])

        print(
            f"- {nombres.get(carrera, carrera)}: "
            f"{r['Puntaje']} puntos"
        )

else:
    print("No fue posible generar una recomendación.")

