# src/simulations/collatz_simulations.py
import pandas as pd
from tqdm import tqdm
import os

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

# Crear directorio si no existe
os.makedirs('../data', exist_ok=True)

# Lista para almacenar resultados
results = []

# Generar secuencias para n de 1 a 100
for n in tqdm(range(1, 101), desc="Simulando Collatz"):
    seq = collatz_sequence(n)
    steps = len(seq) - 1
    max_value = max(seq)
    sequence_str = " → ".join(map(str, seq))
    
    results.append({
        'n': n,
        'steps': steps,
        'max_value': max_value,
        'sequence_length': len(seq),
        'sequence': sequence_str
    })

# Crear DataFrame y guardar como CSV
df = pd.DataFrame(results)
df.to_csv('../data/collatz_initial_dataset.csv', index=False)
print("Datos guardados exitosamente!")