from abc import ABC, abstractmethod

# 访问者接口
class ShoppingVisitor(ABC):
    @abstractmethod
    def visit_fruit(self, fruit):
        pass
    
    @abstractmethod
    def visit_vegetable(self, vegetable):
        pass

# 具体访问者 - 价格计算器
class PriceCalculator(ShoppingVisitor):
    def visit_fruit(self, fruit):
        return fruit.price * fruit.weight
    
    def visit_vegetable(self, vegetable):
        return vegetable.price * vegetable.weight

# 具体访问者 - 营养分析器
class NutritionAnalyzer(ShoppingVisitor):
    def visit_fruit(self, fruit):
        return f"{fruit.name} 含有 {fruit.vitamin} 维生素"
    
    def visit_vegetable(self, vegetable):
        return f"{vegetable.name} 含有 {vegetable.fiber} 克纤维"

# 商品接口
class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# 具体商品 - 水果
class Fruit(Item):
    def __init__(self, name, price, weight, vitamin):
        self.name = name
        self.price = price
        self.weight = weight
        self.vitamin = vitamin
    
    def accept(self, visitor):
        return visitor.visit_fruit(self)

# 具体商品 - 蔬菜
class Vegetable(Item):
    def __init__(self, name, price, weight, fiber):
        self.name = name
        self.price = price
        self.weight = weight
        self.fiber = fiber
    
    def accept(self, visitor):
        return visitor.visit_vegetable(self)

# 使用示例
if __name__ == "__main__":
    # 创建商品
    apple = Fruit("苹果", 5.0, 0.5, "维生素C")
    carrot = Vegetable("胡萝卜", 3.0, 0.3, 2.5)
    
    # 创建访问者
    price_calculator = PriceCalculator()
    nutrition_analyzer = NutritionAnalyzer()
    
    # 计算价格
    print(f"苹果价格: {apple.accept(price_calculator)}元")
    print(f"胡萝卜价格: {carrot.accept(price_calculator)}元")
    
    # 分析营养
    print(apple.accept(nutrition_analyzer))
    print(carrot.accept(nutrition_analyzer))
