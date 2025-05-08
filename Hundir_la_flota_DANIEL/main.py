import utils
import variables as vr

tablero_rival_barcos = utils.crear_tablero()    # MOSTRAR BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.
tablero_rival_disparos = utils.crear_tablero()  # MOSTRAR DISPAROS DEL RIVAL.

tablero_jugador_barcos = utils.crear_tablero()  # MOSTRAR BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL.
tablero_jugador_disparos = utils.crear_tablero()    # MOSTRAR DISPAROS DEL JUGADOR.

def print_tableros():
    print("TABLERO DONDE SE MUESTRAN LOS BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.")
    print(tablero_rival_barcos)
    print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL RIVAL")
    print(tablero_rival_disparos)
    print("___________________________________")
    print("TABLERO DONDE SE MUESTRA LOS BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL")  
    print(tablero_jugador_barcos)
    print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DEL JUGADOR.")
    print(tablero_jugador_disparos)

print_tableros()

colocar_barcos_jugador = utils.colocar_barcos(tablero_jugador_barcos, vr.barcos_jugador)
colocar_barcos_rival = utils.colocar_barcos(tablero_rival_barcos, vr.barcos_rival)

disparo_jugador = utils.disparo(tablero_rival_barcos)
disparo_rival = utils.disparo_rival(tablero_jugador_barcos)
print_tableros()