"""
Ejemplos para documentar en Sphinx.

Acá se documenta al archivo (script o módulo).
"""

def contar_palabras(texto):
    """
    Cuenta la cantidad de palabras que tiene un texto.

    Args:
        texto: Texto de entrada.

    Returns:
        La cantidad de palabras que tiene el texto.
    """
    return len(texto.split(sep=" "))

def buscar_palabra(texto, palabra, numero):
    """
    Cuenta la cantidad de veces que aparece una palabra en un texto.

    Esta función también documenta el tipo de las variables (str, int, float).
    Es opcional hacerlo.

    Args:
        texto (str): String en donde hay que buscar la palabra.
        palabra (str): Palabra a buscar.

    Returns:
        int: Un entero que representa a la cantidad de veces que aparece la
        palabra en el texto.
    """
    return texto.split(sep=" ").count(palabra)
