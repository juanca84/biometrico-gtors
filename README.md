# BIOMETRICO GTORS

Instalar pyenv
https://ser-libre.com.ar/2018/05/30/debian-instalar-pyenv/

instalar una version de python
pyenv install 2.7.10

definir como global la version de python
pyenv global 2.7.10

instalar pip (adminitrador de paquetes de python)
sudo apt-get install python-pip

Instalar libfprint-dev que incluye la libreria libfprint0
sudo apt-get install libfprint-dev

instalar Cython ver tambien https://cython.readthedocs.io/en/latest/src/quickstart/install.html
pip install Cython --install-option="--no-cython-compile"


INSTALACIÓN DE GTORS(https://github.com/gtors/fprint)

Instalación de gtors
pip install git+https://github.com/gtors/fprint#egg=fprint-0.1
