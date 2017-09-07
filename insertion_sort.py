def insertion_sort(vetA):
    curr = 0
    flag = 0
    size = len(vetA)
    for i in range(1, size, 1):
        curr = vetA[i]
        flag = i - 1
        while flag >= 0 and curr < vetA[flag]:
            vetA[flag+1] = vetA[flag]
            flag = flag - 1
        vetA[flag+1] = curr
    return vetA

