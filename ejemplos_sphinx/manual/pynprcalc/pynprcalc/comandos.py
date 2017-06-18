"""
Interfaz entre los comandos de la calculadora y las funciones matemáticas.

Por ejemplo, la función ``X SIN`` se corresponde a ``math.trig.sen(x)``.
"""


import inspect

from .funciones import math
from .funciones import misc


comandos = {
        "+": math.basico.suma,
        "-": math.basico.resta,
        "*": math.basico.producto,
        "/": math.basico.division,
        "²": math.basico.cuadrado,
        "^": math.basico.potencia,
        "SQRT": math.basico.raiz_cuadrada,
        "ROOT": math.basico.raiz,
        "\\": math.basico.inverso,
        "_": math.basico.opuesto,

        "PI": math.const.pi,
        "E": math.const.e,

        "EXP": math.exp.exp,
        "LN": math.exp.ln,
        "LOG10": math.exp.log10,
        "LOG": math.exp.log,

        "DTOR": math.misc.grados_a_radianes,
        "RTOD": math.misc.radianes_a_grados,

        "SIN": math.trig.sen,
        "COS": math.trig.cos,
        "TAN": math.trig.tg,
        "ASIN": math.trig.asen,
        "ACOS": math.trig.acos,
        "ATAN": math.trig.atg,

        "DUP": misc.duplicar,
        "SWAP": misc.intercambiar,
        "DEL": misc.borrar
    }
"""
Mapeo de comandos con su función correspondiente.
"""


def obtener_funcion(comando):
    """
    Obtener la función matemática que se corresponde con el comando dado.

    Args:
        comando (str): El nombre del comando, debe ser en mayúsculas.

    Returns:
        Tuple[Callable, int]: Función matemática y número de argumentos que
            necesita en un tuple.

    Raises:
        ValueError si no existe el comando especificado.
    """

    try:
        funcion = comandos[comando]
    except KeyError:
        raise ValueError("el comando {} no existe".format(comando))

    firma = inspect.signature(funcion)
    cant_args = len(firma.parameters)

    return funcion, cant_args
