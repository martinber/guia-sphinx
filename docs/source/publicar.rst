Publicar en GitHub
==================

`GitHub`_ es un sitio web que hostea sobre todo proyectos de software libre de
forma gratuita. Una alternativa similar es `GitLab`_, aunque voy a usar
`GitHub`_ porque es más conocido.

La función principal de ambos es hostear repositorios `Git`_, pero agregan más
funciones como *Wikis*, *Issues*, y además permiten hostear una pagina web
estática para el proyecto que en este caso va a ser la documentación generada
con `Sphinx`_.

La funcionalidad del hosteo de sitios web se llama `GitHub Pages`_. Se necesita
saber algo sobre `Git`_, y hay varias formas de publicar el sitio web estático.
Para este caso creo que lo mejor es poner los archivos ``html`` generados en una
*branch* llamada ``github-pages`` usando ``git subtree``.

Por primera vez
---------------

Primero se puede crear el repositorio en `GitHub`_, luego creamos el repositorio
en nuestra PC y subimos el código.

Al crear el repositorio se muestra una dirección que se debe usar para subir los
cambios. Si se usa la dirección que empieza con ``https://`` hay que poner la
contraseña de *GitHub* cada vez que se suban modificaciones, si se usa la
dirección que empieza con ``git@`` previamente hay que agregar la clave
pública de *SSH* de la PC a la cuenta de *GitHub*. Yo voy mostrar un ejemplo de
cuando se usa *SSH*, por eso más abajo usé la URL que empieza con ``git@``

.. code:: sh

    sudo apt install git # instalar git
    cd proyecto # ir a la raíz del proyecto

    git init # inicializar el repositorio git
    git remote add origin git@github.com:usuario/proyecto.git # indicar URL de GitHub

    # antes de continuar es necesario ya tener la documentación generada

    git add -A # agregar todos los cambios al commit
    git commit -m "commit inicial" # crear commit
    git push -u origin master # subir cambios

    # ahora subiremos al directorio con los documentos html como una branch llamada gh-pages
    git subtree push --prefix ./docs/build/html origin gh-pages 




Actualizar documentanción
-------------------------

.. _GitHub: https://github.com/
.. _GitLab: https://gitlab.com/
.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _Git: https://git-scm.com/
.. _GitHub Pages: https://pages.github.com/
