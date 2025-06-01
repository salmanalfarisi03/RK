def f(x):
    return x**3 + x**2 - 3*x - 3

def df(x):
    return 3*x**2 + 2*x - 3

def newton_raphson(x0, epsilon=1e-4, max_iter=100):
    result = ["Metode Newton-Raphson:\n"]
    result.append(f"{'Iterasi':<8}{'x_n':<15}{'f(x_n)':<15}{'x_n+1':<15}{'f(x_n+1)'}")
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            result.append("Turunan nol! Tidak bisa melanjutkan.")
            return "\n".join(result)
        x1 = x0 - fx / dfx
        fx1 = f(x1)
        result.append(f"{i:<8}{x0:<15.10f}{fx:<15.10f}{x1:<15.10f}{fx1:.10f}")
        if abs(x1 - x0) < epsilon:
            result.append(f"\nKonvergen ke akar: {x1:.10f} setelah {i} iterasi\n")
            return "\n".join(result)
        x0 = x1
    result.append("\nTidak konvergen dalam jumlah iterasi maksimum.")
    return "\n".join(result)
