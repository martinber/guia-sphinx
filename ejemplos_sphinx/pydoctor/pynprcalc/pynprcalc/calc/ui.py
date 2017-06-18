"""
Interfaz de usuario en línea de comandos.

Utiliza *ncurses*.
"""

import curses
import curses.textpad

from . import main


def run():
    """
    Correr la interfaz.
    """

    ui = UI()


class UI:
    """
    Controla la interfaz de usuario.
    """

    def __init__(self):

        self._terminado = False # indica cuando salir del loop principal
        self._calc = main.Calc()

        # encierro en try..finally porque en el caso de error debo cerrar
        # *curses* correctamente, de lo contrario la terminal queda desacomodada
        try:
            self._terminal = _Terminal()
            self._loop()
        finally:
            self._terminal.cerrar()
            print("Hay algo mal que no anda bien")


    def _loop(self):
        """
        Loop principal del programa.
        """

        while not self._terminado:
            self._imprimir_stack()
            self._procesar_entrada()


    def _imprimir_stack(self):
        """
        Limpia la pantalla y muestra el contenido del *stack*.
        """

        self._terminal.limpiar()
        lista = self._calc.lista()
        for i, n in enumerate(lista):
            # dejar una linea en blanco y una para el cuadro de texto, dibujar
            # de arriba a abajo
            y = self._terminal.alto - 2 - len(lista) + i
            self._terminal.escribir(0, y, str(n))

        self._terminal.actualizar()


    def _procesar_entrada(self):
        """
        Permite al usuario ingresar números o comandos.

        En el caso que el comando ingresado sea inválido, vuelve a imprimir el
        *stack*, muestra un mensaje de error y espera un nuevo intento.
        """

        terminado = False
        while not terminado:
            comandos = self._terminal.leer_entrada().strip().split(" ")

            try:
                for comando in comandos:
                    self._calc.ejecutar(comando)
            except ValueError as e:
                # mostrar error arriba de la pantalla
                y = self._terminal.alto - 2
                self._imprimir_stack()
                self._terminal.escribir(0, y, str(e), curses.A_REVERSE)
                self._terminal.actualizar()
            else:
                terminado = True


class _Terminal:
    """
    Implementa el código relacionado a *curses*.

    *curses* es una librería que permite trabajar con la terminal, pero como es
    bastante engorrosa de usar, meto todo lo que necesito en esta clase.

    Implementa una ventana en donde se puede escribir texto, y la última línea
    es un cuadro de texto en donde el usuario puede escribir.

    Attributes:
        alto (int): Alto de la pantalla en líneas.
        ancho (int): Ancho de la pantalla en columnas.
    """

    def __init__(self):

        # crear pantalla
        self._stdscr = curses.initscr()

        self.alto, self.ancho = self._stdscr.getmaxyx()

        # no dejar al usuario escribir en pantalla, solamente cuando nosotros
        # queramos
        curses.noecho()

        # dejar que curses maneje teclas como *Re Pag*
        self._stdscr.keypad(True)

        # crear cuadro de texto abajo de la pantalla
        self._editwin = curses.newwin(1, self.ancho, self.alto - 1, 0)
        self._editbox = curses.textpad.Textbox(self._editwin)


    def limpiar(self):
        """
        Limpiar la pantalla.

        No limpia el cuadro de texto.
        """
        self._stdscr.clear()


    def escribir(self, x, y, texto, estilo=curses.A_NORMAL):
        """
        Escribir texto en una posición específica de la pantalla.

        Opcionalmente se puede especificar un estilo para el texto. Los estilos
        deben ser algunas de las constantes presentes en *curses*, como por
        ejemplo ``curses.A_BOLD``.
        """
        self._stdscr.addstr(y, x, texto, estilo)


    def leer_entrada(self):
        """
        Dar foco al cuadro de texto y devolver lo ingresado por el usuario.

        Da foco al cuadro de texto y bloquea hasta que el usuario haya terminado
        de escribir, luego devuelve lo ingresado y borra el cuadro de texto.
        """

        self._editbox.edit() # lee entrada y bloquea hasta que se presione Enter
        entrada = self._editbox.gather()
        self._editwin.clear()
        return entrada


    def actualizar(self):
        """
        Refresca la pantalla para que se vean reflejados los cambios.

        También refresca el cuadro de texto.
        """

        self._stdscr.refresh()
        self._editwin.refresh()


    def cerrar(self):
        """
        Cierra *curses* correctamente.

        Como *curses* cambia el comportamiento de la terminal, al cerrar hay que
        revertir los cambios sino la terminal queda medio desacomodada.
        """

        curses.nocbreak()
        self._stdscr.keypad(False)
        curses.echo()
        curses.endwin()
