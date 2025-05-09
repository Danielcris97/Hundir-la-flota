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

def disparo(tablero, tablero2): #tablero 2 es el tablero de disparos
    fila = int(input("selecciona la fila 0-9 "))
    columna = int(input("selecciona la columna 0-9 "))
    o_count1 = np.count_nonzero(tablero == "O") #contar los barcos antes de disparar

    if fila < 0 or columna < 0 or fila > 9 or columna > 9:
        print("error intenta otra vez") #condición para verificar si los valores están entre 0 y 9
        return disparo(tablero, tablero2)

    if tablero[fila, columna] == "O": #si hay una O coloca una X de impacto
        tablero[fila, columna] = "X"
        tablero2[fila, columna] = "X"
        print("¡¡¡IMPACTOOOOO!!!")
        o_count = np.count_nonzero(tablero == "O")

        if o_count > 0 and o_count == o_count1 - 1:
            return disparo(tablero, tablero2)  # solo repite si aún hay barcos

    elif tablero[fila, columna] in ["#", "X"]:
        print("Posiccion ya seleccionada")
        return disparo(tablero, tablero2)

    else:
        tablero[fila, columna] = "#"
        tablero2[fila, columna] = "#"
        print("FALLASTE :)")

    return tablero


def disparo_rival(tablero, tablero2):
    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 10)
    o_count1 = np.count_nonzero(tablero == "O")

    if tablero[fila, columna] == "O":
        tablero[fila, columna] = "X"
        tablero2[fila, columna] = "X"
        o_count = np.count_nonzero(tablero == "O")
        print("¡¡¡IMPACTOOOOO DEL RIVAL!!!")

        if o_count > 0 and o_count == o_count1 - 1:
            return disparo_rival(tablero, tablero2)

    elif tablero[fila, columna] in ["#", "X"]:
        print("Posiccion ya seleccionada por el rival")
        return disparo_rival(tablero, tablero2)

    else:
        tablero[fila, columna] = "#"
        tablero2[fila, columna] = "#"
        print("FALLO DEL RIVAL :)")

    return tablero





