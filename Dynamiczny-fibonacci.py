def dynamiczny_fibonachii(n,tab):
  if n==0:
    tab[n]=0
  if n==1:
    tab[n]=1
  '''jeśli element nie został jeszcze policzony, to w tej chwili jest liczony'''
  if n not in tab:
    tab[n]=dynamiczny_fibonachii(n-1,tab)+dynamiczny_fibonachii(n-2,tab)
  return tab[n]

n=int(input("Podaj liczbe "))
tab={}
print(dynamiczny_fibonachii(n,tab))