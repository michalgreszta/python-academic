# chr(int) --> zwraca znak; ord(c) --> zwraca liczbę z tablicy ASCII
def zamiana_napisu(wyraz):       # usuwa wszystkie znaki nie będące literami, oraz zmienia wszystkie litery na małe
    napis = ''
    for i in range(len(wyraz)):
        if ord(wyraz[i])>=97 and ord(wyraz[i])<=122: # znak jest małą literą
            napis = napis + wyraz[i]                 # po prostu dodaj go do napisu
        elif ord(wyraz[i])>=65 and ord(wyraz[i])<=90:# znak jest wielką literą
            napis = napis + chr(ord(wyraz[i])+32)    # do liczbowego reprezentanta dodaj 32 - wówcza z wielkiej litery
    return napis                                     # uzyskasz małą

def cezar(napis,przesuniecie):                  #metoda, która pracuje TYLKO na małych znakach
    zakod = ''
    if przesuniecie >= 26:
        przesuniecie = przesuniecie % 26
    for i in range(len(napis)):
        znak=chr(ord(napis[i])+przesuniecie)
        if ord(znak)>122:                   # jeśli znajdujemy się poza alfabetem (poza 'z' małym)
            znak = chr(ord(znak)-26)
        zakod=zakod+znak
    return zakod

def brutus(zakod,klucz):
    odszyfr = ''
    if klucz >= 26:
        klucz = klucz % 26
    for i in range(len(zakod)):
        znak=chr(ord(zakod[i])-klucz)
        if ord(znak)<97:
            znak = chr(ord(znak)+26)
        odszyfr=odszyfr+znak
    return odszyfr

wyraz = input("Podaj znak ")
klucz = int(input("Podaj przesuniecie "))
napis = zamiana_napisu(wyraz)
zakod = cezar(napis,klucz)
odszyfr = brutus(zakod,klucz)
print(zakod)
print(odszyfr)