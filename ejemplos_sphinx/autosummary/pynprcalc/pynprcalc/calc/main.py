"""
Corazón de la caluladora.

La calculadora tiene un *stack* (que es una cola LIFO, lo último que entra es lo
primero que sale). Trabaja con *float*.

Los números se ponen en el *stack*. Los comandos sacan cero o más números del
*stack*, hacen una operación con ellos y ponen el resultado en el *stack*.

Por ejemplo al comienzo el *stack* contiene varios números, los últimos números
están abajo.

::

    5
    6
    2
    4

Al usar el comando ``+``, el se toman los últimos dos números del *stack* y se
coloca su suma::

    5
    6
    6
"""


from .. import comandos


class Stack:
    """
    Implementación de un *stack*.
    """

    def __init__(self):
        self._lista = []


    def insertar(self, n):
        """
        Insertar un número en el stack.

        Args:
            n (float): Número a insertar.
        """
        self._lista.append(n)


    def pop(self):
        """
        Sacar un número del *stack*.

        Elimina el número del *stack*.

        Returns:
            float: Número obtenido desde el *stack*.
        """
        return self._lista.pop()


    def lista(self):
        """
        Devuelve una lista que representa al *stack*.

        Para por ejemplo mostrar el *stack* en pantalla y acceder a los
        elementos sin usar ``pop()``.
        """
        return self._lista


class Calc:
    """
    Calculadora en sí.

    Tiene un *stack* y permite correr comandos sobre ese *stack*.
    """

    def __init__(self):
        self._stack = Stack()


    def insertar(self, n):
        """
        Insertar un número en el *stack* de la calculadora.

        Args:
            n (float): Número a insertar.
        """
        self._stack.insertar(n)


    def ejecutar(self, comando):
        """
        Ejecutar un comando en la calculadora.

        Si el comando es un número, lo agrega al *stack*.

        Args:
            comando (Union[str, float]): Comando a ejecutar.

        Raises:
            ValueError cuando el comando no existe.
        """

        try: # en el caso que sea un numero
            self._stack.insertar(float(comando))

        except ValueError: # en el caso que no sea un numero
            try:
                funcion, cant_args = comandos.obtener_funcion(comando)
            except ValueError: # en el caso que el comando no exista
                raise ValueError('el comando "{}" no existe'.format(comando))

            # sacar la cantidad correcta de numeros desde el *stack*
            args = []
            for i in range(cant_args):
                args.append(self._stack.pop())

            # usar esos argumentos para llamar la función y guardar el resultado
            # en el stack
            # si devuelve una lista es porque hay varios elementos a guardar
            resultado = funcion(*args)

            if resultado is None:
                return
            if type(resultado) is list:
                for n in resultado:
                    self._stack.insertar(n)
            else:
                self._stack.insertar(resultado)


    def lista(self):
        """
        Devuelve una lista que representa al *stack*.

        Para por ejemplo mostrar el *stack* en pantalla y acceder a los
        elementos sin usar ``pop()``.
        """
        return self._stack.lista()
