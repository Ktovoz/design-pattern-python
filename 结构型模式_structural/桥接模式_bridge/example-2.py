from abc import ABC, abstractmethod

# 咖啡豆接口（实现部分）
class CoffeeBean(ABC):
    @abstractmethod
    def grind(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass

# 具体咖啡豆实现
class ArabicaBean(CoffeeBean):
    def grind(self):
        return "研磨阿拉比卡咖啡豆"
    
    def get_name(self):
        return "阿拉比卡"

class RobustaBean(CoffeeBean):
    def grind(self):
        return "研磨罗布斯塔咖啡豆"
    
    def get_name(self):
        return "罗布斯塔"

# 咖啡机接口（抽象部分）
class CoffeeMachine(ABC):
    def __init__(self, bean: CoffeeBean):
        self.bean = bean
    
    @abstractmethod
    def make_coffee(self):
        pass

# 具体咖啡机实现
class EspressoMachine(CoffeeMachine):
    def make_coffee(self):
        print(f"使用{self.bean.get_name()}咖啡豆")
        print(self.bean.grind())
        print("制作浓缩咖啡")

class DripCoffeeMachine(CoffeeMachine):
    def make_coffee(self):
        print(f"使用{self.bean.get_name()}咖啡豆")
        print(self.bean.grind())
        print("制作滴滤咖啡")

# 使用示例
if __name__ == "__main__":
    # 创建咖啡豆
    arabica = ArabicaBean()
    robusta = RobustaBean()
    
    # 创建不同类型的咖啡机
    espresso_with_arabica = EspressoMachine(arabica)
    espresso_with_robusta = EspressoMachine(robusta)
    drip_with_arabica = DripCoffeeMachine(arabica)
    drip_with_robusta = DripCoffeeMachine(robusta)
    
    # 制作咖啡
    print("=== 使用阿拉比卡豆制作浓缩咖啡 ===")
    espresso_with_arabica.make_coffee()
    
    print("\n=== 使用罗布斯塔豆制作浓缩咖啡 ===")
    espresso_with_robusta.make_coffee()
    
    print("\n=== 使用阿拉比卡豆制作滴滤咖啡 ===")
    drip_with_arabica.make_coffee()
    
    print("\n=== 使用罗布斯塔豆制作滴滤咖啡 ===")
    drip_with_robusta.make_coffee()
