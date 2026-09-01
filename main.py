import time
import random

from cuadratica import max_subarray_cuadratica
from cubica import max_subarray_cubica
from kadane import max_subarray_kadane


def medir_tiempo(func, a):
    inicio = time.perf_counter()
    resultado = func(a)
    fin = time.perf_counter()
    return resultado, fin - inicio


def probar_caso(nombre, a):
    print(f"\n=== Caso: {nombre} ===")
    print(f"Arreglo: {a if len(a) <= 15 else str(a[:15])[:-1] + ', ...]'}")

    r1, t1 = medir_tiempo(max_subarray_cuadratica, a)
    r2, t2 = medir_tiempo(max_subarray_cubica, a)
    r3, t3 = medir_tiempo(max_subarray_kadane, a)

    print(f"Cúbica    -> resultado: {r2}  tiempo: {t2:.6f}s")
    print(f"Cuadrática-> resultado: {r1}  tiempo: {t1:.6f}s")
    print(f"Kadane    -> resultado: {r3}  tiempo: {t3:.6f}s")

    if r1 == r2 == r3:
        print("Los tres resultados coinciden.")
    else:
        print("¡Los resultados NO coinciden!")


def main():
    # Casos de prueba fijos
    casos_fijos = [
        ("Todos positivos", [1, 2, 3, 4, 5]),
        ("Todos negativos", [-3, -1, -7, -2]),
        ("Mezcla clásica", [-2, 1, -3, 4, -1, 2, 1, -5, 4]),
        ("Un solo elemento", [5]),
        ("Ceros y negativos", [0, -1, 0, -2, 0]),
    ]

    for nombre, a in casos_fijos:
        probar_caso(nombre, a)

    # Caso aleatorio pequeño
    random.seed(42)
    a_pequeno = [random.randint(-50, 50) for _ in range(200)]
    probar_caso("Aleatorio pequeño (n=200)", a_pequeno)

    # Casos aleatorios grandes 1000, 2000, 4000, 8000
    print("\n=== Casos: Aleatorios grandes ===")
    for n in (1000, 2000, 4000, 8000):
        a_grande = [random.randint(-100, 100) for _ in range(n)]

        r1, t1 = medir_tiempo(max_subarray_cuadratica, a_grande)
        r2, t2 = medir_tiempo(max_subarray_cubica, a_grande)
        r3, t3 = medir_tiempo(max_subarray_kadane, a_grande)

        print(f"\n--- n = {n} ---")
        print(f"Cúbica    -> resultado: {r2}  tiempo: {t2:.6f}s")
        print(f"Cuadrática-> resultado: {r1}  tiempo: {t1:.6f}s")
        print(f"Kadane    -> resultado: {r3}  tiempo: {t3:.6f}s")
        print("Coinciden." if r1 == r2 == r3 else "¡No coinciden!")


if __name__ == "__main__":
    main()