# leccion.py
# Importar la clase base Tarea desde el paquete
from .tutor import Tarea

"EN LA TERMINAL python -m tareas.leccion  Y DESPUES  python -m tareas.main"
#si el tutor dice voy a dejar la terea de algebra , la idea es que la tarea cumpla ciertas condiciones para saber si esta bien o no 
#alumno -- esta contenido en tareas 
"""class IntroPython(Tarea):
    def leccion(self):
        return f"Hola {self.alumno}, define las siguientes 2 variables llamadas a y b, 1. un entero igual a 1 y 2. un string con la palabra 'hola'"

    def check(self, codigo):
        return codigo == "a=1\nb='hola'"
"""
class IntroPython:
    def leccion(self):
        return f"Hola {self.alumno}, define dos variables, un entero igual a 1 y un stringcon la palabra 'hola'"
    def cheek(self, codigo):
        return codigo=="a=1 \n b='hola'"
    

class Estadistica(Tarea):
    def leccion(self): #leccion es las instruciones para el alumno
        return f"Hola {self.alumno}. Calcula el promedio de [1,2,4,8] y asígnalo a la variable 'arg'"

    def check(self, codigo): #en check vamos a correr el codigo del alumno y compararlo contra el nuestro
        import statistics
        media_esperada = statistics.mean([1, 2, 4, 8])# nos da el resultado correcto

        c = "import statistics\n" + codigo #es el codigo que se va a correr dentor de python
        localv = {}
        globalv = {} #es como una cajita dentro de python
        try:
            exec(c, globalv, localv)#ejecutas el codigo
        except Exception:
            return False
        valor_arg = localv.get("arg")

        return valor_arg == media_esperada