def na_bin(napis ): #string

    ascii_numery = [ord(litera) for litera in napis]

    ascii_bin = []
    for liczba in ascii_numery:
        znak_bin = ''
        for i in range(7):
            if liczba & 1:
                znak_bin += '1'
            else:
                znak_bin += '0'
            liczba = liczba >> 1
        znak_bin = znak_bin[::-1]
        ascii_bin.append(znak_bin)
    
    napis_binarnie = ''.join(ascii_bin) #string
    bity = [int(znak) for znak in napis_binarnie] # lista int
    return bity # lista int

def getBer(zakodowane, odkodowane):
    ilosc = len(zakodowane)
    nierowne = 0
    for i in range(ilosc):
        if zakodowane[i] != odkodowane[i]:
            nierowne += 1
    return nierowne/ilosc


def czyRowne(zakodowane, odkodowane):
    ilosc = len(zakodowane)
    rowne = True
    for i in range(ilosc):
        if zakodowane[i] != odkodowane[i]:
            rowne = False
            break
    return rowne








