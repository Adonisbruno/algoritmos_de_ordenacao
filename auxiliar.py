from random import randint

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
