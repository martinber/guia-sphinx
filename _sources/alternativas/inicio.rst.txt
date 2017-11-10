Alternativas
============

Antes de elegir `Sphinx`_ probé varias herramientas similares que por algunas
razones creo que son peores. De todas formas hay dos que pueden ser útiles
cuando no hay ganas de configurar *Sphinx* para ver los *docstrings*.

Las herramientas que probé son:

* Sphinx
* Doxygen
* Natural Docs
* pydoctor
* pdoc
* pydoc
* epydoc
* Docutils

De esas, `pydoctor`_ y `pydoc`_, que permiten generar unas páginas ``html`` a
partir de los *docstrings*, tienen la ventaja que se pueden mirar los
*docstrings* en texto plano y no necesitan configuración.

La desventaja que tienen es que lo que uno escribe se ve en texto plano (pero
como *Google Style* es muy legible no es un problema). La otra desventaja es que
no permiten ver documentación aparte (que podría estar escrita en archivos de
texto), solamente permiten ver los *docstrings*.

Puede ser útil usarlos en algún apuro por eso en estas páginas explico bien
rápido como usarlos:

.. toctree::

   pydoctor
   pydoc

En esas páginas también hay una imagen de ejemplo para mirar como se ve mas o
menos la página generada.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _pydoctor: https://github.com/twisted/pydoctor
.. _pydoc: https://docs.python.org/3.6/library/pydoc.html
