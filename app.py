import streamlit as st
from metode import bisection, regulafasi, secant, newtonraphson, lelaran
from persamaan_nirlanjar import fixed_point_dynamic
import math

st.set_page_config(page_title="Metode Numerik", layout="centered")
st.title("🔍 Metode Numerik: Pencarian Akar")

# === Soal ditampilkan di bagian atas
st.markdown("""
### 📘 Soal-soal:
Berikut adalah fungsi yang digunakan dalam masing-masing metode numerik:

- **Metode Titik Tetap (Lelaran):**  
  f(x) = x² - 2x - 3  
  ➤ Contoh bentuk g(x): `(x**2 - 3)/2`

- **Metode Regula Falsi:**  
  f(x) = x³ + x² - 3x - 3

- **Metode Secant:**  
  f(x) = x³ + x² - 3x - 3

- **Metode Bagi Dua (Bisection):**  
  f(x) = x³ + x² - 3x - 3

Dengan tebakan awal:
- **x₀ = 1**, **x₁ = 2**
- **Toleransi error:** 0.000001
""")

# === Input pemilihan metode
metode = st.selectbox("Pilih Metode", [
    "Bisection", "Regula Falsi", "Secant", "Newton-Raphson", "Titik Tetap"
])

# === Input numerik
x0 = st.number_input("Masukkan x0", value=1.0)
x1 = None
if metode not in ["Titik Tetap", "Newton-Raphson"]:
    x1 = st.number_input("Masukkan x1", value=2.0)
epsilon = st.number_input("Toleransi Error (epsilon)", value=0.000001, format="%.6f")
max_iter = st.number_input("Maksimum Iterasi", value=100, step=1)

# === Input untuk metode titik tetap
if metode == "Titik Tetap":
    g_expr = st.text_input("Masukkan g(x)", value="math.sqrt(2*x + 3)")

# === Eksekusi metode saat tombol ditekan
if st.button("🔁 Jalankan"):
    st.subheader("📄 Hasil")
    if metode == "Bisection":
        result = bisection.bisection(x0, x1, epsilon, max_iter)
    elif metode == "Regula Falsi":
        result = regulafasi.regula_falsi(x0, x1, epsilon, max_iter)
    elif metode == "Secant":
        result = secant.secant_method(x0, x1, epsilon, max_iter)
    elif metode == "Newton-Raphson":
        result = newtonraphson.newton_raphson(x0, epsilon, max_iter)
    elif metode == "Titik Tetap":
        result = fixed_point_dynamic(g_expr, x0, epsilon, max_iter)
    else:
        result = "Metode tidak dikenali."
    st.text(result)
