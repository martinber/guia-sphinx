"""
Funciones exponenciales.

A excepción de la potencia que está junto con las funciones básicas.
"""


import math

from . import const


def exp(x):
    """
    Calcula el número :math:`e` elevado al número dado.

    .. math::

        e^x

    Args:
        x (float): Exponente.

    Returns:
        float: La potencia.
    """
    return const.e()**x


def ln(x):
    """
    Calcula el logaritmo natural (con base :math:`e`).

    .. math::

        \ln{x}

    Args:
        x (float): Argumento.

    Returns:
        float: El logaritmo.
    """
    return math.log(x)


def log10(x):
    """
    Calcula el logaritmo de base 10.

    .. math::

        \log{x}

    Args:
        x (float): Argumento.

    Returns:
        float: El logaritmo.
    """
    return math.log10(x)


def log(x, y):
    """
    Calcula el logaritmo de *x* de base *y*.

    .. math::

        \log_y{x}

    Args:
        x (float): Argumento.
        y (float): Base.

    Returns:
        float: El logaritmo.
    """
    return math.log(x, y)
