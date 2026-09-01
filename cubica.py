def max_subarray_cubica(a):
    n = len(a)
    mejor = float('-inf')

    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += a[k]
            if suma > mejor:
                mejor = suma

    return mejor