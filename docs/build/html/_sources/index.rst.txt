
.. toctree::
   :maxdepth: 3
   :caption: Contenidos:

   instalacion
   escribir
   publicar
   ejemplos
   src/miproyecto

Introducción
------------

Esta es una guía simple sobre cómo documentar código escrito en python con
`Sphinx`_. Comenzar con la página sobre la instalación y luego con la que
explica cómo escribir la documentación, al final se puede ver la pagina sobre
cómo publicar en GitHub y los ejemplos.

Hay código fuente documentado automáticamente a partir de los *docstrings* en la
sección *miproyecto*.

Esta guía está escrita usando *Sphinx* así que la idea es ver el `código fuente
de todo esto`__ como ejemplo.

__ Repositorio_

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

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _Repositorio: https://github.com/martinber/guia-sphinx
