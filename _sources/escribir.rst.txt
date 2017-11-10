Escribir la documentación
=========================

Se escribe en los archivos ``.rst`` ubicados en ``docs/source/``. Cada página se
escribe en un archivo separado. Cada página puede importar documentación desde
*docstrings* del código.

La documentacíon se escribe con formato `reStructuredText`_, que tiene una
sintaxis especial para describir texto en negrita, cursiva, etc. Además hay
*directivas* para insertar imagenes, tablas, referencias, etc. Por ejemplo ``..
image:: foto.jpeg``.

Lo importante, es que cada página que va a estar en la web generada viene de un
archivo ``.rst``. Originalmente estas páginas solamente muestran lo que tienen
escrito en ellas, si uno quiere incluir documentación desde *docstrings* se usan
unas *directivas* que indican qué módulos/funciones/clases mostrar.

Al final un archivo ``.rst`` se ve algo así::

  Mi Programa
  ===========

  Esta es la documentación para mi programa.

  Este programa sirve para:

  * Hacer algo
  * Hacer otra cosa
  * ...

  Documentación:
  --------------

  .. automodule:: prog.py
     :members:

``.. automodule::`` es una *directiva*, se va a reemplazar por la documentación
proveniente del módulo ``prog.py``. ``:members:`` es una opción que indica que
además de mostrar el *docstring* del módulo, se quiere mostrar la documentación
de todas las clases y funciones que tiene dentro.

Ahora convendría ver un poco como se usa `reStructuredText`_, una guía que
explica como escribir `es esta`__.

__ http://www.sphinx-doc.org/en/stable/rest.html

Para hacerlo más corto explico lo más importante acá:

.. _guia_reStructuredText:

Guía reStructuredText
---------------------

Los saltos de línea (tecla *Enter*) son ignorados. La idea es que los párrafos
están separados por una línea en blanco, los saltos de línea dentro de un
párrafo no se ven en el resultado:

+-----------------------------------+-----------------------------------+
| Lo que escribo:                   | El resultado que veo:             |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
| ::                                | Este es un párrafo.               |
|                                   |                                   |
|   Este es un                      | Este es otro párrafo.             |
|   párrafo.                        |                                   |
|                                   |                                   |
|   Este es otro párrafo.           |                                   |
|                                   |                                   |
+-----------------------------------+-----------------------------------+

Para hacer títulos hay que subrayar con algún signo de puntuación. La jerarquía
de títulos depende del orden en el que se haya utilizado por primera vez ese
estilo de subrayado. Los subrayados y su orden que recomiendo son::

  Título principal de la página
  =============================

  Título 1
  --------

  Título 2
  ~~~~~~~~

  Título 3
  ^^^^^^^^

  Título 4
  """"""""

Para distintos tipos de letra:

+-----------------------------------+-----------------------------------+
| Lo que escribo:                   | El resultado que veo:             |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
| ::                                | **negrita**, *cursiva*,           |
|                                   | ``código``.                       |
|   **negrita**, *cursiva*,         |                                   |
|   ``código``.                     |                                   |
|                                   |                                   |
+-----------------------------------+-----------------------------------+

Para hacer links hay varias formas, ya que está pongo las tres más fáciles:

+-----------------------------------+-----------------------------------+
| Lo que escribo:                   | El resultado que veo:             |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
| ::                                |   `Git <https://git-scm.com>`_    |
|                                   |                                   |
|   `Git <https://git-scm.com>`_    |   https://www.python.org/         |
|                                   |                                   |
|   https://www.python.org/         |   `Sphinx`__                      |
|                                   |                                   |
|                                   |                                   |
|   `Sphinx`__                      |   __ http://www.sphinx-doc.org    |
|                                   |                                   |
|   __ http://www.sphinx-doc.org    |                                   |
|                                   |                                   |
+-----------------------------------+-----------------------------------+

Para insertar imágenes::

  .. image:: ./imagenes/imagen.jpg

Para escribir código fuente::

  ::

    Lo que escribo acá se ve como código fuente.

La identación recomendada es dos espacios, pero puede ser mayor. Por último para
hacer listas::

  * Elemento 1

  * Elemento 2

    * Elemento 2.1

  * Elemento 3

Y lo más importante es incluir documentación desde *docstrings*, para ello::

  .. automodule: miprograma.funciones
     :members:

Eso incluye todo lo que hay en ese módulo (archivo ``.py``). Para indicar la
ruta al módulo se usa la misma sintaxis que la utilizada en *Python* para
incluir módulos::

  include miprograma.funciones

Ésta ruta es relativa a la carpeta que se haya agregado al *path* en
``conf.py``. También hay directivas ``autoclass``, ``autofunction`` para incluir
documentación de forma más individual, pero no lo veo tan útil.

Página principal
----------------

*Sphinx* crea automáticamente la página principal con el nombre dado en la
configuración, en este caso elegimos ``index.rst``. El archivo se ve así::

  .. Guia Sphinx documentation master file, created by
     sphinx-quickstart on Thu May 11 20:34:32 2017.
     You can adapt this file completely to your liking, but it should at least
     contain the root `toctree` directive.

  Welcome to Guia Sphinx's documentation!
  =======================================

  .. toctree::
     :maxdepth: 2
     :caption: Contents:

  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

Como lo indica el comentario ubicado en las primeras 4 líneas, la página
principal debe tener una tabla de contenidos (la directiva ``.. toctree::``).
Los índices que están abajo en las últimas líneas son opcionales.

En la tabla de contenidos deben especificarse las páginas que uno quiera
agregar dando el nombre de archivo sin la extensión. Por ejemplo::

  .. toctree::
     :maxdepth: 3
     :caption: Contenidos:

     introduccion
     instalacion
     escribir
     publicar
     ejemplos
     recetas/inicio
     alternativas/inicio

Todas las páginas deben ser agregadas manualmente, *Sphinx* muestra una
advertencia cuando hay paginas inaccesibles debido que no han sido agregadas a
ningún índice. Cada página puede tener su propia tabla de contenidos para así
crear un árbol jerárquico de páginas.

Los títulos y subtítulos de cada documento son incluidos automáticamente a la
tabla de contenidos.

En el caso de usar carpetas para ordenar los documentos, no sen ve reflejadas en
el árbol de contenidos. Pero sí debe especificarse la ruta relativa al documento
como se ve en la últimas dos líneas del ejemplo de arriba.

Otras páginas
-------------

Hay que acordarse de poner un título principal que será mostrado en la tabla de
contenidos. Después de eso no hay nada más que sea obligatorio escribir.

Se puede incluir una tabla de contenidos para agregar páginas que estarán debajo
de este documento en la jerarquía, en la directiva no se incluye la opción
``:caption:``. ``:maxdepth:`` es opcional::

  .. toctree::

     pagina1
     pagina2

Normalmente la directiva va justo debajo del título de la página, pero puede ir
en cualquier lado.

Páginas generadas a partir de *docstrings*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lo único que tienen de especial estas páginas es que contienen directivas
``autoclass``, ``automodule``, ``autofunction``, etc. Al generar la
documentación, *Sphinx* importa esos módulos/clases/funciones, es por ello que
en la configuración (``conf.py``) tuvimos que agregar la carpeta que contiene el
código a ``sys.path``.

La estructura de la documentación no necesariamente refleja la estructura de
carpetas que hay en el código fuente. Las directivas se pueden poner en
cualquier página. Creo que algo cómodo y fácil es crear una página por módulo.

Dentro del código fuente, la documentación de los *docstrings* debe estar
escrita en ``reStructuredText`` puro, pero es recomendable usar la extensión
*Napoleón* que ya instalamos y así escribir siguendo la convención `Google
Style`_.

APIdoc
------

`Sitio web`__

__ APIdoc

Es un programa que te ahorra el trabajo de tener que crear un ``.rst`` para cada
módulo y de poner en cada uno la directiva ``automodule``. El problema es que
genera demasiadas páginas para mi gusto. Prefiero en su lugar a la extensión
*autosummary* que es más personalizable.

Autosummary
-----------

Es una extensión que viene incluida en `Sphinx`_ pero debe ser activada en
``conf.py`` al igual que las demás extensiones. Por lo tanto hay que acordarse
de agregarla a la lista de extensiones::

  extensions = ['sphinx.ext.autodoc',
          'sphinx.ext.intersphinx',
          'sphinx.ext.todo',
          'sphinx.ext.mathjax',
          'sphinx.ext.napoleon',
          'sphinx.ext.autosummary', # agregar
          'sphinx.ext.viewcode']

De paso, también en ``conf.py`` hay que agregar (no importa dónde)::

  autosummary_generate = True

Esta extensión te ahorra el trabajo de tener que crear un ``.rst`` para cada
módulo y de poner en cada uno la directiva ``automodule``. Necesita que por
medio de la directiva ``autosummary`` uno le dé una lista de
módulos/clases/funciones a incluir, a partir de esa lista y de unas plantillas,
*autosummary* va a crear un ``.rst`` para cada elemento.

Entonces, la forma más fácil de trabajar es tener solamente ``index.rst`` y
ningún archivo más. En ``index.rst`` se coloca la directiva ``autosummary`` con
la lista de módulos. Al construir la documentación con ``make html``,
*autosummary* va a generar una carpeta llamada ``docs/source/_autosummary`` que
contendrá a un ``.rst`` para cada módulo.

El único problema es que la plantilla que viene por defecto no muestra mucha
información, no queda otra que cambiarla. Entonces lo último que queda es crear
un archivo ``docs/source/_templates/autosummary/module.rst`` y dentro poner lo
que va a estar en la página de cada módulo.

Yo hice una plantilla que creo que está bastante bien::

  {{ fullname }}
  {{ underline }}

  .. currentmodule:: {{ fullname }}

  {% block functions %}
  {% if functions %}
  .. rubric:: Functions

  .. autosummary::
  {% for item in functions %}
    {{ item }}
  {%- endfor %}
  {% endif %}
  {% endblock %}

  {% block classes %}
  {% if classes %}
  .. rubric:: Classes

  .. autosummary::
  {% for item in classes %}
    {{ item }}
  {%- endfor %}
  {% endif %}
  {% endblock %}

  {% block exceptions %}
  {% if exceptions %}
  .. rubric:: Exceptions

  .. autosummary::
  {% for item in exceptions %}
    {{ item }}
  {%- endfor %}
  {% endif %}
  {% endblock %}

  .. automodule:: {{ fullname }}
     :members:
     :private-members:

.. note::

  Al hacer ``make html`` se genera un ``.rst`` para cada módulo en
  ``docs/source/_autosummary`` pero no se actualizan los ya existentes en el
  caso de por ejemplo cambiar la plantilla. Entonces a veces hace falta borrar
  la carpeta ``docs/source/_autosummary`` para que se vean reflejados todos los
  cambios.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _APIdoc: http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Repositorio: https://github.com/martinber/guia-sphinx
.. _Google Style: http://www.sphinx-doc.org/en/stable/ext/example_google.html
.. _NumPy Style: http://www.sphinx-doc.org/en/stable/ext/example_numpy.html
