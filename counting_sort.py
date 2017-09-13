def counting_sort(v):
    maior = max(v)
    maior = maior + 1
    # frequencia
    count = [0] * maior
    for i in v:
        count[i] += 1

    idx = 0
    for i in range(len(count)):
        while 0 < count[i]:
            v[idx] = i
            idx += 1
            count[i] -= 1

    return v