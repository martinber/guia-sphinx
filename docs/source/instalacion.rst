Instalación y configuración
===========================

Yo uso las configuraciones que me parecen más comunes y fáciles de usar. Pero
hay muchas cosas que también se pueden hacer distinto.

La estructura de archivos que vamos a usar es:

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
  └── miproyecto
      ├── ...
      └── main.py

__ http://docs.python-guide.org/en/latest/writing/structure/

Instalación
-----------

Hay que instalar `Sphinx`_. Se usa ``pip`` que es algo así como un ``apt-get``
para los programas escritos en *Python*.

::

  sudo apt install python3-pip
  pip3 install sphinx sphinx_rtd_theme

.. note::

  Nunca supe bien si para usar ``pip`` se necesita ``sudo``.

Generar configuraciones
-----------------------

Para generar la base de las configuraciones, carpetas, etc. hay un comando que
va preguntando las opciones más generales y al final genera lo necesario para
tener algo funcionando.

::

  sphinx-quickstart

En el proceso hace varias preguntas y muestra el valor por defecto entre
corchetes:

* ``Root path for the documentation [.]``: En nuestro caso vamos a usar
  ``docs``.

* ``Separate source and build directories (y/n) [n]``: Determina la estructura
  de carpetas que se va a usar, nosotros usamos ``y`` para tener una carpeta
  llamada ``build`` y una llamada ``source``.

* ``Name prefix for templates and static dir [_]``: Prefijo a usar para carpetas
  especiales y de *Sphinx*, el valor por defecto está bien.

* ``Project name``.

* ``Author name``.

* ``Project version []``: Versión actual del proyecto, por ejemplo ``1.0``.
  Opcional.

* ``Project release []``: Versión menor del proyecto, por ejemplo ``1.0.4``.
  Opcional.

* ``Project language [en]``: Idioma de la documentación, usamos ``es``.

* ``Source file suffix [.rst]``: Extensión de los archivos de documentación, el
  valor por defecto ``.rst`` está bien.

* ``Name of your master document (without suffix) [index]``: Nombre de archivo
  de la página principal de la documentación. El valor por defecto está bien.

* ``Do you want to use the epub builder (y/n) [n]``: Si se desea generar
  documentación en formato *epub*. No es necesario.

* ``autodoc: automatically insert docstrings from modules (y/n) [n]``: Si se
  desea generar documentación a partir de los *docstrings* del código fuente.
  Usar ``y``.

Luego pregunta si se desean habilitar varias extensiones para *Sphinx*.
Recomiendo instalar: ``autodoc``, ``intersphinx``, ``todo``, ``mathjax`` y
``viewcode``.

* ``Create Makefile? (y/n) [y]``: Si se desea crear un ``Makefile`` para
  simplificar la generación de la documentación en Linux. Elegir ``y``.

* ``Create Windows command file? (y/n) [y]``: Si se desea crear un ``make.bat``
  para simplificar la generación de la documentación en Windows. Elegir ``y``.

Todas estas opciones pueden ser cambiadas luego en el archivo ``conf.py`` que
está en ``docs/source``.

Generar documentación
---------------------

Significa correr *Sphinx* para generar un sitio web a partir de los archivos
``.rst`` presentes en ``docs/source`` y a partir de los *docstrings* que están
en el código fuente. Cada vez que hagamos alguna modificación hay que
actualizar la documentación con este comando.

Gracias al ``Makefile``, lo único que hay que hacer es::

  cd docs/
  make html

Para ver la documentación generada abrir ``docs/build/html/index.html`` en el
navegador.

Por ahora la documentación va a estar bastante vacía porque no escribimos nada.

.. note::

  A veces es necesario eliminar los archivos generados y volver a generar la
  documentación desde cero para que se actualicen los índices::

    cd docs/
    make clean
    make html

Configuración
-------------

Toda la configuración se escribe en ``docs/source/conf.py``.

Importar lo necesario
~~~~~~~~~~~~~~~~~~~~~

Hay que importar el código fuente para poder analizar sus *docstrings* y a
partir de ahí generar parte de la documentación. Como el código fuente está en
otra carpeta hay que agregarla al *path* de *Python*::

  import os
  import sys

  sys.path.insert(0, os.path.abspath('../../'))

El *path* a usar depende de la estructura de archivos usada. Debe ser relativo a
la ubicación de ``conf.py``.

Cargar las extensiones
~~~~~~~~~~~~~~~~~~~~~~

A partir de lo que se haya elegido en la configuración inicial, ya hay
extensiones que están siendo cargadas. Las que vamos a usar son estas, no viene
mal tener extensiones de más:

* **autodoc**: Genera la documentación a partir de los *docstrings* del código
  fuente. Es la más importante!.

* **intersphinx**: Permite hacer links entre documentaciones, puede ser útil.

* **todo**: Agrega herramientas para llevar la cuenta de los "ToDo" (cosas por
  hacer).

* **mathjax**: Permite agregar fórmulas matemáticas escritas en *LaTeX*.

* **viewcode**: Permite ver el código fuente desde la documentación, es muy
  cómodo.

* **napoleon**: Permite escribir los *docstrings* con la convención *NumPy* o
  *Google*. Esto hace la documentación en el código fuente más legible que la
  que la posible por defecto. **Esta debe ser agregada manualmente**. También
  es importante!

* **autosummary**: Genera automáticamente archivos ``.rst`` para automatizar
  todavía más el trabajo que hace **autodoc**. Usarla o no depende de qué
  control se quiera tener sobre el resultado final, después explico bien que
  hace. **Agregarla solamente si se la quiere usar**.

Entonces en ``conf.py``::

  extensions = ['sphinx.ext.autodoc',
          'sphinx.ext.intersphinx',
          'sphinx.ext.todo',
          'sphinx.ext.mathjax',
          'sphinx.ext.napoleon',
          'sphinx.ext.autosummary', # solamente si se la quiere usar
          'sphinx.ext.viewcode']

Otras configuraciones
~~~~~~~~~~~~~~~~~~~~~

Hay una línea que se puede agregar para que en la barra lateral aparezca una
tabla de contenidos, yo recomiendo agregarla siempre (en cualquier lugar de
``conf.py``)::

  html_sidebars = { '**': ['globaltoc.html', 'relations.html',
          'sourcelink.html', 'searchbox.html'], }

Por último se puede :doc:`cambiar el tema <./temas>`.

Lo que queda ahora es `escribir la documentación <./escribir>`.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _Read the Docs: https://readthedocs.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _GitHub: https://github.com/
