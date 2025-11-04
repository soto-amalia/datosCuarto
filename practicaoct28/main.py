# archivo: leer_a_lista_sin_safe.py
import xml.etree.ElementTree as ET

try:
    tree = ET.parse('archivo.xml')
    root = tree.getroot()

    # Lista de listas: cada sublista = [Título, Artista, País, Año]
    lista_albumes = []

    for cd in root.findall('CD'):
        # acceder directamente a los elementos; si no existe, usar cadena vacía
        titulo = cd.find('TITLE').text if cd.find('TITLE') is not None else ''
        artista = cd.find('ARTIST').text if cd.find('ARTIST') is not None else ''
        pais = cd.find('COUNTRY').text if cd.find('COUNTRY') is not None else ''
        año = cd.find('YEAR').text if cd.find('YEAR') is not None else ''

        # añadir la sublista
        lista_albumes.append([titulo, artista, pais, año])

        # impresión igual que al inicio
        print(f"Título: {titulo}")
        print(f"Artista: {artista}")
        print(f"País: {pais}")
        print(f"Año: {año}")
        print("-" * 20)

    # mostrar la estructura completa
    print("\nEstructura lista_albumes:")
    print(lista_albumes)

    print(lista_albumes[2][3])

except FileNotFoundError:
    print("No se encontró 'archivo.xml'. Pon el archivo en la misma carpeta que este script.")
except ET.ParseError as e:
    print("Error al parsear el XML:", e)
