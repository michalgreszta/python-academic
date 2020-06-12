liczba_w_10=0                           # potrzebujemy tej zmiennej, żeby później wpisać do niej wynik
liczba_w_dow=input("Podaj liczbe: ")    
system=int(input("Podaj system: "))

x=1
dlgDow = len(liczba_w_dow)

for i in range(dlgDow):
    b=dlgDow-(i+1)    # 'b' jest największą potęgą sumy w pierwszej iteracji

    # w tej pętli liczy się obecna potęga (x = system^b)
    while b>0:          
        x=x*system      
        b-=1

    if(ord(liczba_w_dow[i])>64):        # jeśli jest to któraś z liter od A do J, to zamienia ją na liczbę od 10-19
        a=ord(liczba_w_dow[i])-55
    else:
        a=int(liczba_w_dow[i])          # w przeciwnym razie tylko rzutuje na inta, żeby później móc przemnożyć
  
    liczba_w_10=liczba_w_10+a*x # a to jest nasz współczynnik przez który mnożymy liczbę podniesioną do potęgi
    x=1

print("W 10-tnym to jest: ", liczba_w_10)