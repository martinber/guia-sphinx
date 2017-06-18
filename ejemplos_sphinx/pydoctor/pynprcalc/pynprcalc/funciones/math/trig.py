"""
Funciones trigonométricas.
"""


import math


def sen(x):
    """
    El seno de un número.

    El ángulo debe estar expresado en radianes.

    .. math::

        \sin(x)

    Args:
        x (float): Argumento.

    Returns:
        El seno.
    """
    return math.sin(x)


def cos(x):
    """
    El coseno de un número.

    El ángulo debe estar expresado en radianes.

    .. math::

        \cos(x)

    Args:
        x (float): Argumento.

    Returns:
        El coseno.
    """
    return math.cos(x)


def tg(x):
    """
    La tangente de un número.

    El ángulo debe estar expresado en radianes.

    .. math::

        \\tg(x)

    Args:
        x (float): Argumento.

    Returns:
        La tangente.
    """
    return math.tan(x)


def asen(x):
    """
    El arcoseno de un número.

    El resultado está expresado en radianes.

    .. math::

        \\arcsin(x)

    Args:
        x (float): Argumento.

    Returns:
        El ángulo expresado en radianes.
    """
    return math.asin(x)


def acos(x):
    """
    El arcocoseno de un número.

    El resultado está expresado en radianes.

    .. math::

        \\arccos(x)

    Args:
        x (float): Argumento.

    Returns:
        El ángulo expresado en radianes.
    """
    return math.acos(x)


def atg(x):
    """
    La arcotangente de un número.

    El resultado está expresado en radianes.

    .. math::

        \\arctan(x)

    Args:
        x (float): Argumento.

    Returns:
        El ángulo expresado en radianes.
    """
    return math.atan(x)
