# Resolución de la Conjetura de Collatz mediante el ABC-Core

![ABC-core Visualization](paper/figures/abc_core_visualization.png)

Este repositorio contiene la solución completa a la Conjetura de Collatz mediante el descubrimiento del núcleo ABC, un atractor fractal con propiedades de simetría especular.

## Estructura del repositorio
- `data/`: Datasets generados
- `docs/`: Versión PDF del preprint
- `paper/`: Código LaTeX del artículo científico
- `src/`: Código fuente para simulaciones y visualizaciones
- `notebooks/`: Jupyter notebooks para análisis interactivo

## Instalación y reproducción
```bash
# Clonar repositorio
git clone https://github.com/MagesNRoses/Collatz-Proof.git
cd Collatz-Proof

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar simulaciones básicas
python src/simulations/collatz_simulations.py

# Generar figura 3D para n=27
python src/visualization/trajectory_3d.py