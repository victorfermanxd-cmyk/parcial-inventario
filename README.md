# Sistema de análisis de inventario

Proyecto académico para el parcial de Programación Computacional III.

## Funcionalidades
- Inventario de ejemplo en `datos.csv` para San Salvador, Santa Ana, San Miguel, La Libertad y Sonsonate.
- Análisis exploratorio con Pandas (`analisis.py`).
- Dashboard de escritorio con PyQt5 y gráficos de Matplotlib (`app.py`).
- Informe de consultoría en PDF.

## Requisitos
Python 3.10 o superior recomendado.

## Instalación
```bash
python -m venv venv
```
En Windows:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar el análisis
```bash
python analisis.py
```

## Ejecutar la aplicación gráfica
```bash
python app.py
```

## Estructura
- `app.py`: interfaz gráfica.
- `analisis.py`: inspección y análisis de datos.
- `datos.csv`: inventario de ejemplo.
- `informe_consultoria.pdf`: informe de resultados.
- `requirements.txt`: dependencias.
- `.gitignore`: archivos que no deben subirse.

## Integrantes
- Integrante 1: Victor Ismael Garcia Ferman
- Integrante 2: Fray Stid Ramirez Ordoñez
