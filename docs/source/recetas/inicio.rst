Generar la configuración
------------------------

Ir a la carpeta del proyecto y ejecutar ``sphinx-quickstart``.

::

  cd batch_ffmpeg
  sphinx-quickstart

Va a ir preguntando algunas opciones, usar:

* Root path for documentation: docs/
* Separate source and build directories: y

También pregunta si se desean activar unas extensiones, activar: 

* autodoc
* intersphinx
* todo
* viewcode
* githubpages (si se va a usar *GitHub*)

Al final pregunta si se busca crear *makefiles*, responder sí a ambos.

Configurar
----------

Editar ``conf.py``:

* Importar ``os``, ``sys`` y agregar carpeta al *PATH*.
* Agregar las extensiones ``napoleon`` y ``autosummary``.
* ``autosummary_generate = True``.
* ``todo_include_todos = True``.

Editar ``index.rst`` y agregar:

::

    .. autosummary::
       :toctree: _autosummary
       
       batch_ffmpeg
       batch_ffmpeg.file
       batch_ffmpeg.convert
       batch_ffmpeg.command
       batch_ffmpeg.ui.interactive
       batch_ffmpeg.ui.shell

  Pegar template en ``_templates``.

Usar pydoc
----------

::

  cd batch_ffmpeg
  pydoc3 -p 9876

  Despues apretar b y Enter

Usar pydoctor
-------------

Si o si usa *Python 2*.

::

  cd batch_ffmpeg
  sudo pip install pydoctor
  pydoctor --add-package ./ --docformat plaintext
  pydoctor --add-module ./a.py --docformat plaintext

