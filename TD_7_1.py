import funkcje as f
import funkcje_demodulacja as f_demod
import funkcje_modulacja as f_mod
import funkcje_dekoder as f_dek
import funkcje_koder as f_kod
import numpy as np
import matplotlib.pyplot as plt






slowo = 'asdasdqai'
bity = f.na_bin(slowo)

#wydluzenie zerami dla uzyskania pelnej ramki
while len(bity)%11 != 0:
    bity.append(0)


def transmisja(metoda, bity, alfa):
    ################################## KODER ########################################
    zakodowane = f_kod.koder(bity)
    ################################## USTAWIENIE PARAMETROW ########################
    #metoda = 'ASK'
    Tc=1
    B = len(zakodowane)
    Tb = Tc/B  #czas trwania jednego bitu
    w = 2
    fn1=(w+1)/Tb
    fn2=(w+2)/Tb
    fn = w/Tb
    fs = 10*fn
    N=Tc*fs #ilosc probek
    N=int(N)
    t=[n/fs for n in range(0,N)]
    A1=1
    A2=0.5
    ################################## MODULATOR ###################################
    y, czas = f_mod.modulacja(metoda, A1,A2,fn,t, N, B, zakodowane, fn1, fn2, w)
    ################################## KANALTRANSMISYJNY ###################################
    g = np.random.uniform(0, A1*2*3, len(y))
    y = [y+alfa*g for y,g in zip(y,g)] 
    ################################## DEMODULATOR #################################
    zdemodulowane = f_demod.demodulacja(metoda, A1, A1, A2, fn, czas, N, B, y, fn1, fn2, Tb)
    ################################## DEKODER #####################################
    odebrabe_bity = f_dek.dekoder(zdemodulowane)
    ################################## BER #########################################
    return f.getBer(bity, odebrabe_bity)


alfa = [x/10 for x in range(11)]

BER = []
for a in alfa:
    BER.append(transmisja('ASK', bity, a))
print("\n")
plt.plot(alfa, BER)
plt.show()

BER = []
for a in alfa:
    BER.append(transmisja('FSK', bity, a))
print("\n")
plt.plot(alfa, BER)
plt.show()

BER = []
for a in alfa:
    BER.append(transmisja('PSK', bity, a))
print("\n")
plt.plot(alfa, BER)
plt.show()
