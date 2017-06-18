Método simple
=============

.. note::

  Acá se explica cómo escribir los ``.rst`` de forma manual, antes se debe
  configurar como se indica en :doc:`la receta <./inicio>`.

La documentación va a consistir de una sola página, primero va a haber una
descripción del proyecto y luego la documentación generada a partir de cada
módulo.

Esta es la forma recomendada de configurar Sphinx cuando el proyecto consiste en
menos de 3 módulos.

Escribir
--------

Editar ``index.rst`` y dejarlo algo así:

::

  Documentación de mi proyecto
  ============================

  .. toctree::
     :maxdepth: 2
     :caption: Contents:

  Esta es una introducción a lo que hace este proyecto...

  .. automodule:: miproyecto.modulo1
     :members:
     :private-members:

  .. automodule:: miproyecto.modulo2
     :members:
     :private-members:

  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

.. note::

  Yo escribí ``miproyecto.modulo1``. Esto debe ser el módulo a documentar tal
  cual uno lo importa desde Python. Depende de qué se haya agregado al ``path``
  en ``conf.py``.

Y listo, no hay que hacer nada más.

Continuar
---------

Ahora solamente falta :ref:`generar la documentación! <generar_receta>`.
