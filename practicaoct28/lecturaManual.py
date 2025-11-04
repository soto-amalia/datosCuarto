# leer_por_cadenas.py
def extraer_entre(texto, apertura, cierre):
    start = texto.find(apertura)
    if start == -1:
        return '', texto
    start += len(apertura)
    end = texto.find(cierre, start)
    if end == -1:
        return texto[start:], texto[end:]  # o cadena vacía
    return texto[start:end].strip(), texto[end + len(cierre):]

try:
    with open('archivo.xml', 'r', encoding='utf-8') as f:
        contenido = f.read()

    lista_albumes = []
    # separar por <CD> ... </CD>
    partes = contenido.split('<CD>')
    for parte in partes[1:]:  # el primer elemento antes del primer <CD> no sirve
        cd_block = parte.split('</CD>')[0]

        titulo, _ = extraer_entre(cd_block, '<TITLE>', '</TITLE>')
        artista, _ = extraer_entre(cd_block, '<ARTIST>', '</ARTIST>')
        pais, _ = extraer_entre(cd_block, '<COUNTRY>', '</COUNTRY>')
        year, _ = extraer_entre(cd_block, '<YEAR>', '</YEAR>')
        #falta comapnia y precio
        lista_albumes.append([titulo, artista, pais, year]) # append mete elementos al final de un list

        print(f"Título: {titulo}")
        print(f"Artista: {artista}")
        print(f"País: {pais}")
        print(f"Año: {year}")
        print("-" * 20)

    print("\nEstructura lista_albumes:")
    print(lista_albumes)

    

except FileNotFoundError:
    print("No se encontró 'archivo.xml'.")
except Exception as e:
    print("Error:", e)
