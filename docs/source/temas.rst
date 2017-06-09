Temas
=====

El tema que viene por defecto con *Sphinx* no me parece el mejor. Vienen
incluidos varios temas que se eligen al modificar la variable ``html_theme``.

Los temas que vienen incluidos se pueden ver en `esta página`__. Yo recomiendo
el tema ``nature``.

__ http://www.sphinx-doc.org/en/stable/theming.html

Todavía mejor es el tema ``sphinx_rtd_theme``, pero éste debe ser instalado
aparte::

  pip3 install sphinx_rtd_theme.

Tabla de contenidos en sidebar
------------------------------

Uno puede personalizar todavía más la salida de *Sphinx* cambiando algunas
opciones, algo útil para hacer es agregar la tabla de contenidos completa al
*sidebar*. Esto se hace poneindo en cualquier lado::

  html_sidebars = { '**': ['globaltoc.html', 'relations.html',
          'sourcelink.html', 'searchbox.html'], }
