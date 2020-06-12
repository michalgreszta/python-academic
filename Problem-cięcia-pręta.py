def Max(a,b):
  if a>b:
    return a
  else:
    return b

def ciecie_preta(dlg,cennik):
  zysk=[]

  '''wypełnia tablicę 'zysk' zerami dlg+1 razy'''
  for i in range(dlg+1):
    zysk.append(0)

  if dlg==0:
    zysk[0]=0;
  else:
    '''pętla wykonująca się dla każdej długości w zakresie [1, podanej]'''
    for i in range(1,dlg+1):
      '''zakłada, że obecnie największy zysk to -1'''
      max=-1
      '''sprawdza, z jakiego podziału danej długości jest największy zysk'''
      for j in range(i):
        max=Max(max, cennik[j]+zysk[i-(j+1)])
        zysk[i]=max
  return zysk[dlg]      

dlugosc=int(input("Podaj dlugosc preta "))
cennik=[1,5,8,9,10,16,17,20,24,26]
print(ciecie_preta(dlugosc,cennik))