from abc import ABC, abstractmethod

# 基础组件接口
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

# 具体组件
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 10.0

    def description(self) -> str:
        return "普通咖啡"

# 装饰器基类
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()

# 具体装饰器
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 2.0

    def description(self) -> str:
        return self._coffee.description() + " + 牛奶"

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.0

    def description(self) -> str:
        return self._coffee.description() + " + 糖"

# 使用示例
if __name__ == "__main__":
    # 创建一杯普通咖啡
    coffee = SimpleCoffee()
    print(f"订单: {coffee.description()}")
    print(f"价格: ¥{coffee.cost()}")

    # 添加牛奶
    coffee_with_milk = MilkDecorator(coffee)
    print(f"\n订单: {coffee_with_milk.description()}")
    print(f"价格: ¥{coffee_with_milk.cost()}")

    # 添加牛奶和糖
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"\n订单: {coffee_with_milk_and_sugar.description()}")
    print(f"价格: ¥{coffee_with_milk_and_sugar.cost()}")
