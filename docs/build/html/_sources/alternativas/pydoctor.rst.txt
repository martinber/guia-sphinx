Usar pydoctor
=============

Si o si usa *Python 2*.

Imagen de ejemplo:

.. image:: ../imagenes/reemplazar_ext_html_pydoctor.png

.. todo::

  Revisar.

::

  cd batch_ffmpeg
  sudo pip install pydoctor
  pydoctor --add-package ./ --docformat plaintext
  pydoctor --add-module ./a.py --docformat plaintext

