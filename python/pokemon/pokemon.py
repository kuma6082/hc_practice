class Pokemon:


  def __init__(self, name, type1, type2 ,hp, mp):
    self._name = name
    self._type1 = type1
    self._type2 = type2
    self._hp = hp
    self._mp = mp

  def attack(self):
    print(f"{self._name}がこうげき！")


if __name__ == "__main__":
  hitokage = Pokemon("ヒトカゲ", "ほのお", "ひこう", 100, 10)
  print(hitokage._name)
  print(hitokage._type1)
  print(hitokage._type2)
  print(hitokage._hp)
  print(hitokage._mp)
  hitokage.attack()