def caso_de_teste():
  n, m = map(int, input().split())
  #print(n)
  #print(m)
  matriz = []
  linha_de_zero = [0] * (m + 2)
  matriz.append(linha_de_zero)
  for k in range(n):
    """linha = input()
    print(linha)
    linha = linha.split()
    print(linha)
    linha = map(int, linha)
    print(linha)
    linha = list(linha)
    print(linha)
    """
    linha = list(map(int, input().split()))
    linha.insert(0, 0)
    linha.append(0)
    matriz.append(linha)
  linha_de_zero = [0] * (m + 2)
  matriz.append(linha_de_zero)
  #print(matriz)
  resultado = []
  for k in range(n+2):
    linha_de_zero = [0] * (m + 2)
    resultado.append(linha_de_zero)
  #print(resultado)
  for l in range(1, n+1):
    for c in range(1, m+1):
      #print(l, c)
      if matriz[l][c] == 1: 
        resultado[l][c] = 9
      else:
        resultado[l][c] = matriz[l-1][c] + matriz[l+1][c] + matriz[l][c-1] + matriz[l][c+1]
       
  for l in range(1, n+1):
    for c in range(1, m+1):
      print(resultado[l][c], end="")
    print()

while True:
  try:
    caso_de_teste()
  except EOFError:
    break
