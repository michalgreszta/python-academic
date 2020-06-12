
def findNumbers(lista):   #szuka liczb, które *są pierwsze; *pojawiają się w liście nieparzystą ilość razy;
    locatedPrimes = []  
    for i in lista:
        prime = True
        
        if(i==1):
            prime = False
        
        for j in range(2,i):
            if (i%j == 0):
                prime = False
                break
        
        if (prime == True):
            locatedPrimes.append(i)
    #w tym miejscu kończy się szukanie liczb pierwszych    

        resultList = []
        checked = []

    for i in range(len(locatedPrimes)):
        present = locatedPrimes[i]

        if present in checked:
            continue                    #jeśli liczba była już sprawdzona, przejdź do kolejnej iteracji            
        else:
            checked.append(present)
            counter = 1

            for k in range(i+1, len(locatedPrimes)):
                if ( present == locatedPrimes[k]):
                    counter += 1
                
            if (counter%2 == 1):
                resultList.append(present)
    
    return resultList

lista = [int(x) for x in input().split()]

print(findNumbers(lista))
