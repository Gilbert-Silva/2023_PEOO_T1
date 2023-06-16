num_linhas = 12
num_colunas = 12

# Iniciar a matriz m com num_linhas x num_colunas
m = []                          # m inicia vazio
for k in range(num_linhas):     # para cada uma das num_linhas linha de m
  m.append([0] * num_colunas)   # adiciona uma linha com num_colunas elementos

op = input()

# Ler os valores dos elementos da matriz
for linha in range(num_linhas):
  for coluna in range(num_colunas):
    m[linha][coluna] = float(input())

s = 0 # soma dos elementos
n = 1 # quantidade de elementos
for linha in range(num_linhas):     # pega cada linha
  for coluna in range(num_colunas): # pega cada coluna
    if coluna > linha:              # testa se está acima da diagonal prin.
      s += m[linha][coluna]         # soma o elemento
      n += 1                        # conta o elemento

if op == "S": print(f"{s:.1f}")
else: print(f"{s/n:.1f}")  

#print(m)





