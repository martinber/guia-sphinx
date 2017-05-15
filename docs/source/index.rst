Guía de Sphinx
==============

.. toctree::
   :maxdepth: 3
   :caption: Contenidos:

   instalacion
   escribir
   publicar
   codigo_fuente/ejemplos
   ejemplo_jerarquia/ej1

Introducción
------------

Esta es una guía simple sobre cómo documentar código escrito en python con
`Sphinx`_. Comenzar con la página sobre la instalación y luego con la que
explica cómo escribir la documentación.

Como ejemplo hay código fuente documentado automáticamente a partir de los
*docstrings* y hay varias páginas que muestran cómo hacer una jerarquía en el
árbol de contenidos.

Esta guía está escrita usando *Sphinx* así que la idea es ver el `código fuente
de todo esto`__. Al ver los ``.rst`` desde *GitHub*, es necesario apretar el
botón *Raw* para verlos en texto plano.

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
  viene perfecto para la documentación generada con **Sphinx**.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _Repositorio: https://github.com/martinber/guia-sphinx
