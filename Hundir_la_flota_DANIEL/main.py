import utils
import variables as vr
import time
"""print("INICIANDO JUEGO...")
time.sleep(1)
print("Bienvenido al juego: Hundir la flota")
time.sleep(2)
"""

tablero_rival_barcos = utils.crear_tablero()    # MOSTRAR BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.
tablero_rival_disparos = utils.crear_tablero()  # MOSTRAR DISPAROS DEL RIVAL.

tablero_jugador_barcos = utils.crear_tablero()  # MOSTRAR BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL.
tablero_jugador_disparos = utils.crear_tablero()    # MOSTRAR DISPAROS DEL JUGADOR.

def print_tableros():
    print("TABLERO DONDE SE MUESTRAN LOS BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.")
    #time.sleep(1)#
    print(tablero_rival_barcos)
    #time.sleep(2)#
    print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL RIVAL")
    #time.sleep(1)#
    print(tablero_rival_disparos)
    print("___________________________________")
    #time.sleep(2)#
    print("TABLERO DONDE SE MUESTRA LOS BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL")  
    #time.sleep(1)#
    print(tablero_jugador_barcos)
    #time.sleep(2)#
    print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL JUGADOR.")
    #time.sleep(1)#
    print(tablero_jugador_disparos)
    #time.sleep(2)#

print_tableros()
colocar_barcos_jugador = utils.colocar_barcos(tablero_jugador_barcos, vr.barcos_jugador)
colocar_barcos_rival = utils.colocar_barcos(tablero_rival_barcos, vr.barcos_rival)

disparo_jugador = utils.disparo(tablero_rival_barcos,tablero_jugador_disparos)
disparo_rival = utils.disparo_rival(tablero_jugador_barcos, tablero_rival_disparos)
print_tableros()