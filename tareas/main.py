"""""
CASO DE ESTUDIO
Vamos a crear un sistema de calificaciones automatizado para tareas o lecciones programaticas.

--Debe contar con una interfaz que permita que los tutores implementen sus tareas 
y que reporte errores en casos
donde la tarea no cumpla con las condiciones especificadas.
--Los tutores pueden crear sus tareas y deben crear el dódigo para verificar el trabajo 
de los "alumnos".
--EL tutor debe de poder identificar al alumno(e.g por nombre).
--El tutor debe de tener conocimiento sobre que tareas esta realizando cada alumno 
--EL alumno puede realizar cualquier numero de intentos antes de resolver la tarea y 
se debe tener registro del numero de intentos realizados.

"""

# main.py
# python -m mi_tutor.main
from .leccion import IntroPython, Estadistica
from .tutor import Tarea, Evaluador

if __name__ == "__main__":
    print(issubclass(IntroPython, Tarea))
    print(issubclass(Estadistica, Tarea))

def prueba():

    evaluacion26 = Evaluador() 
    id_estadistica = evaluacion26.registrar(Estadistica)
    print("ID de tarea registrada:",  id_estadistica)
    alumno = "Amalia"
    evaluacion26.iniciar_tarea(alumno,  id_estadistica)
    print("\nLección Estadistica:")
    print(evaluacion26.obtener_leccion(alumno))
    codigo_estudiante = ""
    while True:
        linea = input()
        if linea.strip() == "":
            break
        codigo_estudiante += linea + "\n"

    # Chequear código del alumno
    resultado = evaluacion26.check(alumno, codigo_estudiante)
    print("Check Estadistica:", resultado)

    # Resumen final
    print("Resumen final:", evaluacion26.resumen(alumno))


if __name__ == "__main__":
    prueba()

