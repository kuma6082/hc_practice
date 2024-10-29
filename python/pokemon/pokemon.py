from abc import ABC, abstractmethod

class Pokemon(ABC):

  def __init__(self, name, type1, type2, hp, mp):
    self.__name = name
    self.__type1 = type1
    self.__type2 = type2
    self._hp = hp
    self._mp = mp
  
  def change_name(self, new_name):
    if new_name == "うんこ":
      print("不適切な名前です。")
      return
    self.__name = new_name
  
  def get_status(self):
    status_txt = f"名前:{self.__name}\nタイプ１:{self.__type1}\nタイプ２:{self.__type2}\nHP:{self._hp}\nMP:{self._mp}\n"
    print(status_txt)
  
  @property
  def name(self):
    return self.__name
  
  @property
  def type1(self):
    return self.__type1
  
  @property
  def type2(self):
    return self.__type2
  
  @abstractmethod
  def attack(self):
      pass

class Pika(Pokemon):
    def __init__(self, name, type1, type2, hp, mp):
        super().__init__(name, type1, type2, hp, mp)

    # attack メソッドのオーバーライド
    def attack(self):
        print(f"{self.name} の10万ボルト!")


class kamex(Pokemon):
    def __init__(self, name, type1, type2, hp, mp):
        super().__init__(name, type1, type2, hp, mp)

    # attack メソッドのオーバーライド
    def attack(self):
        print(f"{self.name} のつなみ!")


if __name__ == "__main__":
  pikachu = Pika("ピカチュウ", "でんき", None, 100, 10)
  pikachu.attack()
  pikachu.change_name("うんこ")
  pikachu.attack()
  pikachu.get_status()

  pikachu = kamex("カメックス", "みず", None, 200, 20)
  pikachu.attack()