from auxiliar import *
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import topDownMergeSort
from quick_sort import quickSort
from heapsort import heapsort
from counting_sort import counting_sort
from radix_sort import radix_sort
import sys
import time


def saida(A):
    for i in range(len(A)):
        print A[i]

def main():
    global vetor, opt
    if len(sys.argv) < 3:
        print "python main.py entrada.txt SS|IS|HS|MS|QS|CS|RS > saida.txt"
        print "Exemplo: python main.py entrada.txt IS > saida.txt"
        sys.exit(-1)
    try:
        vetor = ler_entrada(sys.argv[1])
        opt = sys.argv[2]
        #print vetor
    except ValueError:
        print "valores invalidos"
        sys.exit(-1)


if __name__ == "__main__":
    main()

    A = vetor[1:]
    # primeiro elemento da lista eh o tamanho da lista
    n = vetor[0]

    if opt == 'SS':
        saida(selection_sort(A))
    if opt == 'IS':
        saida(insertion_sort(A))
    if opt == 'HS':
        saida(heapsort(A))
    if opt == 'MS':
        saida(topDownMergeSort(A))
    if opt == 'QS':
        saida(quickSort(A))
    if opt == 'CS':
        saida(counting_sort(A))
    if opt == 'RS':
        saida(radix_sort(A))








    
