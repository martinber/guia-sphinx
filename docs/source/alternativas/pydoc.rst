Usar pydoc
==========

Imagen de ejemplo:

.. image:: ../imagenes/reemplazar_ext_html_pydoc.png

Este programa viene incluido con *Python*, permite ver los *docstrings* de
cualquier módulo de diferentes formas.

Muestro como mirar una página web generada a partir de la documentación:

::

  cd mi_proyecto
  pydoc3 -p 9876

Al correr esos dos comandos se inicia un servidor web en el puerto 9876, para
abrir el navegador se puede apretar ``b`` y luego ``Enter``.

En la web se va a ver la documentación de todo lo que haya instalado en la
computadora, a nosotros nos interesa la sección ``.`` que es la documentación de
la carpeta actual (donde ejecutamos el comando).

De esta forma no se guardan los ``html`` generados en ningún lado. Se pueden
guardar pero no creo que valga la pena.
