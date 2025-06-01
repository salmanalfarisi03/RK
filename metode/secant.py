def f(x):
    return x**3 + x**2 - 3*x - 3

def secant_method(x0, x1, epsilon=1e-6, max_iter=100):
    result = ["Metode Secant:\n"]
    result.append(f"{'Iterasi':<8}{'x0':<15}{'x1':<15}{'f(x0)':<15}{'f(x1)':<15}{'x2':<15}{'Error'}")
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            result.append("Pembagi nol. Metode berhenti.")
            return "\n".join(result)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)
        result.append(f"{i:<8}{x0:<15.9f}{x1:<15.9f}{fx0:<15.9f}{fx1:<15.9f}{x2:<15.9f}{error}")
        if error < epsilon:
            result.append(f"\nKonvergen ke akar: {x2:.9f} setelah {i} iterasi\n")
            return "\n".join(result)
        x0, x1 = x1, x2
    result.append("\nTidak konvergen dalam jumlah iterasi maksimum.")
    return "\n".join(result)
