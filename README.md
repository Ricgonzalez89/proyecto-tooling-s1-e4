# API - Proyecto Tooling  
## Integrantes del equipo 
* **Daniela Sofia Marquez C.I: 31.089.011**
* **Tomas Soto C.I: 30.266.566** 
* **Ana Karina Garcia C.I: 31.099.867** 
* **Yosger Toro C.I: 31.066.236** 
* **Ricardo Gonzalez C.I: 31.025.997** 
## Instalación y ejecución  
# Clonar repositorio 
```bash 
git clone <url-del-repo> cd <nombre-del-repo>  
```
# Crear entorno virtual 
```bash 
python -m venv .venv  
```
# Activar entorno 
* **Windows:** 
```bash
.venv\Scripts\activate 
```
* **Mac/Linux:** 
```bash 
source .venv/bin/activate 
```
# Instalar dependencias 
```bash
pip install -r requirements.txt 
```
# Ejecutar servidor python 
```bash
python app.py 
```
## Calidad de Código y Estilo
Para mantener el código limpio y bajo los estándares de PEP 8, utilizamos las siguientes herramientas.

* **Formattrs (formateado): black app.py** 
* **Linter de advertencias y estilo: flake8 app.py** 
* **Linter de calidad y análisis estático: pylint app.py** 
* **Ejecución de 2 pruebas unitarias para los endpoints: pytest -q** 