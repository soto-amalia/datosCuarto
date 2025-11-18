def pedir_matriz(filas, columnas, nombre):
    print(f"\n--- Matriz {nombre} ({filas}x{columnas}) ---")
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    
    return matriz

def mostrar_matriz(matriz, nombre):
    """Muestra una matriz de forma ordenada"""
    print(f"\nMatriz {nombre}:")
    for fila in matriz:
        print(fila)

# Programa principal
print("=== INGRESO DE MATRICES ===")

# Pedir dimensiones
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

# Pedir las dos matrices
matriz1 = pedir_matriz(filas, columnas, "A")
matriz2 = pedir_matriz(filas, columnas, "B")

# Mostrar resultados
mostrar_matriz(matriz1, "A")
mostrar_matriz(matriz2, "B")

#hacer el ejercicios 