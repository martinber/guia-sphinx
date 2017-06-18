Guía Sphinx
===========

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

Esta es una guía simple sobre cómo documentar código escrito en python con
`Sphinx`_.

Habría que leer las páginas en el orden en que están en la tabla de contenidos.
El problema es que son bastantes cosas. Si no hay ganas de aprender tanto hay
recetas que dicen cómo configurar y hacer todo bien rápido sin tantas
explicaciones.

También hay una :download:`presentación que puede servir como introducción
<../../presentacion.pdf>`.

Como esta guía está en *GitHub* y está hecha en *Sphinx*, se puede `descargar,
mirar, mandar correcciones y esas cosas`__.

__ Repositorio_

También hice varios :doc:`ejemplos <ejemplos>`.

Notas
-----

* Cuando probé *Sphinx* en *Ubuntu* tuve un problema, al hacer ``make html``
  recibía un error que decía ``No module named sphinx``. Lo solucioné
  modificando el ``Makefile``, cambiando ``python -msphinx`` por
  ``sphinx-build``. Supongo que es algo relacionado a cambiar de *Python 2* a
  *Python 3*.

.. _glosario:

Glosario
--------

Las cosas que se usan para hacer esto son:

* **Python**: Es el lenguaje de programación que usamos para hacer el programa.
  Hay comentarios especiales que documentan una función, clase, etc. que se
  llaman **docstrings**.

* **Sphinx**: Es un programa que nos ayuda a generar la documentación para ese
  programa. Toma varios archivos escritos con **reStructuredText** y junto con
  los **docstrings** genera una página web estática.

* **reStructuredText**: Es un lenguaje de marcado, especifica como crear
  títulos, listas, tablas, cómo insertar imagenes, etc.

* **GitHub**: Es un sitio web que hostea sobre todo proyectos de software libre
  de forma gratuita. Permite hostear una web estática para cada proyecto, que
  viene perfecto para la documentación generada con **Sphinx** pero es opcional.

Esto es sobre *Python*:

* **módulo** o **script**: Es un archivo ``.py``.

* **paquete**: Es una carpeta que contiene archivos ``.py``. Debe tener un
  archivo (que puede estar vacío) llamado ``__init__.py``.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _Repositorio: https://github.com/martinber/guia-sphinx
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _GitHub: https://github.com/
