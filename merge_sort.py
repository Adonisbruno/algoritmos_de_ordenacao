def topDownMergeSort(vetA, n):
    #n = len(vetA)
    vetB = [0]*n
    topDownSplitMerge(vetA, 0, n, vetB)

def copyArray(vetB, first, last, vetA):
    for i in range(first, last, 1):
        vetA[i] = vetB[i]
    return vetA

def topDownMerge(vetA, first, middle, last, vetB):
    i = first
    j = middle
    for k in range(first, last, 1):
        if (i < middle) and (j >= last or vetA[i] <= vetA[j]):
            vetB[k] = vetA[i]
            i = i + 1
        else:
            vetB[k] = vetA[j]
            j = j + 1
    return vetB

def topDownSplitMerge(vetA, first, last, vetB):
    if last - first < 2:                            # if run size == 1:consider it sorted
        return
    middle = (last + first)/2                       # middle = mid point
    topDownSplitMerge(vetA, first, middle, vetB)    # split merge left  half
    topDownSplitMerge(vetA, middle, last, vetB)     # split merge right half
    topDownMerge(vetA, first, middle, last, vetB)   # merge the two half runs
    copyArray(vetB, first, last, vetA)              # copy the merged runs vetBack to vetA
