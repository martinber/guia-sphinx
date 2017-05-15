Instalación y configuración
===========================

Yo uso las configuraciones que me parecen más comunes y fáciles de usar. Al
final queda algo muy parecido a esta documentación.

Como estructura de archivos, me parece que lo mejor es::

  .
  ├── docs
  │   ├── build
  │   │   ├── ...
  │   │   └── html
  │   │       ├── ...
  │   │       └── index.html
  │   ├── Makefile
  │   └── source
  │       ├── ...
  │       ├── conf.py
  │       └── index.rst
  ├── LICENSE.txt
  ├── README.md
  └── src
      ├── ...
      └── main.py

En ``docs`` va toda la documentación, dentro hay un ``Makefile`` y las carpetas
``source`` y ``build``.

``source`` tiene la documentación escrita en `reStructuredText`_ y un archivo
``conf.py`` con las configuraciones usadas por `Sphinx`_.  Dentro de ``build``
está la misma documentación ya generada por `Sphinx`_. Por último el
``Makefile`` permite generar la documentación con un solo comando.

Después en otra carpeta aparte, ``src`` está el código. ``LICENSE.txt`` y
``README.md`` se suelen agregar para presentar el proyecto en `GitHub`_.

Instalación
-----------

Hay que instalar `Sphinx`_ y algún tema si hace falta. El tema que más me gusta
es el del proyecto `Read The Docs`_.

::
  pip3 install sphinx sphinx_rtd_theme

Generar configuraciones
-----------------------

Para generar la base de las configuraciones, carpetas, etc. hay un comando que
va preguntando las opciones más generales y al final genera lo necesario para
tener algo funcionando.

::
  mkdir docs
  cd docs
  sphinx-quickstart

En el proceso hace varias preguntas y muestra el valor por defecto entre
corchetes:

* ``Root path for the documentation [.]``: En nuestro caso es ``docs``, como ya
  hicimos ``cd`` a la carpeta, el valor por defecto está bien.

* ``Separate source and build directories (y/n) [n]``: Determina si separar
  ``source`` y ``build`` o si se desea dejar los ``.rst`` sueltos y solamente
  crear una carpeta ``_build``. En este caso usamos ``y``.

* ``Name prefix for templates and static dir [_]``: Prefijo a usar para carpetas
  especiales, el valor por defecto está bien.

* ``Project name``.

* ``Author name``.

* ``Project version []``: Versión actual del proyecto, por ejemplo ``1.0``.

* ``Project release []``: Versión menor del proyecto, por ejemplo ``1.0.4``.

* ``Project language [en]``: Idioma de la documentación, por ejemplo ``es``.

* ``Source file suffix [.rst]``: Extensión de los archivos de documentación,
  ``.rst`` está bien.

* ``Name of your master document (without suffix) [index]``: Nombre de archivo
  de la página principal de la documentación. El valor por defecto está bien.

* ``Do you want to use the epub builder (y/n) [n]``: Si se desea generar
  documentación en formato *epub*. No es necesario.

* ``autodoc: automatically insert docstrings from modules (y/n) [n]``: Si se
  desea generar documentación a partir de los *docstrings* del código fuente.
  Usar `y`.

Luego pregunta si se desean habilitar varias extensiones para *Sphinx*, no hace
falta ninguna de esas.

* ``Create Makefile? (y/n) [y]``: Si se desea crear un ``Makefile`` para
  simplificar la generación de la documentación en Linux. Elegir ``y``.

* ``Create Makefile? (y/n) [y]``: Si se desea crear un ``make.bat`` para
  simplificar la generación de la documentación en Windows. Elegir ``y``.

Todas estas opciones pueden ser cambiadas en el archivo ``conf.py`` que está en
``docs/source``.

Generar documentación
---------------------

Significa correr *Sphinx* para generar un sitio web a partir de los archivos
``.rst`` presentes en ``docs/source`` y a partir de los *docstrings* que están
en el código fuente.

Gracias al ``Makefile``, lo único que hay que hacer es::

  cd docs/
  make html

Para ver la documentación generada abrir ``docs/build/html/index.html`` en el
navegador.

A veces es necesario eliminar los archivos generados y volver a generar la
documentación desde cero para que se actualicen los índices::

  cd docs/
  make clean
  make html

Configuración
-------------

Toda la configuración se escribe en ``docs/source/conf.py``.




.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _Read The Docs: https://readthedocs.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _GitHub: https://github.com/
