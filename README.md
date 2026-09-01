# Informe: Comparación de algoritmos de máximo subarreglo

## 1. Entorno de medición

| Ítem | Detalle |
|---|---|
| Lenguaje | Python 3.14.7 |
| Sistema operativo | Windows 11 25H2 |
| Procesador | AMD Ryzen 5 5500H 4 Nucleos / 8 Hilos 3.30GHz |
| Memoria RAM | 16 GB DDR4 3200MT/s |

> Estos datos no pueden inferirse desde el código ni desde la salida de consola; complétalos con la información real de tu equipo (en PowerShell: `Get-ComputerInfo` o revisando "Configuración → Sistema → Acerca de").

## 2. Tiempos medidos

Los siguientes tiempos se obtuvieron ejecutando `main.py` con arreglos aleatorios de enteros en `[-100, 100]`, usando `time.perf_counter()`.

| n | Cúbica O(n³) | Cuadrática O(n²) | Kadane O(n) |
|---:|---:|---:|---:|
| 1000 | 5.777233 s | 0.024904 s | 0.000100 s |
| 2000 | 47.104218 s | 0.096780 s | 0.000197 s |
| 4000 | 388.447199 s | 0.385860 s | 0.000397 s |
| 8000 | **≈ 3185 s (~53 min)** *(estimado, no medido)* | **≈ 1.52 s** *(estimado)* | **≈ 0.0008 s** *(estimado)* |

Para n = 8000 no se ejecutó realmente la versión cúbica (tardaría casi una hora), por lo que su tiempo es una **suposición** obtenida por extrapolación (ver sección 3).

## 3. Cómo se hizo la predicción para n = 8000

Con los tres tiempos medidos (n = 1000, 2000, 4000) se calculó el exponente empírico de crecimiento ajustando:

t(n) = c · n^k  →  k = log(t(4000)/t(1000)) / log(4000/1000)

| Algoritmo | Exponente empírico k | Exponente teórico | Predicción n=8000 |
|---|---:|---:|---:|
| Cúbica | 3.04 | 3 | 3185 s (~53 min) |
| Cuadrática | 1.98 | 2 | 1.52 s |
| Kadane | 0.995 | 1 | 0.0008 s |

**Comparación predicho vs. medido:** el exponente calculado a partir de los datos medidos coincide, en los tres casos, con la complejidad teórica del algoritmo (3, 2 y 1 respectivamente), con un error menor al 4%. Esto valida el modelo y da confianza en usarlo para extrapolar a n = 8000 y a n = 10⁸: no se necesitó "adivinar" la predicción, se dedujo de las propias mediciones.

## 4. Estimación para n = 10⁸

Usando el mismo modelo t(n) = c · n^k con la constante c calculada a partir del tiempo medido en n = 4000:

| Algoritmo | Tiempo estimado en n = 10⁸ | ¿Termina en menos de 1 minuto? |
|---|---|---|
| Cúbica O(n³) | ≈ 8.7 × 10¹⁵ s ≈ 276 millones de años |  No, ni remotamente |
| Cuadrática O(n²) | ≈ 1.9 × 10⁸ s ≈ 6 años |  No |
| Kadane O(n) | ≈ 9.4 s |  **Sí** |

Solo **Kadane** logra procesar un arreglo de 100 millones de elementos en menos de un minuto. Esto es consistente con su complejidad lineal: el tiempo por elemento medido (~9.9 × 10⁻⁸ s/elemento) se mantiene prácticamente constante entre n = 1000 y n = 4000, así que escalarlo linealmente a 10⁸ elementos es razonable.

Para cuadrática y cúbica, el crecimiento no lineal (n² y n³) hace que el tiempo se dispare de forma completamente impráctica mucho antes de llegar a 10⁸: la cuadrática ya tarda años, y la cúbica tarda un tiempo mayor que la edad de los dinosaurios.

## 5. Conclusiones

1. **Los tres algoritmos son correctos**: en todas las pruebas (n = 5 hasta n = 4000) los tres devuelven exactamente el mismo resultado, lo que confirma que las implementaciones cuadrática y cúbica (fuerza bruta) son equivalentes a Kadane, solo que con distinta eficiencia.
2. **La complejidad teórica se confirma empíricamente**: al duplicar n, el tiempo de la cúbica se multiplica por ~8 (2³), el de la cuadrática por ~4 (2²), y el de Kadane por ~2 (2¹). Esto es exactamente lo esperado para O(n³), O(n²) y O(n).
3. **La diferencia se vuelve crítica al escalar**: para n pequeño (decenas o cientos) cualquier algoritmo sirve, pero a partir de unos pocos miles de elementos la fuerza bruta cúbica ya es impracticable (minutos u horas), y para n = 10⁸ solo Kadane es viable en la práctica.
4. **Recomendación**: para el problema de máximo subarreglo, Kadane (O(n)) es la única opción razonable a partir de tamaños moderados de entrada; las versiones cuadrática y cúbica solo tienen valor didáctico para ilustrar la mejora de complejidad.