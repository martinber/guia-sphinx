Cómo editar
===========

Acá explico un poco cómo hacer para editar una documentación rápidamente.

Instalacion
-----------

Primero hay que instalar unos programas::

  sudo apt install python3-pip
  sudo pip3 install sphinx sphinx_rtd_theme

Editando
--------

Hay que editar los archivos ``.rst`` que están en la carpeta ``docs/source/``,
el formato se llama *ReStructured Text*, acá pongo links a algunos tutoriales:

- http://www.sphinx-doc.org/en/stable/rest.html

- http://docutils.sourceforge.net/docs/user/rst/quickstart.html

- La sección :ref:`sobre reStructuredText en esta guía <guia_reStructuredText>`

Leyendo
-------

Para poder leer la documentación hay que abrir ``docs/build/html/index.html``.
Si el archivo no existe o se hicieron modificaciones hay que volver a generar
los ``html`` usando los comandos::

  cd docs
  make html
