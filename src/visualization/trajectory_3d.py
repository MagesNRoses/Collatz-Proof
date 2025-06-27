# src/visualization/trajectory_3d.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

# Importación absoluta
from src.simulations.collatz_simulations import collatz_sequence

def plot_3d_trajectory(n, save_path=None):
    seq = collatz_sequence(n)
    
    # Crear directorio si no existe
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Convertir secuencia a coordenadas 3D
    x = [np.log(s) for s in seq]
    y = list(range(len(seq)))
    z = [s % 10 for s in seq]

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Crear línea con gradiente de color
    for i in range(len(seq)-1):
        ax.plot(
            [x[i], x[i+1]],
            [y[i], y[i+1]],
            [z[i], z[i+1]],
            color=plt.cm.viridis(i/len(seq)),
            linewidth=2
        )

    ax.scatter(x, y, z, c=range(len(seq)), cmap='viridis', s=50)
    ax.set_xlabel('log(n)')
    ax.set_ylabel('Paso')
    ax.set_zlabel('n mod 10')
    ax.set_title(f'Trayectoria 3D de Collatz para n={n}')

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado en {save_path}")
    else:
        plt.show()

if __name__ == "__main__":
    plot_3d_trajectory(27, save_path='../paper/figures/3d_trajectory_27.png')