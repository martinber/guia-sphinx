Usar pydoctor
=============

Si o si usa *Python 2*, pero eso no significa que no pueda documentar código
escrito en *Python 3*.

Imagen de ejemplo:

.. image:: ../imagenes/reemplazar_ext_html_pydoctor.png

Con estos pasos se generarán archivos ``html`` en una carpeta llamada
``apidoc``, que dentro tiene un ``index.html`` que es lo que nos interesa.

::

  cd mi_proyecto
  sudo pip install pydoctor

Luego el comando depende de si se quiere documentar un :ref:`módulo o un paquete
<glosario>`::

  pydoctor --add-package ./ --docformat plaintext
  pydoctor --add-module ./modulo.py --docformat plaintext

.. warning::

  Por alguna razón algunos módulos se muestran como *undocumented* en el
  ``html`` generado, todavía no sé por qué a *pydoctor* no le gustan algunos
  módulos.

.. todo::

  Encontrar por qué. Ver ``parse.py`` y ``convert.py`` de *batch_ffmpeg*. En el
  :doc:`ejemplo <../ejemplos>` se puede ver el problema.
