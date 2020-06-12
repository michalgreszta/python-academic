import random

def zamiana_napisu(wyraz):
    napis = ''
    for i in range(len(wyraz)):
        if ord(wyraz[i])>=97 and ord(wyraz[i])<=122:
            napis = napis + wyraz[i]
        elif ord(wyraz[i])>=65 and ord(wyraz[i])<=90:
            napis = napis + chr(ord(wyraz[i])+32)
    return napis

def szyfrowanie(wyraz,slownik):      #działa sobie tylko na małych literkach
    zakod = ''
    for i in range(len(napis)):         # każdej małej literce
        znak = slownik[wyraz[i]]        # program przypisuje jej odpowiednik ze słownika
        zakod = zakod + znak            # i ten odpowiednik dodaje do całego stringa
    return zakod                        # i zwraca zakodowany napis

a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(k)    # metoda, która przetasowuje elementy listy   

slownik={a[0]:k[0],a[1]:k[1],a[2]:k[2],a[3]:k[3],a[4]:k[4],a[5]:k[5],a[6]:k[6],a[7]:k[7],a[8]:k[8],a[9]:k[9],a[10]:k[10],a[11]:k[11],a[12]:k[12],a[13]:k[13],a[14]:k[14],a[15]:k[15],a[16]:k[16],a[17]:k[17],a[18]:k[18],a[19]:k[19],a[20]:k[20],a[21]:k[21],a[22]:k[22],a[23]:k[23],a[24]:k[24],a[25]:k[25]}
wyraz = input("Podaj znak: ")
napis = zamiana_napisu(wyraz)

zakod = szyfrowanie(napis,slownik)
print(zakod)