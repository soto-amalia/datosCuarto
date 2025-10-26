# tutor.py
import abc #clases abtractas ABC, son clases padres que no puedes crear instancias solo de los hijos
from abc import ABC, abstractmethod
import uuid # identificador unico ejemplo id:2dbh28743gbcg3t4f67
#si el tutor dice voy a dejar la terea de algebra , la idea es que la tarea cumpla ciertas condiciones para saber si esta bien o no 
#alumno -- esta contenido en tareas 

# Clase abstracta
class Tarea(metaclass=abc.ABCMeta):
    @abstractmethod
    def leccion(self):
        pass

    @abstractmethod
    def check(self, codigo):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Tarea:
            att = set(dir(C))
            if set(cls.__abstractmethods__) <= att:
                return True
        # devolver NotImplemented cuando no aplica (en lugar de lanzar)
        return NotImplemented


# Gestor de tareas 
class Evaluador:
    def __init__(self):
        self.alumnos = {}  # mapa alumno -> instancia de tarea
        self.tareas = {}   # mapa tarea_id -> clase de tarea

    def registrar(self, clase_tarea):
        if not issubclass(clase_tarea, Tarea):
            raise RuntimeError("La clase tiene una estructura incorrecta")
        tarea_id = uuid.uuid4()
        self.tareas[tarea_id] = clase_tarea
        return tarea_id

    def iniciar_tarea(self, alumno, tarea_id):
        # crea la instancia de la tarea, le asigna el nombre del alumno
        ClaseTarea = self.tareas[tarea_id]
        instancia = ClaseTarea()
        instancia.alumno = alumno
        # guarda la instancia de la tarea directamente (sin wrapper de estado)
        self.alumnos[alumno] = instancia

    def obtener_leccion(self, alumno):
        tarea_inst = self.alumnos[alumno]
        return tarea_inst.leccion()

    def check(self, alumno, codigo):
        tarea_inst = self.alumnos[alumno]
        return tarea_inst.check(codigo)

    def resumen(self, alumno):
        tarea_inst = self.alumnos.get(alumno)
        if tarea_inst is None:
            return f"No hay tarea iniciada para {alumno}"
        return (f"Avance de {alumno} en la tarea de {tarea_inst.__class__.__name__}")



#agregar clase y metodos y metodo para identificar que lo que dio el alumno sea correcto, agregarlo al main y probarlo y hacer el diagrama de clases 
#agregar 2 clases a las tareas y crear el codigo de prueba de 