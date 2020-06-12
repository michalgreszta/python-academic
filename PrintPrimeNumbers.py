#author: Greszta Michal, godzina grupy: 14:00, rok I, Informatyka

import time

check = True
primes = []

start_time = time.time()

for i in range (2,1000):
  for j in range(2,i):
    if (i%j == 0):
      check = False
      break
  if (check == True):
    primes.append(i)
  else:
    check = True

print("--- %s seconds ---" % (time.time() - start_time))
#sleep(2000)

#for i in range (len(primes)):
#  print(primes[i])

