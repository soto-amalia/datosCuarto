from libreta import Libreta, Notas

class Menu:
    # Muestra un menú de opciones para interactuar con la libreta de notas.
    def _init_(self):
        self.libreta = Libreta()
        # Inicialización de self.opciones (¡Esta es la línea clave corregida!)
        self.opciones = {
            "1": self.mostrar_notas,
            "2": self.buscar_notas,
            "3": self.agregar_nota,
            "4": self.salir
        }

    def correr(self):
        # Bucle principal para ejecutar la aplicación.
        while True:
            self.mostrar_menu()
            opcion = input("Introduce una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida. Por favor, intenta de nuevo.")

    def mostrar_menu(self):
        # Imprime las opciones disponibles del menú.
        print("""
Opciones de la Libreta:
1. Mostrar todas las notas
2. Buscar notas
3. Añadir nueva nota
4. Salir
        """)

    def mostrar_notas(self, notas=None):
        # Muestra todas las notas o un subconjunto usando el formato Contenido // Fecha.
        if not notas:
            notas = self.libreta.notas

        if not notas:
            print("No hay notas en la libreta.")
            return

        print("\n--- Listado de Notas ---")
        for i, nota in enumerate(notas, 1):
            # Formato: <Número>. <Contenido> // <Fecha>
            print(f"{i}. {nota.contenido} // {nota.fecha_creacion}")
        print("----------------------\n")


    def buscar_notas(self):
        # Solicita un filtro y llama a la función de búsqueda.
        filtro = input("Introduce el término de búsqueda: ")
        notas_encontradas = self.libreta.buscar(filtro)
        if notas_encontradas:
            print("\nNotas encontradas:")
            self.mostrar_notas(notas_encontradas)
        else:
            print("No se encontraron notas con ese término.")

    def agregar_nota(self):
        # Solicita el contenido y añade la nota a la libreta.
        contenido = input("Introduce el contenido de la nota: ")
        self.libreta.nueva_nota(contenido)

    def salir(self):
        # Termina la ejecución de la aplicación.
        print("¡Adiós! ")
        exit()

Menu().correr()