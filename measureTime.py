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
import operator

def saida(A):
    for i in range(len(A)):
        print A[i]

def main():
    global vetor, opt
    if len(sys.argv) < 2:
        print "python measureTime.py entrada.txt"
        print "Exemplo: python measureTime.py entrada.txt"
        sys.exit(-1)
    try:
        vetor = ler_entrada(sys.argv[1])
        #opt = sys.argv[2]
        # print vetor
    except ValueError:
        print "valores invalidos"
        sys.exit(-1)

if __name__ == "__main__":
    main()

    # primeiro elemento da lista eh o tamanho da lista
    n = vetor[0]
    # fazendo uma copia do vetor de entrada para cada algoritmo.
    SS = vetor[1:]
    IS = vetor[1:]
    HS = vetor[1:]
    QS = vetor[1:]
    MS = vetor[1:]
    CS = vetor[1:]
    RS = vetor[1:]
    # dicionario para armazenas o tempo de execucao
    tempo = {}

    # algoritmos
    start = time.time()
    selection_sort(SS)
    tempo['SS'] = (time.time() - start)*1000

    start = time.time()
    insertion_sort(IS)
    tempo['IS'] = (time.time() - start)*1000

    start = time.time()
    heapsort(HS)
    tempo['HS'] = (time.time() - start)*1000

    start = time.time()
    quickSort(QS)
    tempo['QS'] = (time.time() - start)*1000

    start = time.time()
    topDownMergeSort(MS)
    tempo['MS'] = (time.time() - start)*1000

    start = time.time()
    CS, menorValor = entrada_NegaToPosi(CS, n)    # deixa lista totalmente positiva
    CS = counting_sort(CS)
    CS = entrada_PosiToNega(CS, menorValor, n)    # retorna a lista com valores original
    tempo['CS'] = (time.time() - start)*1000

    start = time.time()
    RS, menorValor = entrada_NegaToPosi(RS, n) # deixa lista totalmente positiva
    RS = radix_sort(RS)
    RS = entrada_PosiToNega(RS, menorValor, n) # retorna a lista com valores original
    tempo['RS'] = (time.time() - start)*1000

    print "{}".format(tempo)

    plot_dicionario(tempo, n)




