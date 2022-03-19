import math 



def drugi_sygnal_domnozenia(A,fn,t):
    return A* math.sin(2*math.pi*fn*t)

def mnozenie_pierwsze(A,fn,czas,syg):
    y = []
    for i in range(len(czas)):
        y.append(drugi_sygnal_domnozenia(A,fn,czas[i]))
    x = []
    for i in range(len(syg)):
        x.append(syg[i]*y[i])
    return x

def calkowanie_ASK(N,B,x):
    p=[]
    probek_w_bicie = int(N/B)
    it=0
    for b in range(B): 
        akumulator = 0
        for i in range(probek_w_bicie):  
            akumulator += x[it]
            it += 1
            p.append(akumulator)
    return p


def komparator_ASK(p):
    c=[]
    prog=sum(p)/len(p)
    for i in range(len(p)):
        if p[i] > prog:
            c.append(1)
        else:
            c.append(0)
    
    return c
def drugi_sygnal_domnozenia(A,fn,t):
    return A* math.sin(2*math.pi*fn*t)


def calkowanie_PSK(N,B,x):
    p=[]
    probek_w_bicie = int(N/B)
    it=0
    ekstrema_lokalne=[]
    for b in range(B): 
        akumulator = 0
        for i in range(probek_w_bicie):  
            akumulator += x[it]
            it += 1
            p.append(akumulator)
        ekstrema_lokalne.append(akumulator)
    return p


def komparator_PSK(p):
    c=[]
    for i in range(len(p)):
        if p[i] < 0:
            c.append(1)
        else:
            c.append(0)
    return c
def drugi_sygnal_domnozenia(A,fn,t):
    return A* math.sin(2*math.pi*fn*t)

def mnozenie_FSK(A,fn,czas,syg):
    y = []
    for i in range(len(czas)):
        y.append(drugi_sygnal_domnozenia(A,fn,czas[i]))
    x = []
    for i in range(len(syg)):
        x.append(syg[i]*y[i])
    return x



def calkowanie_PSK(N,B,x):
    p=[]
    probek_w_bicie = int(N/B)
    it=0
    ekstrema_lokalne=[]
    for b in range(B): 
        akumulator = 0
        for i in range(probek_w_bicie):  
            akumulator += x[it]
            it += 1
            p.append(akumulator)
        ekstrema_lokalne.append(akumulator)
    return p
def komparator_FSK(p):
    c=[]
    for i in range(len(p)):
        if p[i] > 0:
            c.append(1)
        else:
            c.append(0)
    return c

def podziel_c_na_tablice_tablic(czas, Tb, tab_c):
    moment_konca_bitu = Tb   #poczatkowy
    c_naBity = []
    c_wBicie = []
    for i in range(len(czas)):
        if czas [i] > moment_konca_bitu: #gdy przekroczono interwal czasowy bitu
            #print(czas[i], moment_konca_bitu)
            moment_konca_bitu = moment_konca_bitu + Tb
            c_naBity.append(c_wBicie)
            c_wBicie = []
        c_wBicie.append(tab_c[i])
    c_naBity.append(c_wBicie)
    return c_naBity

def estymuj_bit_dla_tablicy_tablic(tab):
    for i in range(len(tab)):
        if sum(tab[i]) > (len(tab[i])-sum(tab[i])):
            wartoscBitu = 1
        else:
            wartoscBitu = 0
        for j in range(len(tab[i])):
            tab[i][j]=wartoscBitu
    return tab

def calkowanie_PSK(N,B,x):
    p=[]
    probek_w_bicie = int(N/B)
    it=0
    ekstrema_lokalne=[]
    for b in range(B): 
        akumulator = 0
        for i in range(probek_w_bicie):  
            akumulator += x[it]
            it += 1
            p.append(akumulator)
        ekstrema_lokalne.append(akumulator)
    return p
def komparator_PSK(p):
    c=[]
    for i in range(len(p)):
        if p[i] < 0:
            c.append(1)
        else:
            c.append(0)
    return c

def mnozenie_FSK(A,fn,czas,syg):
    y = []
    for i in range(len(czas)):
        y.append(drugi_sygnal_domnozenia(A,fn,czas[i]))
    x = []
    for i in range(len(syg)):
        x.append(syg[i]*y[i])
    return x
def komparator_FSK(p):
    c=[]
    for i in range(len(p)):
        if p[i] > 0:
            c.append(1)
        else:
            c.append(0)
    return c

def demodulacja_ASK(A1, A2, fn, czas, yA, N, B, Tb):
    xA = mnozenie_pierwsze(A1,fn,czas,yA)
    #calkowanie
    pA = calkowanie_ASK(N,B,xA)
    #narysowanie progu
    h=[]
    h+=len(czas)*[sum(pA)/len(pA)] 
    #komparator
    cA = komparator_ASK(pA)
    ############################# KOWNERSJA c z ASK na ciag bitow ###############################
    tab_cA = podziel_c_na_tablice_tablic(czas, Tb, cA) #tablica 2d gdzie wiersz to tablica wartosci c w okresie bitu
    tab_bA = estymuj_bit_dla_tablicy_tablic(tab_cA)    #ustalenie bitu ktory dominuje
    #zmiana z listy 2D na liste 1D
    zdemodulowane = []
    for i in range(len(tab_bA)):
        zdemodulowane.append(tab_bA[i][0])
    zdemodulowane = [int(x) for x in zdemodulowane]

    return zdemodulowane 


def demodulacja_PSK(A, fn, czas, yP, N, B, Tb):
    xP = mnozenie_pierwsze(A,fn,czas,yP)
    #calkowanie
    pP = calkowanie_PSK(N,B,xP)
    #komparator
    cP = komparator_PSK(pP)
    ############################# KOWNERSJA c z PSK na ciag bitow ###############################
    tab_cP = podziel_c_na_tablice_tablic(czas, Tb, cP) #tablica 2d gdzie wiersz to tablica wartosci c w okresie bitu
    tab_bP = estymuj_bit_dla_tablicy_tablic(tab_cP)    #ustalenie bitu ktory dominuje
    #zmiana z listy 2D na liste 1D
    zdemodulowane = []
    for i in range(len(tab_bP)):
        zdemodulowane.append(tab_bP[i][0])
    zdemodulowane = [int(x) for x in zdemodulowane]

    return zdemodulowane 




def demodulacja_FSK(A, fn1, fn2, czas, yF, N, B, Tb):
    #sygnal po mnozeniu
    xF1 = mnozenie_FSK(A,fn1,czas,yF)
    xF2 = mnozenie_FSK(A,fn2,czas,yF)
    #calkowanie
    pF1 = calkowanie_PSK(N,B,xF1)
    pF2 = calkowanie_PSK(N,B,xF2)
    #roznica
    pF = [pF1 - pF2 for pF1, pF2 in zip(pF1, pF2)]
    #komparator
    cF = komparator_FSK(pF)
    ############################# KOWNERSJA c z FSK na ciag bitow ###############################
    tab_cF = podziel_c_na_tablice_tablic(czas, Tb, cF) #tablica 2d gdzie wiersz to tablica wartosci c w okresie bitu
    tab_bF = estymuj_bit_dla_tablicy_tablic(tab_cF)    #ustalenie bitu ktory dominuje
    #zmiana z listy 2D na liste 1D
    zdemodulowane = []
    for i in range(len(tab_bF)):
        zdemodulowane.append(tab_bF[i][0])
    zdemodulowane = [int(x) for x in zdemodulowane]

    return zdemodulowane 


def demodulacja(metoda, A, A1, A2, fn, t, N, B, zakodowane, fn1, fn2, Tb):
    if metoda == 'ASK':
        return demodulacja_ASK(A1, A2, fn, t, zakodowane, N, B, Tb)
    if metoda == 'PSK':
        return demodulacja_PSK(A, fn, t, zakodowane, N, B, Tb)
    if metoda == 'FSK':
        return demodulacja_FSK(A, fn1, fn2, t, zakodowane, N, B, Tb)




