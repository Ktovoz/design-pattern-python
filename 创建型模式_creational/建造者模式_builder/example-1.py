from abc import ABC, abstractmethod

# 产品类
class Sandwich:
    def __init__(self):
        self.bread = None
        self.vegetables = []
        self.meat = None
        self.sauce = None

    def __str__(self):
        return f"三明治包含：\n面包：{self.bread}\n蔬菜：{', '.join(self.vegetables)}\n肉类：{self.meat}\n酱料：{self.sauce}"

# 抽象建造者
class SandwichBuilder(ABC):
    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_vegetables(self):
        pass

    @abstractmethod
    def add_meat(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

# 具体建造者
class ClubSandwichBuilder(SandwichBuilder):
    def __init__(self):
        self.sandwich = Sandwich()

    def add_bread(self):
        self.sandwich.bread = "全麦面包"
        return self

    def add_vegetables(self):
        self.sandwich.vegetables = ["生菜", "番茄", "黄瓜"]
        return self

    def add_meat(self):
        self.sandwich.meat = "烤鸡胸肉"
        return self

    def add_sauce(self):
        self.sandwich.sauce = "蛋黄酱"
        return self

    def get_result(self):
        return self.sandwich

# 指导者
class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_sandwich(self):
        return (self.builder
                .add_bread()
                .add_vegetables()
                .add_meat()
                .add_sauce()
                .get_result())

# 使用示例
if __name__ == "__main__":
    # 创建具体建造者
    builder = ClubSandwichBuilder()
    # 创建指导者
    director = SandwichDirector(builder)
    # 制作三明治
    sandwich = director.make_sandwich()
    print(sandwich)