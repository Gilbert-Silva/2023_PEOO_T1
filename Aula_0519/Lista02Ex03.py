class Viagem:
  def __init__(self, d, t):
    self.__distancia = 0
    self.__tempo = 0
    self.set_distancia(d)
    self.set_tempo(t)
  def set_distancia(self, d):
    if d >= 0: self.__distancia = d
    else: raise ValueError()  
  def set_tempo(self, t):
    if t >= 0: self.__tempo = t
    else: raise ValueError() 
  def get_distancia(self):
    return self.__distancia
  def get_tempo(self):
    return self.__tempo
  def velocidade_media(self):
    if self.__tempo == 0: return 0
    return self.__distancia / self.__tempo
  def __str__(self):
    return f"Distância = {self.__distancia} km - Tempo = {self.__tempo} h"

class UI:
  @staticmethod
  def main():
    print("Informe a distância da sua viagem em km")
    distancia = float(input())
    print("Informe o tempo gasto na viagem em hh:mm")
    tempo = input()
    horas, minutos = map(int, tempo.split(':'))
    tempo = horas + minutos/60
    #v = Viagem()
    #v.set_distancia(distancia)
    #v.set_tempo(tempo)
    v = Viagem(distancia, tempo)
    print(f"{v.get_distancia()} km")
    print(f"{v.get_tempo()} h")
    print(f"{v.velocidade_media():.1f} km/h")
    print(v)
    
    

UI.main()


def calc_media(self):
  return (2 * n1 ...)/10

def calc_media_final():
  media_parcial = self.calc_media()
  if media_parcial < 60:
    return (media_parcial + self.__provafinal)/2
  else:
    return media_parcial

