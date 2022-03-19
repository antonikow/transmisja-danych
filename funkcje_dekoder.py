import numpy as np

def dekoduj(c):
    n = 15
    k = 11
    m = 4
    
    #obliczenie P
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
    
    H = np.concatenate((np.eye(n-k),P.T),axis = 1)
    np.dot(c, H.T)
    #wektor syndromu
    s = np.dot(c, H.T) % 2
    #obliczenie S
    S = 0
    it = 0
    for para in pairIdx+1:
        S += s[it]*para
        it += 1
    
    return int(S)

def dekoder(zdemodulowane):
    odebrane_bity = []
    pocz = 4
    kon = 15
    for i in range(len(zdemodulowane)//15):
        odebrane_bity = odebrane_bity + zdemodulowane[pocz:kon]
        pocz += 15
        kon += 15
    return odebrane_bity