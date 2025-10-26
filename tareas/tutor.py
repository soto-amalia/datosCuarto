#--------------------------# tutor.py
"""
Este archivo contiene la clase base abstracta Tarea y la clase Evaluador.
- Tarea: define la interfaz para cualquier tarea, con métodos abstractos leccion() y check().
- Evaluador: gestiona alumnos, tareas registradas, intentos, corrección y resumen de progreso.
"""

import abc
from abc import ABC, abstractmethod
import uuid


#-------------------------- Clase abstracta para tareas

class Tarea(metaclass=abc.ABCMeta):
    @abstractmethod
    def leccion(self):
        """Devuelve las instrucciones de la tarea para el alumno"""
        pass

    @abstractmethod
    def check(self, codigo):
        """Recibe el código del alumno y devuelve True si es correcto, False si no"""
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Tarea:
            att = set(dir(C))
            if set(cls.__abstractmethods__) <= att:
                return True
        raise NotImplemented


# 
#--------------------------Evaluador de tareas
# 
class Evaluador:
    """
    Gestiona alumnos y tareas.
    Permite registrar clases de tarea, iniciar tareas para alumnos,
    revisar código entregado y mostrar resumen de progreso.
    """

    def __init__(self):
        self.alumnos = {}  # alumno -> instancia de tarea
        self.tareas = {}   # tarea_id -> clase de tarea

    def registrar(self, clase_tarea):
        """Registra una clase de tarea y devuelve un id único"""
        if not issubclass(clase_tarea, Tarea):
            raise RuntimeError("La clase tiene una estructura incorrecta")
        tarea_id = uuid.uuid4()
        self.tareas[tarea_id] = clase_tarea
        return tarea_id

    def iniciar_tarea(self, alumno, tarea_id):
        """Inicia la tarea para un alumno"""
        ClaseTarea = self.tareas[tarea_id]
        instancia = ClaseTarea()
        instancia.alumno = alumno
        # Inicializar contadores de intentos y correctos en la instancia
        instancia.intentos = 0
        instancia.correctos = 0
        self.alumnos[alumno] = instancia

    def obtener_leccion(self, alumno):
        """Devuelve la lección/instrucciones de la tarea actual del alumno"""
        tarea_inst = self.alumnos[alumno]
        return tarea_inst.leccion()

    def check(self, alumno, codigo):
        """Evalúa el código entregado por el alumno y actualiza intentos y correctos"""
        tarea_inst = self.alumnos[alumno]
        tarea_inst.intentos += 1
        res = tarea_inst.check(codigo)
        if res:
            tarea_inst.correctos += 1
        return res

    def resumen(self, alumno):
        """Devuelve un resumen del progreso del alumno en su tarea actual"""
        tarea_inst = self.alumnos.get(alumno)
        if tarea_inst is None:
            return f"No hay tarea iniciada para {alumno}"
        intentos = getattr(tarea_inst, "intentos", 0)
        correctos = getattr(tarea_inst, "correctos", 0)
        aprobado = correctos > 0
        return (f"Avance de {alumno} en la tarea {tarea_inst.__class__.__name__}, "
                f"Intentos: {intentos}, Correctos: {correctos}, Aprobado? {aprobado}")
