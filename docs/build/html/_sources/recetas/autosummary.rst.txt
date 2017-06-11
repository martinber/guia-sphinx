Utilizando autosummary
======================

.. note::

  Acá se explica cómo configurar y usar *autosummary*, antes se debe configurar
  como se indica en :doc:`la receta <./inicio>`.

La documentación va a consistir con una página principal que tiene una
descripción simple y varios links, cada uno lleva a la documentación de un
módulo que está en una página separada.

Hay que hacer dos archivos ``.rst``: uno es el *index* y otro es una plantilla
que se utiliza para generar la documentación de cada módulo.

Esto se hace gracias a la extensión *autosummary*. Esta extensión crea un
archivo ``.rst`` para cada módulo a partir de la plantilla. Estos archivos
``.rst`` generados a partir de la platilla se guardan en
``docs/source/_autosummary/``.

Luego a partir de el ``index.rst`` y de cada ``.rst`` generado, se crea la
documentación en *HTML*.

.. note::

  *autosummary* por defecto no reemplaza los archivos ``.rst`` ya generados, por
  lo tanto si se cambia la plantilla hay que borrar la carpeta
  ``docs/source/_autosummary/`` para que se genere nuevamente y se vean
  reflejados los cambios.

.. note::

  Para entender mejor cuál es el trabajo que hace *autosummary* mirar en qué
  consiste el :doc:`método manual <./manual>`.

Configurar
----------

* Agregar la extension ``sphinx.ext.autosummary`` en la lista ``extensions``.

* En cualquier lado poner ``autosummary_generate = True``.

Escribir
--------

Editar ``index.rst`` y dejarlo algo así:

::

  Documentación de mi proyecto
  ============================

  .. toctree::
     :maxdepth: 2
     :caption: Contents:

  Esta es una introducción a lo que hace este proyecto...

  .. autosummary::
     :toctree: _autosummary

     miproyecto.mimodulo1
     miproyecto.mimodulo2

  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

.. note::

  Yo escribí ``miproyecto.modulo1``. Esto debe ser el módulo a documentar tal
  cual uno lo importa desde Python. Depende de qué se haya agregado al ``path``
  en ``conf.py``.

Después crear una plantilla, el archivo sería
``docs/source/_templates/autosummary/module.rst``. Dentro debe llevar escrito lo
que estará en la página de cada módulo. Hice una plantilla que para mí es mejor
que la que viene por defecto::

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
