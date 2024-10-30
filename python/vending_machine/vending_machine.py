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
        self._inventory = [
            {"juice": Juice("ペプシ", 150), "stock": 5},
            {"juice": Juice("モンスター", 200), "stock": 5},
            {"juice": Juice("いろはす", 120), "stock": 5},
        ]
        self._sales = 0

    def get_stock(self, juice_name):
        for v in self._inventory:
            if v["juice"].get_name() == juice_name:
                stock = v["stock"]
                return stock
        raise ValueError("指定されたジュースは存在しません。")

    def dispense_item(self, juice_name):
        for v in self._inventory:
            if v["juice"].get_name() != juice_name:
                continue
            if v["stock"] == 0:
                raise ValueError("在庫がありません。")
            v["stock"] -= 1
            return
        raise ValueError("指定されたジュースは存在しません。")
        

    def get_sales(self):
        return self._sales

    def get_juices(self):
        juices = [v["juice"].get_name() for v in self._inventory]
        return juices

    def purchase(self, suica, juice_name):
        for v in self._inventory:
            if v["juice"].get_name() != juice_name:
                continue
            if v["stock"] == 0:
                raise ValueError("在庫がありません。購入をキャンセルされました。")
            suica.pay(v["juice"].get_price())
            self.dispense_item(juice_name)
            self._sales += v["juice"].get_price()
            return f"{juice_name}を購入しました。"
        raise ValueError("指定されたジュースは存在しません。")

    def restock(self, juice_name, quantity):
        if quantity <= 0:
            raise ValueError("在庫数は1以上の数値である必要があります。")
        for v in self._inventory:
            if v["juice"].get_name() != juice_name:
                continue
            v["stock"] += quantity
            return v["stock"]
        raise ValueError("指定されたジュースは存在しません。")

if __name__ == "__main__":
    suica = Suica()
    vm = VendingMachine()
    suica.charge(300)
    try:
        juice_name = input(f"\n下記から飲み物を選んでください\n{', '.join(vm.get_juices())}\n")
        print(f"{juice_name}の在庫はあと{vm.get_stock(juice_name)}個です。")
        message = vm.purchase(suica, juice_name)
        print(message)
        print(f"残高は{suica.get_balance()}円です。")
        print(f"{juice_name}の在庫はあと{vm.get_stock(juice_name)}個です。")
        stock = vm.restock(juice_name, 5)
        print(f"{juice_name}の在庫はあと{stock}個です。")
        print(f"売り上げは{vm.get_sales()}円です。")
    except ValueError as e:
        print("エラー:", e)
    except KeyboardInterrupt:
        print("\n窓口からシステムを終了します。")
