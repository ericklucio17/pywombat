matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 100],
]

columna1 = matriz[0][0] + matriz[1][0] + matriz[2][0]
columna2 = matriz[0][1] + matriz[1][1] + matriz[2][1]
columna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]

fila1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
fila2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
fila3 = matriz[2][0] + matriz[2][1] + matriz[2][2]

esquinas = matriz[0][0] + matriz[0][2] + matriz[2][0] + matriz[2][2]

print('La suma de las columnas es:', columna1, '-', columna2, '-', columna3)
print('La suma de las filas es:', fila1, '-', fila2, '-', fila3)
print('La suma de las esquinas es:', esquinas)