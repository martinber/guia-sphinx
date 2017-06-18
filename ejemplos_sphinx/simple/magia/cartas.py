"""
Mazos y cartas.

Contiene un Mazo y una clase Carta.

.. rubric:: Tipos de mazos y cartas disponibles:

* "español": Cartas del 1 al 12 más dos comodines. Los palos son "espada",
  "oro", "basto" y "copas".

* "francés": Cartas del 2 al 10 más las A, J, Q, K y dos comodines. Los palos
  son "pica", "corazón", "trébol" y "diamantes".
"""

from typing import List, Union
import random

FIGURAS_POSIBLES = {}
"""
Figuras soportadas por Carta.

No incluye "comodín"
"""
PALOS_POSIBLES = {}
"""
Palos soportados por Carta.
"""

FIGURAS_POSIBLES["español"] = list(range(1, 12 + 1))
PALOS_POSIBLES["español"] = ["espada", "oro", "basto", "copas"]

FIGURAS_POSIBLES["francés"] = list(range(2, 10 + 1)) + ["A", "J", "Q", "K"]
PALOS_POSIBLES["francés"] = ["pica", "corazón", "trébol", "diamante"]

class Mazo:
    """
    Un mazo de cartas.

    Al crear el mazo está vacío.

    Attributes:
    """

    # pep 484
    def __init__(self):

        self.cartas = []

    def generar(self, tipo: str = "español", juego: int = 50):
        """
        Crear un mazo estándar.

        .. rubric:: Tipos y Juegos disponibles

        * "español": Cartas del 1 al 12 más dos comodines. Los palos son espada,
          oro, basto y copas.

          * 50: Todas las cartas del mazo más dos comodines.

          * 48: Todas las cartas del mazo menos los dos comodines.

          * 40: Todas las cartas del mazo menos los comodines, los 8 y los 9.

          * 36: Todas las cartas del mazo menos los comodines, los 8, los 9 y
            los 10.

        * "francés": Cartas del 2 al 10 más las A, J, Q, K y dos comodines. Los
          palos son pica, corazón, trébol y diamantes.

          * 54: Todas las cartas del mazo más dos comodines.

          * 52: Todas las cartas del mazo menos los dos comodines.

        Args:
            tipo: Tipo de mazo a utilizar. "español" o "francés".
            juego: Número de cartas a utilizar. Los posibles juegos dependen del
                tipo de mazo. Ver posibilidades abajo

        Attributes:
            cartas: Lista que contiene a las cartas del mazo, los primeros
                elementos son los que están más abajo en el mazo y los últimos
                son los que están arriba del mazo.

        """

        if tipo == "español":
            palos = PALOS_POSIBLES["español"]
            if juego == 50:
                figuras = FIGURAS_POSIBLES["español"]
                self.generar_personalizado("español", figuras, palos, 2)
            elif juego == 48:
                figuras = FIGURAS_POSIBLES["español"]
                self.generar_personalizado("español", figuras, palos, 0)
            elif juego == 40:
                figuras = range(1, 7 + 1) + [10]
                self.generar_personalizado("español", figuras, palos, 0)
            elif juego == 40:
                figuras = range(1, 7 + 1)
                self.generar_personalizado("español", figuras, palos, 0)
            else:
                raise ValueError("juego {} inválido para mazo {}"\
                        .format(juego, tipo))

        elif tipo == "francés":
            palos = PALOS_POSIBLES["francés"]
            figuras = FIGURAS_POSIBLES["francés"]
            if juego == 54:
                self.generar_personalizado("francés", figuras, palos, 2)
            elif juego == 54:
                self.generar_personalizado("francés", figuras, palos, 0)
            else:
                raise ValueError("juego {} inválido para mazo {}"\
                        .format(juego, tipo))

        else:
            raise ValueError("tipo {} inválido".format(tipo))

    def generar_personalizado(self, tipo: str, figuras: List[Union[str, int]],
            palos: List[str], cant_comodines: int) -> None:
        """
        Generar mazo a partir de las figuras (números), palos y cantidad de
        comodines.

        Args:
            tipo: Tipo de mazo a utilizar. "español" o "francés".
            figuras: Figuras a utilizar, puede ser cualquier número o cualquier
            string en el caso de tratarse de una letra. Ver abajo los
                valores aceptados.
            palos: Palos a utilizar, ver abajo los valores aceptados.
            cant_comodines: Cantidad de comodines a utilizar.

        .. rubric:: Valores aceptados

        * "español"

          * Figuras: int desde 1 al 12.

          * Palos: "espada", "oro", "basto" y "copas".

        * "francés"

          * Figuras: int desde 2 al 10, sino puede ser un str de los posibles:
            "A", "J", "Q", "K".

          * Palos: "espada", "oro", "basto" y copas".
        """

        # chequeo de valores obtenidos
        for figura in figuras:
            if figura not in FIGURAS_POSIBLES[tipo]:
                raise ValueError("figura {} inválida".format(figura))

        for palo in palos:
            if palo not in PALOS_POSIBLES[tipo]:
                raise ValueError("palo {} inválido".format(palo))

        self.cartas = []

        for palo in palos:
            for figura in figuras:
                self.cartas.append(Carta(tipo, figura, palo))

        for _ in range(cant_comodines):
            self.cartas.append(Carta(tipo, "comodín"))
                
    def __str__(self):
        """
        Las cartas se muestran en orden, comenzando por la superior.
        """
        string = ""
        for carta in reversed(self.cartas):
            string += str(carta) + "\n"

        return string

    def mezclar(self):
        """
        Mezclar las cartas.
        """

        random.shuffle(self.cartas)

    def tomar(self):
        """
        Tomar una carta del mazo.
        """

        return self.cartas.pop()

    def poner(self, e):
        """
        Poner una carta o un mazo encima de este mazo.

        Al poner un mazo se vacía al otro mazo.
        """
        if type(e) == Mazo:
            self.cartas.extend(e.cartas)
            e.vaciar()
        elif type(e) == Carta:
            self.cartas.append(e)
        else:
            raise TypeError("argumento inválido, debe ser un mazo o una carta")

    def vaciar(self):
        """
        Elimina todas las cartas del mazo.
        """
        self.cartas = []

    def cant_cartas(self):
        """
        Obtener la cantidad de cartas del mazo.
        """
        return len(self.cartas)



class Carta:
    """
    Representa a una carta.

    Attributes:
        tipo: Tipo de mazo al que pertenece, "español" o "francés".
        figura: Figura de esta carta, ver FIGURAS_POSIBLES. Además puede ser
            "comodín".
        palo: Palo al que pertenece esta carta, ver PALOS_POSIBLES. Si la figura
            es "comodín", el palo es None.

    Args:
        tipo: Tipo de mazo al que pertenece, "español" o "francés".
        figura: Figura de esta carta, ver FIGURAS_POSIBLES. Además puede ser
            "comodín".
        palo: Palo al que pertenece esta carta, ver PALOS_POSIBLES. Si la figura
            es "comodín", el palo es None.
    """

    def __init__(self, tipo, figura, palo = None):

        # chequeo de valores obtenidos
        if figura != "comodín":
            if figura not in FIGURAS_POSIBLES[tipo]:
                raise ValueError("figura {} inválida".format(figura))
            if palo not in PALOS_POSIBLES[tipo]:
                raise ValueError("palo {} inválido".format(palo))
        else:
            palo = None

        self.tipo = tipo
        self.figura = figura
        self.palo = palo

    def __str__(self):
        """
        Representación de la carta, se muestra el palo y la figura en una misma
        línea.

        Primero el palo justificado a la izquierda y luego la figura.
        """
        if self.palo is None:
            return "{}".format(self.figura)
        else:
            return "{:>2} - {}".format(self.figura, self.palo)
