# YTCweb

python 3.8.2

abrir wsl
bash

instalar virtual environment
python3 -m venv virtual-env

activar virtual environment
source virtual-env/bin/activate

instalar django
python3 -m pip install Django

correr server
python3 ytc/manage.py runserver

URL
http://127.0.0.1:8000/

instalar filebrowser
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

para abrir filebrowser (en otra terminal de wsl)
filebrowser -r ytc/webpage/static/content

filebrowser
http://127.0.0.1:8080/

Conectar ssh
nombre.apellido@ssh.inf.santiago.usm.cl
