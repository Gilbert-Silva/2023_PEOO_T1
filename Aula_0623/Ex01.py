#import aluno
from aluno import Aluno
import datetime

#import locale
#locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
                 

#a = aluno.Aluno("Gilbert")
a = Aluno("Gilbert")
print(a)

a = datetime.datetime(2023, 6, 1)
print(a)
b = datetime.datetime(2023, 6, 1, 10, 48)
print(b)
c = datetime.datetime.today()
print(c)

e = datetime.datetime.fromisoformat("2023-06-23T09:30")
print(e)

#print("Informe a data de nascimento dd/mm/aaaa")
#f = datetime.datetime.strptime(input(), "%d/%m/%Y")
#print(f)

t1 = datetime.timedelta(days=1, hours=10)
print(t1)
print(t1.days)
print(t1.seconds)
print(t1.microseconds)

a = datetime.datetime(2023, 6, 1)
hoje = datetime.datetime.today()
b = hoje - a
print(b)
print(b.days)
print(b.seconds//3600)

joao = datetime.datetime(2005, 8, 19)
dias = hoje - joao
print(dias)



