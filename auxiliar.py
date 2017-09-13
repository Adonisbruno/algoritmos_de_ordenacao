from random import randint
import matplotlib.pyplot as plt

def vector_random(size, start, stop):
    v = []
    for a in range(1, size, 1):
        v.append(randint(start,stop))
    return v

def ler_entrada(filename):
    arquivo = open(filename,"r")
    linhas = arquivo.read()
    arquivo.close()
    vetor = map(int, linhas.split())
    return vetor

def entrada_NegaToPosi(vetor,n):
    menorValor = abs(min(vetor))
    saida = [0 for _ in range(n)]
    for i in range(n):
        saida[i] = vetor[i] + menorValor
    return saida, menorValor

def entrada_PosiToNega(vetor, menorValor, n):
    saida = [0 for _ in range(n)]
    for i in range(n):
        saida[i] = vetor[i] - menorValor
    return saida

def plot_dicionario(D, n):
    plt.bar(range(len(D)), D.values(), align='center')
    plt.xticks(range(len(D)), D.keys())
    plt.ylabel("ms")
    plt.grid(True)
    plt.title("Para %d amostras" % n)
    plt.show()
