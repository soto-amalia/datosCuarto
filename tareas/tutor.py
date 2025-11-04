"""
Este archivo contiene:
- Tarea: clase abstracta base para cualquier tarea.
- Evaluador: clase que gestiona alumnos, tareas registradas, intentos, corrección y resumen.
"""

import abc
from abc import ABC, abstractmethod
import uuid


# -------------------------- Clase abstracta para tareas
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


# -------------------------- Evaluador de tareas
class Evaluador:
    """
    Gestiona alumnos y tareas.
    Permite registrar clases de tarea, iniciar tareas para alumnos,
    revisar código entregado y mostrar resumen de progreso.
    """

    def __init__(self):
        self.alumnos = {}  # alumno -> {tarea_id: instancia de tarea}
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
        # Inicializar contadores
        instancia.intentos = 0
        instancia.correctos = 0

        if alumno not in self.alumnos:
            self.alumnos[alumno] = {}
        self.alumnos[alumno][tarea_id] = instancia

    def obtener_leccion(self, alumno, tarea_id):
        """Devuelve la lección/instrucciones de la tarea específica"""
        return self.alumnos[alumno][tarea_id].leccion()

    def check(self, alumno, tarea_id, codigo):
        """Evalúa el código entregado por el alumno y actualiza intentos y correctos"""
        tarea_inst = self.alumnos[alumno][tarea_id]
        tarea_inst.intentos += 1
        res = tarea_inst.check(codigo)
        if res:
            tarea_inst.correctos += 1
        return res

    def resumen(self, alumno):
        """
        Genera resumen completo de todas las tareas del alumno,
        indicando cuántas aprobó y porcentaje de éxito.
        """
        tareas_alumno = self.alumnos.get(alumno, {})
        total = len(tareas_alumno)
        correctas = 0
        detalle = []

        for tarea_id, tarea_inst in tareas_alumno.items():
            aprobado = tarea_inst.correctos > 0
            detalle.append(f"{tarea_inst.__class__.__name__}: {'Aprobado' if aprobado else 'No aprobado'}")
            if aprobado:
                correctas += 1

        porcentaje = (correctas / total * 100) if total else 0
        resumen_texto = "\n".join(detalle)
        resumen_texto += f"\n{alumno} completó {correctas}/{total} lecciones correctamente ({porcentaje:.0f}%)"
        return resumen_texto
