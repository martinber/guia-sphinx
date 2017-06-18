import os
import time

from cartas import Mazo, Carta

def _explicar(texto):
    """
    Limpiar la pantalla y mostrar in texto recuadrado.

    Args:
        texto (str): Texto a mostrar en pantalla.

    Examples:
        ::

            -----------------------------------------------------
            Esto es un texto recuadrado
            -----------------------------------------------------

    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------------------")
    print(texto)
    print("-----------------------------------------------------")

def _mostrar_pilas(pilas):
    """
    Imprimir cuarto pilas (mazos) en columnas.

    Args:
        pilas (magia.cartas.Mazo): Mazos a mostrar en pantalla.
    """

    # obtener cantidad máxima de lineas a imprimir
    lineas = max(pilas[0].cant_cartas(),
                 pilas[1].cant_cartas(),
                 pilas[2].cant_cartas())

    print("{:<14} {:<14} {:<14}".format("Pila 1", "Pila 2", "Pila 3"))

    for i in range(lineas):
        cartas = [] # cartas a imprimir en esta línea
        for pila in pilas:
            try:
                cartas.append(str(pila.cartas[i]))
            except IndexError:
                cartas.append("")

        print("{:<14} {:<14} {:<14}".format(cartas[0], cartas[1], cartas[2]))

def truco_de_magia():
    """
    Hace un truco de magia usando las cartas.
    """

    # mazo con todas las cartas
    mazo_completo = Mazo()
    mazo_completo.generar("español", 48)

    explicar("Conseguí un mazo")
    print(mazo_completo)

    # cartas usadas en el truco, son 20
    mazo = Mazo()

    # crear 3 pilas en donde se ponen las cartas
    pilas = []
    for _ in range(3):
        pilas.append(Mazo())

    # mezclar mazo
    mazo_completo.mezclar()
    explicar("Mezclé el mazo")
    print(mazo_completo)

    # tomar 21 cartas del mazo y ponerlas en la mano
    for i in range(21):
        mazo.poner(mazo_completo.tomar())

    explicar("Tomé 21 cartas del mazo, a las demás las descarté\n"
             "Pensá en una carta, cuando estés listo apretá Enter")
    print(mazo)
    input()

    # truco de magia en sí
    for _ in range(3):

        # poner las cartas del mazo en las pilas ordenadamente
        p = 0 # pila en donde poner la siguiente carta
        for i in range(21):
            pilas[p].poner(mazo.tomar())
            if p < 2:
                p += 1
            else:
                p = 0
            
            explicar("Estoy poniendo las cartas en pilas")
            mostrar_pilas(pilas)
            time.sleep(0.1)

        explicar("Terminé de poner las cartas en pilas\n"
                 "Decime en qué pila está tu carta, ingresa 1, 2 o 3")
        mostrar_pilas(pilas)
        pila_elegida = int(input()) - 1

        # poner las cartas en el mazo nuevamente, la pila elegida debe ir al
        # medio
        orden_pilas = [0, 1, 2] # orden en el cual poner las pilas en el mazo
        orden_pilas.remove(pila_elegida) # sacar el número de la pila elegida
        orden_pilas.insert(1, pila_elegida) # ponerlo en el segundo lugar
        for i in orden_pilas:
            mazo.poner(pilas[i])

    # obtener la carta pensada tomando la carta número 11
    for _ in range(10):
        mazo.tomar()

    carta_mágica = mazo.tomar()
    explicar("La carta que pensaste es:")
    print(carta_mágica)

    print(
"             *\n"
"       *   *\n"
"     *    \* / *\n"
"       * --.:. *\n"
"      *   * :\ -\n"
"        .*  | \\\n"
"       * *     \\\n"
"     .  *       \\\n"
"      ..        /\\.\n"
"     *          |\\)|\n"
"   .   *         \ |\n"
"  . . *           |/\\\n"
"     .* *         /  \\\n"
"   *              \\ / \\\n"
" *  .  *           \\   \\\n"
"    * .  \n"
"   *    *    \n"
"  .   *    *  \n"
        )
