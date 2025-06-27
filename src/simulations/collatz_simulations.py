# src/simulations/collatz_simulations.py
import numpy as np
import pandas as pd
import os
from tqdm import tqdm

LOG23 = np.log2(3)
EPSILON = 0.05

def collatz_sequence(n):
    """Genera la secuencia de Collatz para un número n"""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def classify_region(seq, window=5):
    """Clasifica cada paso en regiones A, B, C o D"""
    regions = []
    ops = []  # 1 para 3n+1, 0 para n/2
    
    # Identificar operaciones
    for i in range(1, len(seq)):
        if seq[i] == 3 * seq[i-1] + 1:
            ops.append(1)
        else:
            ops.append(0)
    
    # Clasificar con ventana móvil
    for i in range(len(ops)):
        start = max(0, i - window + 1)
        window_ops = ops[start:i+1]
        j = sum(window_ops)  # Cantidad de 3n+1
        k = len(window_ops) - j  # Cantidad de n/2
        
        if k == 0:
            ratio = float('inf')
        else:
            ratio = j / k
        
        # Clasificación
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
    """Genera el dataset sin usar tqdm para depuración"""
    results = []
    
    # Versión sin tqdm (comentada la versión con tqdm)
    # for n in tqdm(range(n_min, n_max+1), desc="Generando dataset"):
    for n in range(n_min, n_max+1):
        seq = collatz_sequence(n)
        regions = classify_region(seq)
        total_ops = len(regions)
        abc_count = sum(1 for r in regions if r in ['A', 'B', 'C'])
        
        results.append({
            'n': n,
            'steps': len(seq)-1,
            'abc_ratio': abc_count / total_ops if total_ops > 0 else 0.0,
            'max_value': max(seq),
            'total_ops': total_ops,
            'region_A': regions.count('A'),
            'region_B': regions.count('B'),
            'region_C': regions.count('C'),
            'region_D': regions.count('D'),
            'sequence': str(seq)  # Para depuración
        })
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    import os
    import pandas as pd
    
    # Crear directorio si no existe
    os.makedirs('../data', exist_ok=True)
    
    # Generar dataset
    df = generate_dataset(1, 100)
    
    # DEBUG: Verificar el DataFrame en memoria
    print("\nDebug - DataFrame en memoria:")
    print(df.head())
    print(f"\nTotal de filas: {len(df)}")
    
    # Guardar a CSV - Método alternativo robusto
    output_path = '../data/collatz_initial_dataset.csv'
    try:
        # En collatz_simulations.py, reemplazar el bloque de guardado con:
        import csv
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(df.columns)  # Escribir encabezados
            for row in df.itertuples(index=False):
                writer.writerow(row)
        
        # Verificar el archivo
        file_size = os.path.getsize(output_path)
        print(f"Tamaño del archivo: {file_size} bytes")
        
        # Mostrar primeras líneas
        with open(output_path, 'r') as f:
            print("\nPrimeras 5 líneas del archivo:")
            for _ in range(5):
                print(f.readline().strip())
                
    except Exception as e:
        print(f"\nError al guardar: {str(e)}")
        print(f"Directorio existe?: {os.path.exists('../data')}")
        print(f"Permisos de directorio: {oct(os.stat('../data').st_mode)[-3:]}")