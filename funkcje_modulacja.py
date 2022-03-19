import math

def zA(A1, A2, fn, t, N, B, b):
    yA=[]
    it = 0
    probek_w_bicie = int(N/B)
    for n in range(B): 
        if b[n] == 1:
            for pomiar_nr in range(probek_w_bicie):  
                yA.append(A1*math.sin(2*math.pi*fn*t[it + pomiar_nr]))
            it += probek_w_bicie
        elif b[n] == 0:
            for pomiar_nr in range(probek_w_bicie):  
                yA.append(A2*math.sin(2*math.pi*fn*t[it + pomiar_nr]))
            it += probek_w_bicie
    czas = [x/len(yA) for x in range(len(yA))]
    return yA, czas

def zP(powiekszenie,fn, t, N, B, b):
    yP=[]
    it = 0
    probek_w_bicie = int(N/B)
    for n in range(B): 
        if b[n] == 1:
            for pomiar_nr in range(probek_w_bicie):  
                yP.append(math.sin(2*math.pi*fn*t[it + pomiar_nr]+ powiekszenie))
            it += probek_w_bicie
        elif b[n] == 0:
            for pomiar_nr in range(probek_w_bicie):  
                yP.append(math.sin(2*math.pi*fn*t[it + pomiar_nr] ))
            it += probek_w_bicie
    
    czas = [x/len(yP) for x in range(len(yP))]
    return yP, czas


def zF(fn1,fn2, t, N, B, b):
    yF=[]
    it = 0
    probek_w_bicie = int(N/B)
    for n in range(B): 
        if b[n] == 1:
            for pomiar_nr in range(probek_w_bicie):  
                yF.append(math.sin(2*math.pi*fn1*t[it + pomiar_nr]))
            it += probek_w_bicie
        elif b[n] == 0:
            for pomiar_nr in range(probek_w_bicie):  
                yF.append(math.sin(2*math.pi*fn2*t[it + pomiar_nr] ))
            it += probek_w_bicie
    
    czas = [x/len(yF) for x in range(len(yF))]
    return yF, czas




def modulacja(metoda, A1,A2,fn,t, N, B, zakodowane, fn1, fn2, w):
    if metoda == 'ASK':
        return zA(A1, A2, fn, t, N, B, zakodowane)
    if metoda == 'PSK':
        return zP(w, fn, t, N, B, zakodowane)
    if metoda == 'FSK':
        return zF(fn1, fn2, t, N, B, zakodowane)



