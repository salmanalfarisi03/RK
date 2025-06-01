import math

# Fungsi-fungsi g(x)
def g1(x):
    return math.sqrt(2 * x + 3)

def g2(x):
    return 3 / (x - 2)

def g3(x):
    return (x ** 2 - 3) / 2

# Fungsi iterasi titik tetap
def fixed_point(g, x0, epsilon=1e-5, max_iter=100, label="g(x)"):
    print(f"\nMetode Titik Tetap untuk {label}")
    print(f"{'Iterasi':<8}{'x_n':<15}{'x_n+1':<15}{'|x_n+1 - x_n|'}")
    for i in range(1, max_iter + 1):
        x1 = g(x0)
        error = abs(x1 - x0)
        print(f"{i:<8}{x0:<15.10f}{x1:<15.10f}{error:.10f}")
        if error < epsilon:
            print(f"\nKonvergen ke akar: {x1:.10f} setelah {i} iterasi\n")
            return x1
        x0 = x1
    print("\nTidak konvergen dalam jumlah iterasi maksimum.\n")
    return None

# Jalankan ketiga metode
fixed_point(g1, x0=1, label="g1(x) = sqrt(2x + 3)")
fixed_point(g2, x0=1.5, label="g2(x) = 3 / (x - 2)")
fixed_point(g3, x0=1, label="g3(x) = (x^2 - 3)/2")
