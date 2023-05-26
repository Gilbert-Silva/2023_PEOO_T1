class Aluno:
  def __init__(self):
    self.nome = "sem nome" 
    self.matricula = "1234"
  def __eq__(self, outro):
    return self.matricula == outro.matricula
  def __gt__(self, outro):  # if a > b
    return self.nome > outro.nome

a = Aluno()  # um aluno novo
b = Aluno()  # um aluno novo
c = a        # aluno existente
print(a)
print(b)
print(c)
a.nome = "Minora"
b.nome = "Gilbert"
print(type(a))
print(type(b))
print(type(c))
print(a.nome, a.matricula)
print(b.nome, b.matricula)
print(c.nome, c.matricula)
print(id(a))
print(id(b))
print(id(c))
print(a == b)
print(a == c)

x = 5
y = 5
print(type(x))
print(x + x)
print(x == y)
print(id(x))
print(id(y))

w = [20, 10, 5, 30]
w.sort()
for num in w:
  print(num)

diario = [a, b]
diario.sort()
for aluno in diario:
  print(aluno.nome)
  



