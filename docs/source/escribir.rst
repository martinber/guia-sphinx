Escribir la documentación
=========================

Se escribe en los archivos ``.rst`` ubicados en ``docs/source/``. Cada página se
escribe en un archivo separado. Cada página puede importar documentación desde
*docstrings* del código.

Uno puede crear los ``.rst`` manualmente o sino es posible generarlos a partir
del código fuente utilizando un programa llamado `APIdoc`_, el problema es que
*APIdoc* genera demasiadas páginas, conviene crear los ``.rst`` y manualmente
especificar dónde queremos insertar la documentación que proviene de los
*docstrings*.

Acá explico como crear las páginas manualmente. La documentacíon se escribe con
formato `reStructuredText`_, que tiene una sintaxis especial para describir
texto en negrita, cursiva, etc. Además hay *directivas* para insertar imagenes,
tablas, referencias, etc. Por ejemplo ``.. image:: foto.jpeg``.

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

Como lo indica el comentario, la página principal debe tener una tabla de
contenidos (la directiva ``.. toctree::``). Los índices que están abajo son
opcionales, el único que me parece útil de los tres es el de búsqueda
(``search``) pero si usamos el tema *Read the Docs* no es necesario porque ya
hay un campo de búsqueda en la barra lateral.

En la tabla de contenidos deben especificarse las páginas que uno quiera
agregar dando el nombre de archivo sin la extensión. Por ejemplo::

  .. toctree::
     :maxdepth: 3
     :caption: Contenidos:

     instalacion
     escribir
     publicar
     ejemplos
     src/miproyecto

Todas las páginas deben ser agregadas manualmente, *Sphinx* muestra una
advertencia cuando hay paginas inaccesibles debido que no han sido agregadas a
ningún índice. Cada página puede tener su propia tabla de contenidos para así
crear un árbol jerárquico de páginas.

Los títulos y subtítulos de cada documento son incluidos automáticamente a la
tabla de contenidos.

En el caso de usar carpetas para ordenar los documentos, no sen ve reflejadas en
el árbol de contenidos. Pero sí debe especificarse la ruta relativa al documento
como se ve en la última línea del ejemplo de arriba.

Otras páginas
-------------

Las páginas tienen un título principal que será mostrado en la tabla de
contenidos.

En `reStructuredText`_ los títulos se indican con subrayados, la jerarquía de
subrayados es el orden en el cual fueron definidos en el archivo. El orden más
común (el usado por la documentación de *Sphinx*) es::

  Título de página
  ================

  Título 1
  --------

  Título 2
  ~~~~~~~~

  Título 3
  ^^^^^^^^

  Título 4
  """"""""

Se puede incluir una tabla de contenidos para agregar páginas que estarán debajo
de este documento en la jerarquía, en la directiva no se incluye la opción
``:caption:``, ``:maxdepth:`` es opcional::

  .. toctree::

     pagina1
     pagina2

Normalmente la directiva va justo debajo del título de la página.

Para un tutorial de *reStructuredText* se puede ver `el que ofrece la
documentación de Sphinx <http://www.sphinx-doc.org/en/stable/rest.html>`_.

También se puede ver el `código fuente de esta guía como ejemplo`__.

__ Repositorio_

Páginas generadas a partir de *docstrings*
------------------------------------------

Lo único que tienen de especial estas páginas es que contienen directivas
``autoclass``, ``automodule``, ``autofunction``, etc. Al generar la
documentación, *Sphinx* importa esos módulos, es por ello que en la
configuración (``conf.py``) tuvimos que agregar la carpeta que contiene el
código a ``sys.path``.

La estructura de la documentación no necesariamente refleja la estructura de
paquetes que hay en el código fuente. Las directivas se pueden poner en
cualquier página. Creo que algo cómodo y fácil es crear una página por módulo o
por clase.

Dentro del código fuente, la documentación de los *docstrings* debe estar
escrita en ``reStructuredText`` puro, pero es recomendable usar la extensión
*Napoleón* que ya instalamos y así escribir siguendo la convención `Google
Style`_ o `NumPy Style`_.

.. _APIdoc: http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Repositorio: https://github.com/martinber/guia-sphinx
.. _Google Style: http://www.sphinx-doc.org/en/stable/ext/example_google.html
.. _NumPy Style: http://www.sphinx-doc.org/en/stable/ext/example_numpy.html
