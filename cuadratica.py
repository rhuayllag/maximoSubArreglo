def max_subarray_cuadratica(a):
    n = len(a)
    mejor = float('-inf')

    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += a[j]
            if suma > mejor:
                mejor = suma

    return mejor