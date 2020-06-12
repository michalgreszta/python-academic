def zamiana_napisu(wyraz):
    napis = ''
    for i in range(len(wyraz)):
        if ord(wyraz[i])>=97 and ord(wyraz[i])<=122:
            napis = napis + wyraz[i]
        elif ord(wyraz[i])>=65 and ord(wyraz[i])<=90:
            napis = napis + chr(ord(wyraz[i])+32)
    return napis

def szyfrowanie(napis,klucz):
    zaszyrf = ''
    j=0

    for i in range(len(napis)):
        if j >= len(klucz):                     # jeśli klucz nie został podany
            j=0

        znak = chr(ord(napis[i])+ord(klucz[j])-96)
        if ord(znak) > 122:
            znak = chr(ord(znak) - 26)
        zaszyrf = zaszyrf + znak
        j+=1
    return zaszyrf

def odszyfrowanie(napis,klucz):
    odszyfr = ''
    j=0

    for i in range(len(napis)):
        if j >= len(klucz):             
            j=0

        znak = chr(ord(napis[i]) - ord(klucz[j]) + 96)
        if ord(znak) < 97:
            znak = chr(ord(znak) + 26)
        odszyfr = odszyfr + znak
        j+=1
    return odszyfr

wyraz = input("Podaj wyraz: ")
klucz = input("Podaj klucz: ")
wyraz = zamiana_napisu(wyraz)   # zamiana wszystkich wielkich liter na małe i pozbycie się pozostałych znaków
klucz = zamiana_napisu(klucz)

zaszyfr = szyfrowanie(wyraz,klucz)
print(zaszyfr)
odszyfr = odszyfrowanie(zaszyfr,klucz)
print(odszyfr)