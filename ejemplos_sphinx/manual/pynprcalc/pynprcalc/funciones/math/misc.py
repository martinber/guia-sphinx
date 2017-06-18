"""
Funciones misceláneas.
"""


from . import const


def grados_a_radianes(x):
    """
    Convierte el ángulo dado de grados a radianes.

    Args:
        x (float): Ángulo.

    Returns:
        float: El ángulo en radianes.
    """
    return (x / 360) * 2 * const.pi()


def radianes_a_grados(x):
    """
    Convierte el ángulo dado de radianes a grados.

    Args:
        x (float): Ángulo.

    Returns:
        float: El ángulo en grados.
    """
    return (x / (2 * const.pi())) * 360
