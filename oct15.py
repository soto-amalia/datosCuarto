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

tareas/
#paquete
__init__.py
#en main vamos a probar las clases 
main.py
print(issubclass(IntroPython,Tarea))
print(issubclass(Estadistica,Tarea))
leccion.py
"""
#tutor.py
import abc
from abc import ABC, abstractmethod

#si el tutor dice voy a dejar la terea de algebra , la idea es que la tarea cumpla ciertas condiciones para saber si esta bien o no 
#alumno -- esta contenido en tareas 
#leccion.py
class IntroPython:
    def leccion(self):
        return f"Hola {self.alumno}, define dos variables, un entero igual a 1 y un stringcon la palabra 'hola'"
    def cheek(self, codigo):
        return codigo=="a=1\n b='hola'"
#leccion.py
class Estadistica(Tarea):
    def leccion(selft):
        return f"Hola {selft.alumno}.Calcula el promedio de [1,2,4,8] y asignalos a la variable 'arg'"
    def check(self, codigo):#verifica lo que sea que haga el alumno de acuerdo a las especificaciones que se les de  
        import statistics
        c="import statistics\n"+ codigo
        localv={}
        globalv={}
        exec(c, globalv, localv)#va a retornar la variable del alumno 'arg' 
        return localv.get("arg")==1
        statistics.mean([1,2,4,8])
#tutor.py


#clase abstracta 
class Tarea(metaclass=abc.ABCMeta):#import abc
    @abstractmethod
    def leccion(self, alumno):
        pass
    @abstractmethod
    def cheek(self, codigo):
        pass
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Tarea:
            att=set(dir(C))
            if set(cls.__abstractmethods__)<=att:
                return True
        raise NotImplemented

#main.py
print(issubclass(IntroPython,Tarea))
print(issubclass(Estadistica,Tarea))
""""Viernes 17 de Occtubre 2025
"""
#tutor.py 
class Evaluador:
    def __init__(self, alumno, ClaseTarea):
        self.tarea=ClaseTarea()
        self.tarea.alumno=alumno
        self.intentos=0
        self.correctos=0 
    def leccion(self):
        return self.tarea.leccion()       
    def check(self, codigo):
        self.intentos+=1
        res=self.tarea.check(codigo)
        if res:
            self.correctos+=1
        return res

#tutor.py
import uuid
class Evaluador: 
    def __init__(self):
        self.alumnos={}
        self.tareas={}
    def regristar(self, clase_tarea):
        if not issubclass(clase_tarea,Tarea):
            raise RuntimeError("La clase tiene una estructura incorrecta")
        id=uuid.uuid4()
        self.tareas[id]=clase_tarea
        return id 
#Diseño lo mas excalable posible

#tutor.py
    def iniciar_tarea(self, alumno, id):
        self.alumnos[alumno].EvaluadorTarea(alumno, self.tareas[id])
    def obtener_leccion(self,alumno):
        leccion=self.alumnos[alumno]
        return leccion.leccion()
    def check(self,alumno, codigo):
        leccion=self.alumnos[alumno]
        return leccion.check(codigo)
    def resumen(self, alumno):
        tarea=self.alumnos[alumno]
        return f"Avance de {alumno} en la tarea {tarea.tarea, __class__.__name__}, Intentos :{tarea.intentos}, Correctos : {tarea.correctos}, Aprobado? {tarea.correectos>0} "
    
    
    

#agregar clase y metodos y metodo para identificar que lo que dio el alumno sea correcto, agregarlo al main y probarlo y hacer el diagrama de lases 
#agregar 2 clases a las tareas y crear el codigo de prueba de 


