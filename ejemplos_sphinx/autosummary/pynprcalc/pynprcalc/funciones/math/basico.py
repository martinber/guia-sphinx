"""
Funciones matemáticas básicas.
"""


def suma(x, y):
    """
    Suma de dos números.

    .. math::

        x + y

    Args:
        x (float): Sumando.
        y (float): Sumando.

    Returns:
        float: La suma.
    """
    return x + y


def resta(x, y):
    """
    Resta de dos números.

    .. math::

        x - y

    Args:
        x (float): Minuendo.
        y (float): Sustraendo.

    Returns:
        float: La resta.
    """
    return x - y


def producto(x, y):
    """
    Producto de dos números.

    .. math::

        x y

    Args:
        x (float): Factor.
        y (float): Factor.

    Returns:
        float: El producto.
    """
    return x * y


def division(x, y):
    """
    La división de dos números.

    .. math::

        \\frac{x}{y}

    Args:
        x (float): Dividendo.
        y (float): Divisor.

    Returns:
        float: El cociente.
    """
    return x / y


def cuadrado(x):
    """
    El cuadrado de un número.

    .. math::

        x^2

    Args:
        x (float): Base.

    Returns:
        float: El cuadrado.
    """
    return x * x


def potencia(x, y):
    """
    Potencia de dos números.

    .. math::

        x^y

    Args:
        x (float): Base.
        y (float): Exponente.

    Returns:
        float: La potencia.
    """
    return x**y


def raiz_cuadrada(x):
    """
    La raiz cuadrada de un número.

    .. math::

        \sqrt{x}

    Args:
        x (float): Radicando.

    Returns:
        float: La raíz cuadrada.
    """
    return x**(1/2)


def raiz(x, y):
    """
    La raíz enésima de un número.

    .. math::

        \sqrt[y]{x}

    Args:
        x (float): Radicando.
        y (float): Índice.

    Returns:
        float: La raíz.
    """
    return x**(1/y)


def inverso(x):
    """
    El inverso de un número.

    .. math::

        \\frac{1}{x}

    Args:
        x (float): Número a invertir.

    Returns:
        float: El inverso.
    """
    return 1 / x


def opuesto(x):
    """
    El opuesto de un número.

    .. math::

        -x

    Args:
        x (float): Número a calcular el opuesto.

    Returns:
        float: El opuesto.
    """
    return -x
