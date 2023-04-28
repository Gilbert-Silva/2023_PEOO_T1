print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b or a == c or a == d or b == c or b == d or c == d:
  print("Algum valor está repetido")
else:
  """
    x = [a, b, c, d]
    x.sort()
    print("Maior valor", x[3])
    print("Menor valor", x[0])
    print("Segundo maior mais segundo menor", x[1] + x[2])  
  """ 
  menor = a
  if b < menor: menor = b
  if c < menor: menor = c
  if d < menor: menor = d
  maior = a
  if b > maior: maior = b
  if c > maior: maior = c
  if d > maior: maior = d  
  print("Maior valor", maior)
  print("Menor valor", menor)    
  print("Segundo maior mais segundo menor", a+b+c+d-maior-menor)  