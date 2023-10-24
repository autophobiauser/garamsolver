# Definir las dimensiones de la matriz
filas = 9
columnas = 7

# Inicializar la matriz con ceros
garam = [[0] * columnas for _ in range(filas)]

# Leer los datos del archivo
with open("garam.txt", "r") as archivo:
    for fila, linea in enumerate(archivo):
        if fila >= filas:
            break
        valores = linea.split()
        for columna, valor in enumerate(valores):
            if columna >= columnas:
                break
            garam[fila][columna] = (valor)

with open("operaciones.txt", "r") as archivoO:
    for i in range (20):
        operadores[i] = archivo0.read()


# Imprimir la matriz
for fila in garam:
    print(fila)

# Función que valida si el número n es una solución válida para la casilla en la fila y columna
def valido(garam, n, fila, columna):


# BackTracking:
def resolver(garam):
    for i in range (9):
        for j in range(7):
            if garam[i][j] == 'X':
                for n in range(1,10):
                    #se prueba meter n
                    if valido(garam, n, i, j):
                        garam[i][j] = n
                        if resolver(garam):
                            return True
                        else:
                            garam[i][j] = 0
                return False
    return True

resolver(garam)