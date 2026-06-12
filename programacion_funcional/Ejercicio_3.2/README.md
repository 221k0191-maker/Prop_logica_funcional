# Sistema Experto Vocacional — TecNM
### Motor de Inferencia: Prolog · Controlador: Python (Funcional)

---

## Descripción

Sistema experto que recomienda la carrera más adecuada para estudiantes de nuevo ingreso del Tecnológico Nacional de México Campus Felipe Carrillo Puerto. Combina:

- **Paradigma lógico** (SWI-Prolog) como motor de inferencia con base de conocimientos y reglas de ponderación.
- **Paradigma funcional** (Python) como controlador, usando `map`, `filter`, `reduce`.

### Carreras evaluadas

| # | Carrera |
|---|---------|
| 1 | Ingeniería en Sistemas Computacionales |
| 2 | Ingeniería en Ciencia de Datos e IA |
| 3 | Ingeniería en Administración |
| 4 | Ingeniería Industrial |
| 5 | Ingeniería en Industrias Alimentarias |
| 6 | Ingeniería en Desarrollo Comunitario |
| 7 | Ingeniería en Gestión Empresarial |

---

## Archivos del proyecto

```
sistema_experto_vocacional/
├── carreras.pl           # Base de conocimientos + motor de inferencia (Prolog)
├── index.py              # Controlador interactivo (Python funcional)
├── requirements.txt      # Dependencias Python
└── README.md             # Este archivo
```

---

## Requisitos

**1. SWI-Prolog**

**2. Python 3.8 o superior**

**3. (Opcional) Crear entorno virtual**


## Instalación

1. Clona o descarga el repositorio:
```bash
git clone <url-del-repo>
cd programacion-logica/Ejercicio_3.2
```

2. Asegúrate de que ambos archivos estén en el mismo directorio:
```
carreras.pl
index.py
```

---

## Ejecución

### Forma principal (recomendada)

```bash
python index.py
```

El sistema presentará un cuestionario interactivo de 24 preguntas 
Al finalizar, mostrará las carreras ordenadas por puntaje.

---

## Arquitectura del sistema

```
┌─────────────────────────────────────────────────────────┐
│                  index.py                               │
│                  (Controlador Python)                   │
│                                                         │  
│  Funciones puras   filtrar_respuestas()                 │
│  map/filter/(), calcular_...                            │
│                                                         │ │
└─────────────────────┬───────────────────────────────────┘
                      │ 
                      ▼
┌─────────────────────────────────────────────────────────┐
│                    carreras.pl                          │
│              (Motor de Inferencia Prolog)               │
│                                                         │  
│  Meta     recomendar_y_mostrar/ ──► stdout             │
└─────────────────────────────────────────────────────────┘
```

---

## Tecnologías

- **SWI-Prolog** 8.x+ — https://www.swi-prolog.org
- **Python** 3.8+ — https://www.python.org
- Sin dependencias externas (solo stdlib de Python)

---

*Desarrollado como proyecto académico — Programación lógica y funcional · TecNM*
