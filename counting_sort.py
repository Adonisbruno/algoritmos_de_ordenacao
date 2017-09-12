def counting_sort(v):
    size = len(v)
    maior = max(v)

    # frequencia
    count = [0] * (maior+1)
    for i in v:
        count[i] += 1

    idx = 0
    for i in range(len(count)):
        while 0 < count[i]:
            v[idx] = i
            idx += 1
            count[i] -= 1

    return v