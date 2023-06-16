"""m = [ [1, 2, 3, 4] , [5, 6, 7, 8], [9, 10, 11, 12] ]
print(m)

for linha in range(3):
  for coluna in range(4):
    print(f"{m[linha][coluna]:3d}", end=" ")
  print()  
"""    
num_linhas = int(input("Qual o número de linhas? "))
num_colunas = int(input("Qual o número de colunas? "))

m = []
for k in range(num_linhas):
  m.append([0] * num_colunas)
#m[1][2] = 5
#print(m)

for linha in range(num_linhas):
  for coluna in range(num_colunas):
    print(f"{m[linha][coluna]:3d}", end=" ")
  print() 






