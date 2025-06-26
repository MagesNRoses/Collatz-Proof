import numpy as np
import pandas as pd
from tqdm import tqdm

LOG23 = np.log2(3)
EPSILON = 0.05

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def classify_region(seq, window=5):
    """Clasifica regiones con ventana móvil"""
    regions = []
    ops = []  # Almacenar operaciones (1 para 3n+1, 0 para n/2)
    
    # Obtener operaciones
    for i in range(1, len(seq)):
        if seq[i] == 3 * seq[i-1] + 1:
            ops.append(1)
        else:
            ops.append(0)
    
    # Clasificar con ventana móvil
    for i in range(len(ops)):
        start = max(0, i - window + 1)
        window_ops = ops[start:i+1]
        j = sum(window_ops)  # Operaciones 3n+1
        k = len(window_ops) - j  # Operaciones n/2
        
        if k == 0:
            ratio = float('inf')
        else:
            ratio = j / k
        
        if ratio > LOG23 + EPSILON:
            region = 'A'
        elif LOG23 < ratio <= LOG23 + EPSILON:
            region = 'B'
        elif LOG23 - EPSILON <= ratio <= LOG23:
            region = 'C'
        else:
            region = 'D'
        regions.append(region)
    return regions

def generate_dataset(n_min=1, n_max=100):
    """Genera dataset inicial"""
    results = []
    for n in tqdm(range(n_min, n_max+1), desc="Generando dataset"):
        seq = collatz_sequence(n)
        regions = classify_region(seq)
        abc_count = regions.count('A') + regions.count('B') + regions.count('C')
        total_ops = len(ops)
        results.append({
            'n': n,
            'steps': len(seq)-1,
            'abc_ratio': abc_count / total_ops if total_ops > 0 else 0.0,
            'max_value': max(seq)
        })
    return pd.DataFrame(results)

if __name__ == "__main__":
    # Generar y guardar dataset
    df = generate_dataset(1, 100)
    df.to_csv('../../data/collatz_initial_dataset.csv', index=False)