import numpy as np
import variables as vr
def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero


# barco_1 = [[0,3], [0,4], [0,5], [0,6]]
# barco_jugador = [[[0,3], [0,4], [0,5], [0,6]], [[4,7], [5,7], [6,7]], [[8,8], [8,9]], [[1,7]]]

def colocar_barcos(tablero, barcos):
    for  i in barcos:
        for j in i:
            tablero[j[0], j[1]] = "O"
        
    return tablero

def disparo(tablero):
    fila = int(input("selecciona la fila"))
    columna = int(input("selecciona la columna"))
    if tablero[fila,columna] =="O":
        tablero[fila,columna] = "X"
        print("¡¡¡IMPACTOOOOO!!!")
    elif tablero[fila,columna] == "#" or tablero[fila, columna] == "X":
        print("Posiccion ya seleccionada")
        disparo()
    else:
        tablero[fila,columna] = "#"
        print("FALLASTE :)")
    return tablero
def disparo_rival(tablero):
    fila = np.random.random_integers(0, 10)
    columna = np.random.random_integers(0, 10)
    if tablero[fila,columna] =="O":
        tablero[fila,columna] = "X"
        print("¡¡¡IMPACTOOOOO DEL RIVAL!!!")
    elif tablero[fila,columna] == "#" or tablero[fila, columna] == "X":
        print("Posiccion ya seleccionada rival")
        disparo()
    else:
        tablero[fila,columna] = "#"
        print("FALLO DEL RIVAL :)")
    return tablero

    