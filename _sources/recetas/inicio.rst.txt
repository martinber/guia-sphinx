Recetas
=======

Esta es una guía bien rápida y que no explica tanto cómo funciona *Sphinx*.
Primero hay que hacer lo que está en esta página para configurar *Sphinx* de
forma general, después los pasos finales dependen de cómo uno quiera documentar
las cosas.

Generar la configuración
------------------------

Ir a la carpeta del proyecto y ejecutar ``sphinx-quickstart``.

::

  cd batch_ffmpeg
  sphinx-quickstart

Va a ir preguntando algunas opciones, usar:

* Root path for documentation: ``docs/``.
* Separate source and build directories: ``y``.

Las demás opciones dejarlas por defecto. También pregunta el nombre del
proyecto, número de versión (opcional) y autor.

Luego pregunta las extensiones a utilizar, activar estas:

* autodoc.
* intersphinx.
* todo.
* mathjax.
* viewcode.
* githubpages (si se va a usar *GitHub*).

Al final pregunta si se busca crear *makefiles*, responder sí a ambos.

Configurar
----------

Se configura en ``docs/source/conf.py``.

* Importar ``os``, ``sys`` y agregar carpeta que contiene el código al *PATH*.
  Si estás usando la estructura de archivos que recomendé, el *path* es:
  ``'../../'``.

* Agregar la extension ``sphinx.ext.napoleon`` en la lista ``extensions``.

* En cualquier lado poner::

    html_sidebars = { '**': ['globaltoc.html', 'relations.html',
            'sourcelink.html', 'searchbox.html'], }

  Eso agrega una tabla de contenidos al *sidebar*.

* Opcionalmente :ref:`cambiar el tema <temas>`, recomiendo cambiar
  ``'alabaster'`` por ``'nature'``.

.. _tipos_receta:

Como continuar
--------------

Una vez que se hayan hecho estos pasos, ya se puede generar la documentación,
aunque todavía esté vacía.

Para poder ver lo que se haya escrito en *docstrings* antes hay que indicar
dónde está el código fuente e indicar las páginas a usar. Hay tres formas de
hacerlo:

.. toctree::

  simple
  autosummary
  manual

Antes de utilizar *autosummary* me parece que uno debe entender como funcionan
los otros dos métodos.

.. _generar_receta:

Generar
-------

Una vez que se haya utilizado uno de esos métodos, la web se genera con::

  cd miproyecto/docs
  make html
