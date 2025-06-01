def f(x):
    return x**3 + x**2 - 3*x - 3

def regula_falsi(x0, x1, epsilon=1e-4, max_iter=100):
    result = ["Metode Regula Falsi:\n"]
    result.append(f"{'Iterasi':<8}{'Xn':<15}{'Xn+1':<15}{'Xt':<15}{'f(Xt)':<20}{'f(Xn)*f(Xt)'}")
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx0 * fx1 > 0:
            result.append("f(x0) dan f(x1) tidak memiliki tanda berbeda.")
            return "\n".join(result)
        xt = x1 - (fx1 * (x0 - x1)) / (fx0 - fx1)
        fxt = f(xt)
        fx0fxt = fx0 * fxt
        result.append(f"{i:<8}{x0:<15.10f}{x1:<15.10f}{xt:<15.10f}{fxt:<20.10f}{fx0fxt:.10f}")
        if abs(fxt) < epsilon:
            result.append(f"\nKonvergen ke akar: {xt:.10f} setelah {i} iterasi\n")
            return "\n".join(result)
        if fx0fxt < 0:
            x1 = xt
        else:
            x0 = xt
    result.append("\nTidak konvergen dalam jumlah iterasi maksimum.")
    return "\n".join(result)
