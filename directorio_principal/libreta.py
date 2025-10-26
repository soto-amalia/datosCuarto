import datetime

class Notas:
    # Representa una nota individual con contenido y fecha de creación.
    def _init_(self, contenido):
        self.contenido = contenido
        self.fecha_creacion = str(datetime.date.today()) # Almacena la fecha de hoy como string.

    def coincide(self, filtro):
        # Verifica si el contenido de la nota contiene el filtro.
        return filtro in self.contenido

class Libreta:
    # colección de notas.
    def _init_(self):
        self.notas = []#inicializando 

    def nueva_nota(self, contenido):
        # Crea y añade una nueva nota a la libreta.
        self.notas.append(Notas(contenido))
        print("Nota añadida exitosamente.")

    def buscar(self, filtro):
        # Devuelve una lista de notas cuyo contenido coincide con el filtro.
        return [nota for nota in self.notas if nota.coincide(filtro)]

