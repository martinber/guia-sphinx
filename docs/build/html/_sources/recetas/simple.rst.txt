Receta simple
=============

La documentación va a consistir de una sola página, primero va a haber una
descripción del proyecto y luego la documentación generada a partir de cada
módulo.

Esta es la forma recomendada de configurar Sphinx cuando el proyecto consiste en
menos de 3 módulos.

Generar la configuración
------------------------

Ir a la carpeta del proyecto y ejecutar ``sphinx-quickstart``.

::

  cd batch_ffmpeg
  sphinx-quickstart

Va a ir preguntando algunas opciones, usar:

* Root path for documentation: docs/
* Separate source and build directories: y

También pregunta si se desean activar unas extensiones, activar: 

* intersphinx
* todo
* viewcode
* githubpages (si se va a usar *GitHub*)

Al final pregunta si se busca crear *makefiles*, responder sí a ambos.

Configurar
----------

Se configura en ``conf.py``.

* Importar ``os``, ``sys`` y agregar carpeta al *PATH*.
* Agregar la extension ``napoleon``.
* ``todo_include_todos = True``.

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

  Mi modulo1
  ----------

  .. automodule:: miproyecto.modulo1
     :members:
     :private-members:

  Mi modulo2
  ----------

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

Generar
-------

Moverse a la carpeta de la documentación y hacer ``make html``::

  cd miproyecto/docs
  make html
