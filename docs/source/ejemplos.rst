Ejemplos
========

Sobre documentar desde docstrings
---------------------------------

Hice varios ejemplos (6 en total) para :download:`descargar
<../../ejemplos_sphinx.zip>`. Hay dos para :ref:`cada forma de documentar
<tipos_receta>` explicada en la página de :doc:`Recetas <recetas/inicio>`:

* Receta simple: Se incluyen los *docstrings* directamente en ``index.rst``,
  estos ejemplos no siguen la :ref:`estructura de archivos recomendada
  <estructura>`.

  * **introduccion**: Documenta solamente un módulo de ejemplo.

  * **magia**: Tiene dos módulos.

* Receta manual: Cada módulo está en una página separada que fue creada
  manualmente.

  * **batch_ffmpeg**: Es un programa que no sigue la :ref:`estructura de
    archivos recomendada <estructura>`.

  * **pynprcalc**: Es una calculadora con varios módulos y que además tiene
    fórmulas matemáticas en la documentación.

* Usando *autosummary*: Cada módulo está en una página separada generada
  automaticamente.

  * **batch_ffmpeg**.

  * **pynprcalc**.

Sobre documentar texto
----------------------

Como ejemplo, se puede ver el `código fuente de esta guía`__.

__ Repositorio_

.. note::
    Al ver los ``.rst`` desde *GitHub*, es necesario apretar el botón *Raw* para
    verlos en texto plano.

.. _Repositorio: https://github.com/martinber/guia-sphinx

pydoctor
--------

También se puede ver la documentación generada por *pydoctor* siguiendo
:doc:`estas instrucciones <./alternativas/pydoctor>`.
