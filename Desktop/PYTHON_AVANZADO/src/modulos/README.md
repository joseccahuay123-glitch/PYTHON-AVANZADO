# Modularidad
## 1
## 2
## 3. Importar solo lo necesario (from ... import)
a veces es necesario importar solo una parte del modulo, etso se usa cuando deseamos utilizar partes especificas de un modulo. para esto usamos `from nombre_modulo import parte especifica`
`matematicas.py`
```python
def resta(a,b):
    return a-b
def suma (a,b)
    return a+b
PI=3.1415
```
`main.pi`
```python
from matematicas import PI
```
## PAQUETES (carpetas de modulos)
cuando el proyecto empiesa a crecer los módulos se ordenan en carpetas
