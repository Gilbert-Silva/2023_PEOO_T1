try: 
  n = int(input("Informe um inteiro: "))
  print(2*n)
  s = "Teste"
  print(s[n])
except ValueError:
  print("Você não digitou um número inteiro. Rode o programa novamente")
except IndexError:
  print("Não existe o caractere informado")