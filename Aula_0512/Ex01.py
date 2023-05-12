"""print("Digite um número inteiro")
n = int(input())
for k in range(1, n+1):
  if k % 6 == 0: print(-k, end=" ")
  else: print(k, end=" ")  
"""

def primo(x):
  if x == 1: return False
  p = True
  for k in range(2, x):
    if x % k == 0: p = False
  return p
  
print(primo(1))
