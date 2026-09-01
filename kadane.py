def max_subarray_kadane(a):
    aqui = a[0]
    global_max = a[0]

    for i in range(1, len(a)):
        aqui = max(a[i], aqui + a[i])
        global_max = max(global_max, aqui)

    return global_max