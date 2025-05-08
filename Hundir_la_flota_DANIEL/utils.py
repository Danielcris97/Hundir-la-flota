import numpy as np
import variables as vr

turno_jugador = np.random.random_integers(0, 1)
def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero


def colocar_barcos(tablero, barcos):
    for  i in barcos:
        for j in i:
            tablero[j[0], j[1]] = "O" 
    return tablero

def disparo(tablero, tablero2):
    fila = int(input("selecciona la fila 0-9 "))
    columna = int(input("selecciona la columna 0-9 "))
    o_count1 = np.count_nonzero(tablero == "O")
    if fila < 0 or columna < 0:
        print("error intenta otra vez")
        disparo(tablero,tablero2)
    if fila > 9 or columna > 9:
        print("error intenta otra vez")
        disparo(tablero,tablero2)
    if tablero[fila,columna] =="O":
        tablero[fila,columna] = "X"
        tablero2[fila,columna] = "X"
        print("¡¡¡IMPACTOOOOO!!!")
        o_count = np.count_nonzero(tablero == "O")
        if o_count == o_count1 - 1:
            disparo(tablero,tablero2)
    elif tablero[fila,columna] == "#" or tablero[fila, columna] == "X":
        print("Posiccion ya seleccionada")
        disparo(tablero,tablero2)    
    else:
        tablero[fila,columna] = "#"
        tablero2[fila,columna] = "#"
        print("FALLASTE :)")
    return tablero
def disparo_rival(tablero,tablero2):
    fila = np.random.random_integers(0, 9)
    columna = np.random.random_integers(0, 9)
    o_count1 = np.count_nonzero(tablero == "O")
    if tablero[fila,columna] =="O":
        tablero[fila,columna] = "X"
        tablero2[fila,columna] = "X"
        o_count = np.count_nonzero(tablero == "O")
        print("¡¡¡IMPACTOOOOO DEL RIVAL!!!")
        if o_count == o_count1 - 1:
            disparo_rival(tablero,tablero2)  
    elif tablero[fila,columna] == "#" or tablero[fila, columna] == "X":
        print("Posiccion ya seleccionada por el rival")
        disparo_rival(tablero,tablero2)
    else:
        tablero[fila,columna] = "#"
        tablero2[fila,columna] = "#"
        print("FALLO DEL RIVAL :)")
    return tablero

def turno_inicial():
    if turno_jugador == 1:
        disparo(tablero_rival_barcos,tablero_jugador_disparos)
    if turno_jugador == 0:
        disparo_rival(tablero_jugador_barcos, tablero_rival_disparos)



