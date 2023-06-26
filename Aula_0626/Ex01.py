import datetime

agora = datetime.datetime.today()
print(agora)

inicio = datetime.datetime(2023, 6, 26, 12, 0, 0)
print(inicio)

#print("informe uma data com horário")
#valor = input()
#data = datetime.datetime.strptime(valor, "%d/%m/%Y %H:%M")
#print(data)

intervalo = datetime.timedelta(minutes=10, seconds=30)
print(intervalo)
print("informe um intervalo no formato mm:ss")
t1 = input().split(":")
print(t1)
t2 = datetime.timedelta(minutes=int(t1[0]), seconds=int(t1[1]))
print(t2)
min, seg = map(int, input().split(":"))
t3 = datetime.timedelta(minutes = min, seconds = seg)
print(t3)







