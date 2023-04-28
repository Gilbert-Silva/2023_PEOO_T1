def formatar_nome(nome):
  s = nome.lower()
  palavras = s.split()
  resultado = ""
  for palavra in palavras:
    if palavra != "da" and palavra != "de" and palavra != "do" and palavra != "das" and palavra != "dos" and palavra != "e":
      resultado += palavra[0].upper() + palavra[1:] + " "
    else:
      resultado += palavra + " "
  return resultado

print("Digite seu nome")
s = input()
print(formatar_nome(s))


"""print("Digite seu nome")
s = input().lower()
palavras = s.split()
resultado = ""
for palavra in palavras:
  if palavra != "da" and palavra != "de" and palavra != "do" and palavra != "das" and palavra != "dos" and palavra != "e":
    resultado += palavra[0].upper() + palavra[1:] + " "
  else:
    resultado += palavra + " "
print(resultado)"""  

