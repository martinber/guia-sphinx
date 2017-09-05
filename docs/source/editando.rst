Cómo editar
===========

Acá explico un poco cómo hacer para editar una documentación rápidamente sin
tener que aprender mucho sobre *Sphinx*.

Instalacion
-----------

Primero hay que instalar unos programas::

  sudo apt install python3-pip
  sudo pip3 install sphinx sphinx_rtd_theme

Introducción
------------

Después hay que conseguir la carpeta del proyecto que se quiere editar, la
estructura de la carpeta es algo asi::

  .
  ├── docs
  │   ├── build
  │   │   ├── ...
  │   │   └── html
  │   │       ├── ...
  │   │       └── index.html
  │   └── source
  │       ├── ...
  │       ├── conf.py
  │       └── index.rst
  ├── ...
  └── Otras cosas...

En ``docs/`` está todo lo relacionado a la documentación, afuera de ``docs/``
puede haber cualquier cosa.

En ``docs/source/`` está lo que uno escribe, en ``docs/build/`` está la página
web generada a partir de lo que uno escribió en ``docs/source/``.

Editando
--------

Hay que editar los archivos ``.rst`` que están en la carpeta ``docs/source/``,
el formato se llama *ReStructured Text*, acá pongo links a algunos tutoriales:

- http://www.sphinx-doc.org/en/stable/rest.html

- http://docutils.sourceforge.net/docs/user/rst/quickstart.html

- La sección :ref:`sobre reStructuredText en esta guía <guia_reStructuredText>`

Estos archivos se editan en cualquier editor de texto.

Leyendo
-------

Antes de poder ver la documentación hay que generar todo lo que está dentro de
``docs/build/`` con unos comandos::

  cd docs
  make html

Para poder leer la documentación hay que abrir ``docs/build/html/index.html``.
