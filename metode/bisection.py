def f(x):
    return x**3 + x**2 - 3*x - 3

def bisection(a, b, epsilon=0.0001, max_iter=100):
    result = ["Metode Bisection:\n"]
    result.append(f"{'Iter':<5} {'Xn':<12} {'Xn+1':<12} {'Xt':<12} {'f(Xn)':<15} {'f(Xn+1)':<15} {'f(Xt)':<15} {'f(Xt)*f(Xn)':<20}")
    result.append("-" * 108)
    for i in range(1, max_iter + 1):
        xt = (a + b) / 2
        fa = f(a)
        fb = f(b)
        ft = f(xt)
        prod = fa * ft
        result.append(f"{i:<5} {a:<12.9f} {b:<12.9f} {xt:<12.9f} {fa:<15.9f} {fb:<15.9f} {ft:<15.9f} {prod:<20.9f}")
        if abs(ft) < epsilon or abs(b - a) < epsilon:
            result.append(f"\nAkar ditemukan: x ≈ {xt:.10f}")
            return "\n".join(result)
        if prod < 0:
            b = xt
        else:
            a = xt
    result.append("\nMaksimum iterasi tercapai tanpa konvergensi.")
    return "\n".join(result)
