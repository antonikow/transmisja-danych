import numpy as np

def zakoduj(b):
    n = 15
    k = len(b)
    m = 4
    
    #obliczenie P
    #indeksy bitow parzystosci
    pairIdx = np.array([1, 2, 4, 8])-1
    notPairIdx = np.array([x for x in range(n)])
    for ind in pairIdx:
        notPairIdx = notPairIdx[notPairIdx != ind]
    P = np.array([[0,0,0,1],
                  [0,0,1,0],
                  [0,0,1,1],
                  [0,1,0,0],
                  [0,1,0,1],
                  [0,1,1,0],
                  [0,1,1,1],
                  [1,0,0,0],
                  [1,0,0,1],
                  [1,0,1,0],
                  [1,0,1,1],
                  [1,1,0,0],
                  [1,1,0,1],
                  [1,1,1,0],
                  [1,1,1,1]
                 ])

    P = P[notPairIdx]
    Ik = np.eye(k,k)
    G = np.concatenate((P, Ik), axis=1)
    #wektor slowa kodowego
    c = np.dot(b, G) %2

    return c

def koder(b):
    zakodowane = []
    pocz = 0
    kon = 11
    for i in range(len(b)//11):
        zakodowane= zakodowane +(list(zakoduj(b[pocz:kon])))
        pocz += 11
        kon += 11
    return zakodowane