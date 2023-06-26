import datetime

print("Informe a duração da 1ª música mm:ss")
min, seg = map(int, input().split(":"))
t1 = datetime.timedelta(minutes = min, seconds = seg)
print("Informe a duração da 2ª música mm:ss")
min, seg = map(int, input().split(":"))
t2 = datetime.timedelta(minutes = min, seconds = seg)
print(f"Tempo total = {t1+t2}")
t = t1 + t2
print(f"Tempo total = {t.seconds//60:02d}:{t.seconds%60:02d}")

data = datetime.datetime(1, 1, 1)
print(data)
t = data + t1 + t2
print(t.strftime("%H:%M:%S"))

class Amigo:
  def __init__(self, nome, nasc):

    
