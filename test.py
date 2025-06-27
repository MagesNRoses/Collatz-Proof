# test.py
def collatz(n):
    seq = []
    while n != 1:
        seq.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    seq.append(1)
    return seq

if __name__ == "__main__":
    print("Test Collatz básico:")
    for n in [6, 7, 9, 27]:
        print(f"n={n}: {len(collatz(n))-1} pasos: {collatz(n)}")