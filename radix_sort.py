def radix_sort(v):
    nBalde = 10
    maxSize = False
    tmp = -1
    digito = 1

    while not maxSize:
        maxSize = True
        # criando os baldes
        baldes = [list() for _ in range(nBalde)]
        # separando nos baldes
        for i in v:
            tmp = i/digito
            baldes[tmp % nBalde].append(i)
            if maxSize and tmp > 0:
                maxSize = False
        # tirando os baldes e juntando novamente
        idx2 = 0
        for i in range(nBalde):
            balde = baldes[i]
            for j in balde:
                v[idx2] = j
                idx2 += 1
        # movendo para proximo digito
        digito *= nBalde
    return v