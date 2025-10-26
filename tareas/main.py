# main.py
# python -m tareas.main
from .leccion import IntroPython, Estadistica, Algebra
from .tutor import Tarea, Evaluador

if __name__ == "__main__":
    print(issubclass(IntroPython, Tarea))
    print(issubclass(Estadistica, Tarea))
    print(issubclass(Algebra, Tarea))

def prueba():

    evaluacion = Evaluador() 

    alumno = "Amalia"

    # Registrar tareas
    id_intro = evaluacion.registrar(IntroPython)
    id_estadistica = evaluacion.registrar(Estadistica)
    id_algebra = evaluacion.registrar(Algebra)

    print("ID tarea IntroPython:", id_intro)
    print("ID tarea Estadistica:", id_estadistica)
    print("ID tarea Algebra:", id_algebra)

    # Lista de todas las tareas a evaluar
    tareas = [
        (id_intro, "IntroPython"),
        (id_estadistica, "Estadistica"),
        (id_algebra, "Algebra")
    ]

    for tarea_id, nombre in tareas:
        print(f"\n--- Lección {nombre} ---")
        evaluacion.iniciar_tarea(alumno, tarea_id)
        print(evaluacion.obtener_leccion(alumno))

        # Leer código del alumno
        codigo_estudiante = ""
        while True:
            linea = input("Ingresa tu código (Enter vacío para terminar): ")
            if linea.strip() == "":
                break
            codigo_estudiante += linea + "\n"

        # Chequear código
        resultado = evaluacion.check(alumno, codigo_estudiante)
        print(f"Check {nombre}:", resultado)

    # Resumen final de la última tarea (por ahora)
    print("\nResumen final:", evaluacion.resumen(alumno))

if __name__ == "__main__":
    prueba()
