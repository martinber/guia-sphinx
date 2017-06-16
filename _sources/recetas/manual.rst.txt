Método manual
=============

.. note::

  Acá se explica cómo escribir los ``.rst`` de forma manual, antes se debe
  configurar como se indica en :doc:`la receta <./inicio>`.

La documentación va a consistir de varias páginas, uno tiene control total sobre
dónde colocar la documentación proveniente de los *docstrings*.

Los *docstrings* van a estar donde uno ponga las directivas ``.. automodule``,
esto puede ir en cualquier lado. Yo voy a usar una estructura que me parece la
mejor para proyectos grandes.

En este caso voy a documentar el programa de ejemplo *pynprcalc*.

Escribir
--------

En el ``index.rst`` va a haber una introducción al proyecto y enlaces a cada uno
de los ``.rst`` que documentan módulos o paquetes que estén en el primer nivel.

::

  Documentación de mi pynprcalc
  =============================

  .. toctree::
     :maxdepth: 2
     :caption: Contents:

     pynprcalc.comandos
     pynprcalc.calc
     pynprcalc.funciones

  Esta es una introducción a lo que hace este proyecto...

  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

.. note::

  Los nombres que estoy poniendo en el ``toctree`` no son necesariamente
  iguales a los paquetes/módulos de Python. En el ``toctree`` van los nombres
  de los archivos ``.rst`` (sin incluir la extensión), yo uso el mismo nombre
  en el ``.rst`` y en el módulo/paquete.

Ahora hay que hacer un ``.rst`` para cada paquete y cada módulo que vayamos
agregando al ``toctree``.

Al documentar los paquetes hay que agregar al ``toctree`` a cada uno de los
módulos/paquetes que pertenezcan a éste. Este es un ejemplo de cómo documentar
al paquete *funciones*, el nombre del archivo deberá ser
``pynprcalc.funiones.rst`` porque así lo especificamos en el ``toctree`` del
``index.rst``.

::

  pynprcalc.funciones
  ===================

  .. toctree::
     :maxdepth: 2
     :caption: Contents:

     pynprcalc.funciones.math
     pynprcalc.funciones.misc

.. note::

  El título del documento no necesariamente debe coincidir con el nombre de
  archivo ni con el nombre del paquete/modulo que se documenta.

Al documentar un módulo solamente hay que usar ``automodule`` para importar la
documentación desde los *docstrings* presentes en ese módulo, en este caso voy a
dar el ejemplo para el archivo ``pynprcalc.funciones.misc.rst``::

  pynprcalc.funciones.misc
  ========================

  .. automodule:: pynprcalc.funciones.misc
     :members:
     :private-members:

.. note::

  El nombre que se coloca a la derecha de ``automodule`` es el único que debe
  ser igual al nombre del módulo a documentar. Este nombre se debe escribir tal
  cual uno lo importa desde Python. Se escribe relativo al *path* que se
  escribió en ``conf.py``.

Y así se continúa para cada módulo/paquete que uno quiera. Hay que acordarse de
que cada vez que uno crea un ``.rst`` éste debe ser incluido en algún
``toctree``.
