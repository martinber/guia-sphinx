Usar pydoctor
=============

Si o si usa *Python 2*.

::

  cd batch_ffmpeg
  sudo pip install pydoctor
  pydoctor --add-package ./ --docformat plaintext
  pydoctor --add-module ./a.py --docformat plaintext

