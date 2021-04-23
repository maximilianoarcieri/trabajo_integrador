# trabajo_integrador
Trabajo integrador para Seminario de Python 2021

## MemPy: entrenando la memoria con Python
En este proyecto se irá desarrollando un juego de memoria.

El mismo se realizará con Python y utilizando diferentes librerías, como PySimpleGUI para las interfaces gráficas.

También se incluyen pruebas y modificaciones personales, ya que la versión final del trabajo se alojará en GitLab.

## Ejecución
  Se debe ejecutar el módulo main.py, el cual abrirá la ventana de menú del juego. Si el usuario es nuevo, podrá registrarse indicando solo su nombre de usuario y marcando la casilla "Usuario nuevo", luego de apretar "Siguiente" lo llevará a completar los demás datos, quedando registrado en la base de datos (en este caso, nuestra base de datos es el archivo "file_users.csv"). 
 
  Si el usuario ya está registrado, ingresa sus datos y si la clave es correcta, se le permitirá el ingreso.
  
 ## Funciones
 ### Register
 Se presenta la ventana que permitirá que los usuarios se registren con sus datos.
 ### Encrypt
 Recibe la contraseña del usuario nuevo y la guarda en la base de datos aplicando un algoritmo de encriptado (este algoritmo lo desarrollé yo a modo de prueba, no se busca una seguridad avanzada ni mucho menos).
 
 Tambíen, al momento de que un usuario quiere conectarse con usuario y contraseña, este módulo aplica el algoritmo inverso sobre la clave almacenada en la base de datos correspondiente al usuario recibido. Si esta coincide con la que el usuario ingresó se permite el ingreso.
