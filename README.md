Proyecto base Python (entorno reproducible)

Este repositorio es un template mínimo profesional de proyecto Python cuyo objetivo es:
	•	Tener un entorno aislado por proyecto (no contaminar el sistema)
	•	Poder replicar exactamente el mismo entorno en otra máquina
	•	Trabajar de forma ordenada y profesional con Git
	•	Facilitar el trabajo colaborativo

No estamos construyendo funcionalidad todavía.
Estamos construyendo la base correcta del proyecto.

⸻

Requisitos previos

Antes de comenzar, debes tener instalado:
	•	Python 3.13.5 (o una versión 3.10+ consistente en todo el equipo)
	•	Git
	•	Terminal compatible con entorno Unix (macOS, Linux o WSL)

Puedes verificar tu versión de Python con:

python --version

Debe mostrar algo como:

Python 3.13.5


⸻

Estructura del proyecto

La estructura esperada del proyecto es:

finance-test/
├── main.py
├── requirements.txt
├── .gitignore
├── venv/        ← entorno virtual (NO se sube a Git)
└── README.md

El objetivo es que cualquier persona que clone este repositorio pueda reconstruir exactamente el mismo entorno.

⸻

Paso 1: Crear el entorno virtual (venv)

Desde la raíz del proyecto, ejecuta:

python -m venv venv

Esto crea una carpeta llamada venv/ que contiene:
	•	Su propio Python
	•	Su propio pip
	•	Sus propias librerías instaladas

Este aislamiento es fundamental para evitar conflictos entre proyectos.

⸻

Paso 2: Activar el entorno virtual

Ejecuta:

source venv/bin/activate

Cuando el entorno está activo, tu terminal debería verse así:

(venv) usuario@maquina finance-test %

El prefijo (venv) confirma que estás trabajando dentro del entorno aislado.

⸻

Paso 3: Verificación profesional del entorno

Este paso es crítico para confirmar que todo está bien configurado.

Ejecuta:

which python
which pip

El resultado debe apuntar a rutas similares a:

/ruta/a/tu/proyecto/finance-test/venv/bin/python
/ruta/a/tu/proyecto/finance-test/venv/bin/pip

Si en lugar de eso aparece algo como:
	•	/usr/bin/python
	•	/opt/homebrew/bin/python
	•	.pyenv/...

Entonces el entorno virtual no está activo correctamente y debes revisar el paso anterior.

⸻

Paso 4: Instalación de dependencias

Siempre con el entorno activado, puedes instalar librerías así:

pip install requests

Todas las librerías se instalarán únicamente dentro del proyecto.

⸻

Paso 5: Generar el archivo requirements.txt

Este archivo registra las versiones exactas de las dependencias instaladas.

Ejecuta:

pip freeze > requirements.txt

Ejemplo de contenido:

requests==2.31.0
urllib3==2.2.1
certifi==2024.2.2

Este archivo es clave para lograr un entorno reproducible.

⸻

Paso 6: Cómo otra persona reproduce el entorno

Cualquier persona que clone el repositorio puede ejecutar exactamente esto:

git clone https://github.com/Ccanas-h/python-standar.git
cd python-standar

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Resultado:
Tendrá exactamente las mismas dependencias, con las mismas versiones, en un entorno limpio.

Ese es el objetivo profesional de este proyecto.

⸻

Paso 7: Archivo .gitignore recomendado

El archivo .gitignore debe contener al menos lo siguiente:

venv/
__pycache__/
*.pyc
.env
.DS_Store
.vscode/
.idea/

Esto evita subir archivos locales, temporales o específicos del entorno de desarrollo.

⸻

Objetivo alcanzado

Con esta estructura, el proyecto ya cumple estándares profesionales reales:
	•	Entorno aislado por proyecto
	•	Dependencias versionadas
	•	Proyecto completamente reproducible
	•	Base sólida para escalar el desarrollo

A partir de aquí, ya se puede construir funcionalidad real sobre una base técnica correcta.

⸻

Nota final

Este repositorio no busca ser complejo.
Busca ser correcto, claro, mantenible y profesional desde el primer día.

Una base bien construida evita problemas durante todo el ciclo de vida del proyecto.
