import os

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

os.makedirs('../data', exist_ok=True)

results = []
for n in range(1, 101):
    print(f"Procesando n={n}")  # Debug
    seq = collatz_sequence(n)
    steps = len(seq) - 1
    max_val = max(seq)
    results.append((n, steps, max_val))

# Guardar sin pandas
with open('../data/debug_collatz.csv', 'w') as f:
    f.write("n,steps,max_value\n")
    for n, steps, max_val in results:
        f.write(f"{n},{steps},{max_val}\n")
        
print("¡Datos guardados en data/debug_collatz.csv!")
