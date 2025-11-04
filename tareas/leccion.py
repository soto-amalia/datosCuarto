from .tutor import Tarea

# -------------------------- Tareas concretas

class IntroPython(Tarea):
    def leccion(self):
        return f"Hola {self.alumno}, define 2 variables: a es un entero igual a 1 y b un string con la palabra 'hola'"

    def check(self, codigo):
        # Limpiamos espacios y saltos de línea
        codigo_limpio = "".join(codigo.split())
        codigo_esperado = "a=1b='hola'"
        return codigo_limpio == codigo_esperado


class Estadistica(Tarea):
    def leccion(self):
        return f"Hola {self.alumno}. Calcula el promedio de [1,2,4,8] y asígnalo a la variable 'arg'"

    def check(self, codigo):
        import statistics
        media_esperada = statistics.mean([1, 2, 4, 8])
        c = "import statistics\n" + codigo
        localv = {}
        globalv = {}
        try:
            exec(c, globalv, localv)
        except Exception:
            return False
        valor_arg = localv.get("arg")
        return valor_arg == media_esperada


class Algebra(Tarea):
    def leccion(self):
        return f"Hola {self.alumno}, resuelve la ecuación 3*x - 6 = 0 y asigna el resultado a la variable 'x'"

    def check(self, codigo):
        localv = {}
        globalv = {}
        try:
            exec(codigo, globalv, localv)
        except Exception:
            return False
        return localv.get("x") == 2

class Geometria(Tarea):
    def leccion(self):
        return (f"Hola {self.alumno}, calcula el área de un triángulo.\n"
                "Asigna el resultado a la variable 'area'.\n"
                "Usa base=5 y altura=3 y la fórmula: area = (base * altura) / 2")

    def check(self, codigo):
        localv = {}
        globalv = {}
        try:
            exec(codigo, globalv, localv)
        except Exception:
            return False
        # El área correcta es (5*3)/2 = 7.5
        return localv.get("area") == 7.5
