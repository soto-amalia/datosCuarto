# main.py
from .leccion import IntroPython, Estadistica, Algebra
from .tutor import Tarea, Evaluador

def leer_codigo():
    codigo = ""
    while True:
        linea = input()
        if linea.strip() == "":
            break
        codigo += linea + "\n"
    return codigo

def prueba():
    evaluacion = Evaluador() 
    alumno = "Amalia"

    # Registrar tareas
    tareas_ids = {
        "IntroPython": evaluacion.registrar(IntroPython),
        "Estadistica": evaluacion.registrar(Estadistica),
        "Algebra": evaluacion.registrar(Algebra)
    }

    resultados = {}

    # Ejecutar cada lección
    for nombre, tarea_id in tareas_ids.items():
        evaluacion.iniciar_tarea(alumno, tarea_id)
        print(f"\nLección {nombre}")
        print(evaluacion.obtener_leccion(alumno))
        codigo = leer_codigo()
        resultados[nombre] = evaluacion.check(alumno, codigo)
        print(f"Resultado: {resultados[nombre]}")

    # Resumen y reintentos
    while True:
        total = len(resultados)
        correctas = sum(1 for r in resultados.values() if r)
        print("\nResumen:")
        for nombre, r in resultados.items():
            print(f"{nombre}: {'Aprobado' if r else 'No aprobado'}")
        print(f"{alumno} completó {correctas}/{total} lecciones correctamente ({correctas*100/total:.0f}%)")

        malas = [n for n, r in resultados.items() if not r]
        if not malas:
            break
        if input("¿Quieres reintentar lecciones malas? (si/no): ").strip().lower() != "si":
            break

        leccion = input(f"Elige lección a reintentar {malas}: ").strip()
        if leccion in malas:
            evaluacion.iniciar_tarea(alumno, tareas_ids[leccion])
            print(evaluacion.obtener_leccion(alumno))
            codigo = leer_codigo()
            resultados[leccion] = evaluacion.check(alumno, codigo)

if __name__ == "__main__":
    prueba()
