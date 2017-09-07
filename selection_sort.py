def selection_sort(vet):
    aux = 0
    for i in range(0, len(vet)):
        menor = i

        for k in range(i, len(vet)):
            if vet[k] < vet[menor]:
                menor = k

        if menor != i:
            aux = vet[i]
            vet[i] = vet[menor]
            vet[menor] = aux
    return vet
