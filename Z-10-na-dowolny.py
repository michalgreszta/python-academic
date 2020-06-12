
def z_10_na_dow(liczba,system):
  wynik=''                          #zmienna wynik zadeklarowana jako string
  while liczba>0:
    x=(liczba%system)
    if x>9:                                     
      x=chr(x+55)                               
    wynik=str(x)+wynik                          
    liczba=liczba//system
  return wynik

liczba=int(input("Podaj liczbe w systemie 10: "))
system=int(input("Podaj system od 2-20: "))

x=''
koniec=''

koniec=z_10_na_dow(liczba,system)
print(koniec)