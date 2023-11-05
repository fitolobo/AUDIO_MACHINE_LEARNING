# Alternativa 1: Manejo de Ambiente via Poetry
### Para installar poetry

**Observación**: en general estas herramientas son fáciles de instalar en sistemas OSX y Linux. Para windiws siempre será un dolor. 


La instalación la realicé en un Mac OSX:

1 - ```brew install pipx```

2 - ```pipx install poetry```

3 - El problema que tenía my consola era que yo estaba usando una terminal diferente (zsh). Esta terminal
no estaba logrando acceder al paquete instaldao. Tuve que entrar al archivo ```~/.zshrc```
con un editor de texto o con ```nano ~/.zshrc``` y agregar la siguiente linea dentro de ese archivo: ```export PATH=$HOME/.local/bin:$PATH```
con esto le avismos a la terminal zsh que en ese directorio llamado ```bin``` se encuentran los binarios que instalé (ya sean de poetry u otras dependencias.)

Referencia: [Link](https://python-poetry.org/docs/#installing-with-pipx)

### Para instalar Pyenv

Para instalar ```pyenv``` en Mac OSX/UNIX: 
```
    brew update
    brew install pyenv
```

Para sistemas Windows es necesario crear un ambiente para pyenv. 

Referencia [Link](https://github.com/pyenv/pyenv)

### Uso de ambas herramientas

Primero debemos crear un proyecto con nombre en Spanglish: 

1 - ```poetry new my-proyect```

Obtienen como respuesta algo como: ```Created package my_proyect in my-proyect```

2 - Pueden revisar las versiones de python instaladas con 
```pyenv versions```. Obteniendo una respuesta similar a: 

```* system (set by /Users/rodolfolobocarrasco/.pyenv/version)
  3.9.7
  3.11.6
  ```

Si no tuvieran versiones de python instaladas deberán instalar a través de ```pyenv install 3.10.4``` (por ejemplo), luego si revisan, deberá aparecer listada la versión que agregaron. En mi caso: 

```pyenv install 3.10.4
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.10.4.tar.xz...
-> https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tar.xz
Installing Python-3.10.4...
python-build: use readline from homebrew
python-build: use ncurses from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.10.4 to /Users/rodolfolobocarrasco/.pyenv/versions/3.10.4
```

Si repito el comando ```pyenv versions``` ahora obtengo: 

```
pyenv versions
* system (set by /Users/rodolfolobocarrasco/.pyenv/version)
  3.9.7
  3.10.4
  3.11.6
  ```

  4 - Luego, entramos al directorio donde esta nuestro proyecto via terminal a través del comando ```cd my-proyect```, estamos en condiciones de seleccionar una versión de python para nuestro ambiente a través de ```pyenv local 3.11.6``` esto crea un archivo dentro del directorio llamado ```.python-version``` que dentro contiene el nombre de la versión de python. Además adentro del directorio hay otros archivos creados automáticamente por poetry: 

```
  ➜  my-proyect tree -L 2
.
├── README.md
├── my-proyect 
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py
```

Observemos el contenido en cada uno de los archivos: 

- ```.python-version```: 3.11.6

- ```pyproject.toml```: contiene una descripción del ambiente que estamos creando. Por ahora no hay dependencias installadas. La versión de python debe ser mayor a 3.9 por eso el símbolo ```^```.

```[tool.poetry]
name = "my-proyect"
version = "0.1.0"
description = ""
authors = ["fitolobo <rodolfolobo@ug.uchile.cl>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

- Los archivos ```__init__.py``` están vacíos y permitirán entre otras cosas poder llamar módulos que estén adentro de esos directorios (módulos = scripts).

5 - Ahora instalemos dependencias a través de ```poetry add```, por ejemplo: 

```
poetry add openai
```

En este caso mi consola arroja: 

```
➜  my-proyect poetry add openai
Creating virtualenv my-proyect-G33NJe_6-py3.9 in /Users/rodolfolobocarrasco/Library/Caches/pypoetry/virtualenvs
Using version ^0.28.1 for openai

Updating dependencies
Resolving dependencies... (6.4s)

Package operations: 14 installs, 0 updates, 0 removals

  • Installing frozenlist (1.4.0)
  • Installing idna (3.4)
  • Installing multidict (6.0.4)
  • Installing aiosignal (1.3.1)
  • Installing async-timeout (4.0.3)
  • Installing attrs (23.1.0)
  • Installing certifi (2023.7.22)
  • Installing charset-normalizer (3.3.2)
  • Installing urllib3 (2.0.7)
  • Installing yarl (1.9.2)
  • Installing aiohttp (3.8.6)
  • Installing requests (2.31.0)
  • Installing tqdm (4.66.1)
  • Installing openai (0.28.1)
```


Si ahora revisamos el archivo ```pyproject.toml```:

```
[tool.poetry]
name = "my-proyect"
version = "0.1.0"
description = ""
authors = ["fitolobo <rodolfolobo@ug.uchile.cl>"]
readme = "README.md"

[tool.poetry.dependencies]
python = ">=3.9"
openai = "^0.28.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Ha instalado la dependencia y la lista dentro de este documento. 
A veces es posible que existan problemas con las versiones de python y las cosas que queremos instalar. En tal caso poetry imprime por pantalla las posibles soluciones a esos conflictos de dependencia. Por ejemplo, yo intenté instalar ```numpy``` a través de ```poetry add numpy``` pero no pude por un conflicto con la versión de python, por pantalla mesugiere colocar dentro del archivo ```pyproject.toml``` lo siguiente en la propiedad python : 

```
python = ">=3.9,<3.13"
```

Luego, fui capaz de installar numpy en la versión ```1.26.1```


6 - **Levantamos el ambiente!**: para levantar el ambiente deberán utilizar el comando ```poetry shell```, obteniendo: 

```
➜  my-proyect poetry shell
Spawning shell within /Users/rodolfolobocarrasco/Library/Caches/pypoetry/virtualenvs/my-proyect-G33NJe_6-py3.9
➜  my-proyect emulate bash -c '. /Users/rodolfolobocarrasco/Library/Caches/pypoetry/virtualenvs/my-proyect-G33NJe_6-py3.9/bin/activate'
(my-proyect-py3.9) ➜  my-proyect 
```

7 - Si ustedes desean correr un script, por ejemplo de nombre ```test.py``` de python solo bastaría realizar ```poetry run python test.py```. 

8 - Si desean utilizar notebooks para realizar experimentos bastaría instalar jupyterlab a través de ```poetry add jupyterlab```, si tienen el ambiente andando con ```poetry shell``` es solo usar el comando ```jupyter lab``` dentro de la consola del ambiente, ahí se abrirá una ventana en su navegador de preferencia con el notebook. 

9 - Para instalar dependencias más complejas como ```whisper``` u otros repositorios que no manejan solo un ```requirements.txt``` requerirán levantar el ambiente con ```poetry shell``` y luego dentro de la consola del ambiente usar ```pip``` de la siguiente forma:

```pip install git+<linktorepo>```

Por ejemplo: 

```pip install git+https://github.com/openai/whisper.git ```

Sin embargo, parecen existir conflictos con algunas dependencias o formas de instalación y al utilizar esta forma whisper parece estar instalado mieintras el ambiente esté instalado. Una vez cerrado el ambiente con ```exit``` al volver a levantarlo no queda registro en el ```pyproyect.toml```
de la instalación y deberás repetir el paso anterior. 

10 - Para salir del ambiente debes ejecutar en la terminal ```exit``` y esto te retorna a tu consola. 

# Alterantiva 2: Manejo de Ambiente via pyenv, pyenv-virtualenv


En Mac OSX: 
1 - Instala ```brew install pyenv```

2 - Luego deberás avisar a Pyenv donde están los binarios de python instalados en tu computador. En mi caso Zsh será utilizando los siguientes comandos en la terminal: 

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

para bash u otros leer el segundo link que dejé abajo. 

Referencia (Sección Getting Pyenv):  [Link](https://github.com/pyenv/pyenv#homebrew-in-macos)
Referencia (Sección set up shell enviroment): [Link](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv)

3 - Ahora puedes instalar una versión de python, por ejemplo:  ```pyenv install 3.10.9```

4 - Instala ```brew install pyenv-virtualenv``` (nuestra alternativa a poetry)

5 - Crea el ambiente virtual ```pyenv virtualenv 3.10.9 mi-ambiente-python-whisper``` y luego ```pyenv local mi-ambiente-python-whisper```

6 - Reinicia la terminal ```exec zsh -l``` Si tienes otro tipo de terminal revisa las opciones aquí [Link](https://stackoverflow.com/questions/57262349/restart-terminal-without-closing-on-macos)

7 - Ahora cada vez que entres al directorio se activará el ambiente virtual automáticamente. 

8 - Ahora solo deberás instalar via ```pip install <nombre de la libreria>``` las cosas que necesites. 

9 - Para guardar en un archivo ```requierements.txt``` todas las depencias que has instalad debes ejectuar ```pip freeze > requirements.txt```

Ahora es posible instalar de manera más simple  ```pip install git+https://github.com/openai/whisper.git ```