import numpy as np

def convertir_a_array(x):
    return np.asarray(x)

def producto_punto_vectores(vector_a, vector_b): #  Producto punto entre dos vectores 1D.
   
    suma_acumulada = 0
    longitud_vector = vector_a.shape[0]  # cantidad de elementos en los vectores
    for indice_elemento in range(longitud_vector):
        suma_acumulada += vector_a[indice_elemento] * vector_b[indice_elemento]
    return suma_acumulada

def multiplicacion_matricial_clasica(matriz_a, matriz_b): 
    # obtener dimensiones 
    filas_a, columnas_a = matriz_a.shape
    filas_b, columnas_b = matriz_b.shape

    # validación sencilla de compatibilidad
    if columnas_a != filas_b:
        raise ValueError(
            f"Dimensiones incompatibles para multiplicar: "
            f"matriz A es {filas_a}x{columnas_a} y matriz B es {filas_b}x{columnas_b}."
        )
    # reservar matriz resultado de forma (filas_a x columnas_b)
    matriz_resultado = np.zeros(
        (filas_a, columnas_b),
        dtype=np.result_type(matriz_a.dtype, matriz_b.dtype)
    )

    # recorrer cada posición (fila_resultado, columna_resultado)
    for indice_fila_resultado in range(filas_a):
        for indice_columna_resultado in range(columnas_b):
            suma_parcial = 0
            # sumar productos A[fila, k] * B[k, columna]
            for indice_k in range(columnas_a):  # columnas_a == filas_b
                suma_parcial += matriz_a[indice_fila_resultado, indice_k] * matriz_b[indice_k, indice_columna_resultado]
            matriz_resultado[indice_fila_resultado, indice_columna_resultado] = suma_parcial

    return matriz_resultado
    
def producto(a, b): # funcion principal decidir si e sproducto punto o matricial
    arreglo_a = convertir_a_array(a)
    arreglo_b = convertir_a_array(b)

    if arreglo_a.ndim == 1 and arreglo_b.ndim == 1:
        return producto_punto_vectores(arreglo_a, arreglo_b)

    if arreglo_a.ndim == 2 and arreglo_b.ndim == 2:
        return multiplicacion_matricial_clasica(arreglo_a, arreglo_b)

    raise TypeError("Sólo se soportan (1D,1D) o (2D,2D).")

# --------------------------

if 0==0:
    print("Ejemplo 1:", producto([1, 2, 3], [4, 5, 6]))  # 32

    v1 = np.array([1, 2])
    v2 = np.array([3, 4])
    print("Ejemplo 2:", producto(v1, v2))               # 11

    A = [[1, 2, 3],
         [4, 5, 6]]          # 2 x 3
    B = [[7, 8],
         [9, 10],
         [11, 12]]           # 3 x 2
    print("Ejemplo 3:\n", producto(A, B))
    # [[ 58  64]
    #  [139 154]]
# Si quieres que devuelva siempre un int/float de Python en vez de un numpy.scalar, reemplaza la línea por: return suma_acumulada.item()
