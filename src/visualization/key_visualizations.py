import numpy as np
import matplotlib.pyplot as plt
from simulations.collatz_simulations import generate_dataset

# 1. Correlación ABC-core vs Pasos
df = generate_dataset(1, 10000)
plt.figure(figsize=(10, 6))
plt.scatter(df['abc_ratio'], np.log(df['steps']), alpha=0.2, c=df['max_value'], cmap='viridis')
plt.colorbar(label='Valor Máximo')
plt.xlabel('Proporción ABC-core')
plt.ylabel('log(Pasos)')
plt.title('Correlación ABC-core vs Velocidad Convergencia')
plt.savefig('../paper/figures/abc_correlation.png', dpi=300)

# 2. Distribución Fractal (Ejemplo n=27)
seq = collatz_sequence(27)
fractal_dims = [calculate_fractal_dim(seq[:i]) for i in range(10, len(seq))]
plt.figure(figsize=(10, 6))
plt.plot(fractal_dims, 'bo-')
plt.axhline(y=np.log2(3), color='r', linestyle='--')
plt.xlabel('Subsecuencia')
plt.ylabel('Dimensión Fractal')
plt.title('Evolución de la Dimensión Fractal (n=27)')
plt.savefig('../paper/figures/fractal_evolution_27.png', dpi=300)