class Suica:
    def __init__(self, initial_balance=500):
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def charge(self, amount):
        if amount < 100:
            raise ValueError("チャージできるのは100円以上からです。")
        self._balance += amount
        return self._balance

    def pay(self, amount):
        if self._balance < amount:
            raise ValueError("残高が足りません。チャージしてください")
        self._balance -= amount
        return self._balance


class Juice:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


class VendingMachine:
    def __init__(self):
        self._inventory = {
            "ペプシ": {"juice": Juice("ペプシ", 150), "stock": 5},
            "モンスター": {"juice": Juice("モンスター", 200), "stock": 5},
            "いろはす": {"juice": Juice("いろはす", 120), "stock": 5},
        }
        self._sales = 0

    def get_stock(self, juice_name):
        if juice_name not in self._inventory:
            raise ValueError("持っている在庫がありません。")
        return self._inventory[juice_name]["stock"]

    def dispense_item(self, juice_name):
        if self._inventory[juice_name]["stock"] <= 0:
            raise ValueError("在庫がありません。")
        self._inventory[juice_name]["stock"] -= 1

    def get_sales(self):
        return self._sales

    def get_juices(self):
        return list(self._inventory.keys())

    def purchase(self, suica, juice_name):
        if juice_name not in self._inventory:
            raise ValueError("指定されたジュースは存在しません。")

        juice = self._inventory[juice_name]["juice"]
        if self._inventory[juice_name]["stock"] <= 0:
            raise ValueError("在庫がありません。購入はキャンセルされました。")

        suica.pay(juice.get_price())
        self.dispense_item(juice_name)
        self._sales += juice.get_price()
        return f"{juice_name}を購入しました。"

    def restock(self, juice_name, quantity):
        if juice_name not in self._inventory:
            raise ValueError("指定したジュースは存在しません。")

        if quantity <= 0:
            raise ValueError("在庫数は1以上の数値である必要があります。")

        self._inventory[juice_name]["stock"] += quantity
        return self.get_stock(juice_name)


if __name__ == "__main__":
    suica = Suica()
    vm = VendingMachine()
    try:
        juice_name = input(f"\n下記から飲み物を選んでください\n{', '.join(vm.get_juices())}\n")
        print(f"{juice_name}の在庫はあと{vm.get_stock(juice_name)}個です。")
        message = vm.purchase(suica, juice_name)
        print(message)
        print(f"残高は{suica.get_balance()}円です。")
        print(f"{juice_name}の在庫はあと{vm.get_stock(juice_name)}個です。")
        print(f"売り上げは{vm.get_sales()}円です。")
    except ValueError as e:
        print("エラー:", e)
    except KeyboardInterrupt:
        print("\n窓口からシステムを終了します。")
