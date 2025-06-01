import tkinter as tk
from tkinter import ttk, messagebox
import math

# Fungsi f(x) dan turunannya
def f(x):
    return x**3 + x**2 - 3*x - 3

def df(x):
    return 3*x**2 + 2*x - 3

# Metode Secant
def secant_method_gui(x0, x1, epsilon=1e-6, max_iter=100):
    result = ["Metode Secant:\n"]
    result.append(f"{'Iterasi':<8}{'x0':<12}{'x1':<12}{'f(x0)':<12}{'f(x1)':<12}{'x2':<12}{'Error':<12}")
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            return "Pembagi nol. Metode tidak dapat dilanjutkan."
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)
        result.append(f"{i:<8}{x0:<12.6f}{x1:<12.6f}{fx0:<12.6f}{fx1:<12.6f}{x2:<12.6f}{error:<12.6f}")
        if error < epsilon:
            result.append(f"\nKonvergen ke akar: {x2:.6f} setelah {i} iterasi")
            break
        x0, x1 = x1, x2
    return "\n".join(result)

# Metode Bisection
def bisection_method(a, b, epsilon=1e-6, max_iter=100):
    result = ["Metode Bisection:\n"]
    for i in range(1, max_iter + 1):
        xt = (a + b) / 2
        fa, fb, ft = f(a), f(b), f(xt)
        result.append(f"Iterasi {i}: xt = {xt:.6f}, f(xt) = {ft:.6f}")
        if abs(ft) < epsilon or abs(b - a) < epsilon:
            result.append(f"\nKonvergen ke akar: {xt:.6f}")
            return "\n".join(result)
        if fa * ft < 0:
            b = xt
        else:
            a = xt
    return "\n".join(result) + "\nTidak konvergen."

# Metode Regula Falsi
def regula_falsi_method(x0, x1, epsilon=1e-6, max_iter=100):
    result = ["Metode Regula Falsi:\n"]
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx0 * fx1 > 0:
            return "f(x0) dan f(x1) tidak memiliki tanda berbeda."
        xt = x1 - (fx1 * (x0 - x1)) / (fx0 - fx1)
        fxt = f(xt)
        result.append(f"Iterasi {i}: xt = {xt:.6f}, f(xt) = {fxt:.6f}")
        if abs(fxt) < epsilon:
            result.append(f"\nKonvergen ke akar: {xt:.6f} setelah {i} iterasi")
            return "\n".join(result)
        if fx0 * fxt < 0:
            x1 = xt
        else:
            x0 = xt
    return "\n".join(result) + "\nTidak konvergen."

# Metode Newton-Raphson
def newton_raphson_method(x0, epsilon=1e-6, max_iter=100):
    result = ["Metode Newton-Raphson:\n"]
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            return "Turunan nol. Metode tidak dapat dilanjutkan."
        x1 = x0 - fx / dfx
        result.append(f"Iterasi {i}: x = {x0:.6f}, f(x) = {fx:.6f}, x_next = {x1:.6f}")
        if abs(x1 - x0) < epsilon:
            result.append(f"\nKonvergen ke akar: {x1:.6f} setelah {i} iterasi")
            return "\n".join(result)
        x0 = x1
    return "\n".join(result) + "\nTidak konvergen."

# Metode Titik Tetap dari ekspresi string
def fixed_point_dynamic(g_expr, x0, epsilon=1e-6, max_iter=100):
    result = [f"\nMetode Titik Tetap untuk g(x) = {g_expr}:\n"]
    result.append(f"{'Iterasi':<8}{'x_n':<15}{'x_n+1':<15}{'|x_n+1 - x_n|'}")

    def g(x):
        return eval(g_expr, {"x": x, "math": math})

    for i in range(1, max_iter + 1):
        try:
            x1 = g(x0)
        except Exception as e:
            return f"❌ Error evaluasi g(x): {e}"
        error = abs(x1 - x0)
        result.append(f"{i:<8}{x0:<15.6f}{x1:<15.6f}{error:<.6f}")
        if error < epsilon:
            result.append(f"\n✅ Konvergen ke akar: {x1:.6f} setelah {i} iterasi\n")
            return "\n".join(result)
        x0 = x1
    result.append("\n⚠️ Tidak konvergen dalam jumlah iterasi maksimum.\n")
    return "\n".join(result)