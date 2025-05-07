from abc import ABC, abstractmethod

# 抽象主题
class VendingMachine(ABC):
    @abstractmethod
    def sell_drink(self):
        pass

# 真实主题
class RealVendingMachine(VendingMachine):
    def sell_drink(self):
        return "饮料已售出"

# 代理
class VendingMachineProxy(VendingMachine):
    def __init__(self):
        self._real_machine = RealVendingMachine()
        self._money = 0
    
    def insert_money(self, amount):
        self._money += amount
        print(f"投入了 {amount} 元")
    
    def sell_drink(self):
        if self._money >= 3:
            self._money -= 3
            return self._real_machine.sell_drink()
        else:
            return "金额不足，请继续投币"

# 使用示例
if __name__ == "__main__":
    proxy = VendingMachineProxy()
    print(proxy.sell_drink())  # 金额不足
    proxy.insert_money(2)
    print(proxy.sell_drink())  # 金额不足
    proxy.insert_money(2)
    print(proxy.sell_drink())  # 饮料已售出
