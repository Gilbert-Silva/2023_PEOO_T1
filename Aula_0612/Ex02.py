x = []
for i in range(10):
  n = int(input())
  if n <= 0: n = 1
  x.append(n)
"""k = 0
while k < 10:
  if x[k] <= 0: x[k] = 1
  k += 1
"""  
for i in range(10): # i é o índice, x[i] é o elemento
  #print(f"X[{i}] = {x[i]}")
  print("X[" + str(i) + "] = " + str(x[i]))


  