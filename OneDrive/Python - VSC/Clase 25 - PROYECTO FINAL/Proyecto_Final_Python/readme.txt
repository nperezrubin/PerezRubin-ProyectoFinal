Proyecto Final - Nicolás Pérez Rubín
----------------------------------------------------------------------------------------------------------------------------------------------

Página de inicio: http://127.0.0.1:8000/

La web contiene un nav con los siguientes botones: 
- Inicio (padre.html) --> Utilizada para heredar templates. No requiere login. Muestra la fecha y hora actual antes del final de la página.

Páginas con CRUD y herencia desde 'padre.html': 
- Los 3 requieren login y contienen un formulario para agregar objetos, otro para buscar, y otro para borrar. También permite editar campos.
  - Clientes --> Contiene valoraciones de 2 clientes.
  - Pedidos --> Contiene los dos cafés más pedidos.
  - Sucursales --> Muestra las 2 sucursales actuales.

- About Me (aboutme.html) --> Datos del creador del sitio web. No requiere login.

- A la derecha tenemos un menú desplegable para la gestión de usuarios. Tiene las siguientes funcionalidades:
  - Si no se inició sesión, permite iniciarla, o bien crear un nuevo usuario
  - Si ya se inició sesión, permite editar el usuario y/o cambiar la contraseña, o bien cerrar sesión


Casos de prueba: https://docs.google.com/spreadsheets/d/1djJ9zFFpQbuIsFxr9ZimDn0imiAlM9ntG-mGxEUAc84/edit?usp=sharing
Video de prueba: En repositorio 

-----------------------------------------------------------------------------------------------------------------------------------------------



ADMIN
http://127.0.0.1:8000/admin/
superuser: nico_admin
pass: golden1234
email: nperezrubin@gmail.com

user2:
username: manud
password: manuloide1

usuario prueba video:
username: user_prueba
password: domingo2

----------------------------------------------------------------------------------------------------------------------------------------------


Notas para mí:

--> Abrir carpeta del proyecto con VSC

--> Consola-Terminal:
entorno-virtual-p/Scripts/activate (para activar el entorno virtual)
python manage.py runserver (para correr el servidor y que se pueda ver la página en el URL que indica)


--> GIT BASH:
en git Bash: (ir a la carpeta del proyecto, click derecho --> open git bash here)
- git status
- git add .
- git commit -m "comentario sobre el commit"
- ls
- git push (para llevarlo al repo) (luego hacer F5 en el repo y validar los cambios).




