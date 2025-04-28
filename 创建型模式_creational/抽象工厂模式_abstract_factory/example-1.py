from abc import ABC, abstractmethod

# =============== 抽象产品类 ===============

class Chair(ABC):
    """椅子的抽象类"""
    @abstractmethod
    def sit(self):
        pass

class Sofa(ABC):
    """沙发的抽象类"""
    @abstractmethod
    def lie_down(self):
        pass

class CoffeeTable(ABC):
    """茶几的抽象类"""
    @abstractmethod
    def put_items(self):
        pass

# =============== 具体产品类 - 现代风格 ===============

class ModernChair(Chair):
    """现代风格椅子"""
    def sit(self):
        return "坐在简约现代风格的椅子上"

class ModernSofa(Sofa):
    """现代风格沙发"""
    def lie_down(self):
        return "躺在舒适的现代风格沙发上"

class ModernCoffeeTable(CoffeeTable):
    """现代风格茶几"""
    def put_items(self):
        return "在现代风格茶几上放置物品"

# =============== 具体产品类 - 古典风格 ===============

class ClassicChair(Chair):
    """古典风格椅子"""
    def sit(self):
        return "坐在雕花古典风格的椅子上"

class ClassicSofa(Sofa):
    """古典风格沙发"""
    def lie_down(self):
        return "躺在豪华的古典风格沙发上"

class ClassicCoffeeTable(CoffeeTable):
    """古典风格茶几"""
    def put_items(self):
        return "在古典风格茶几上放置物品"

# =============== 抽象工厂 ===============

class FurnitureFactory(ABC):
    """家具工厂的抽象类"""
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass

# =============== 具体工厂 ===============

class ModernFurnitureFactory(FurnitureFactory):
    """现代风格家具工厂"""
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

class ClassicFurnitureFactory(FurnitureFactory):
    """古典风格家具工厂"""
    def create_chair(self) -> Chair:
        return ClassicChair()

    def create_sofa(self) -> Sofa:
        return ClassicSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ClassicCoffeeTable()

# =============== 客户端代码 ===============

def client_code(factory: FurnitureFactory):
    """
    客户端代码 - 使用工厂创建并测试家具
    这段代码可以与任何工厂类一起工作，而不需要修改代码
    """
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    coffee_table = factory.create_coffee_table()

    print(chair.sit())
    print(sofa.lie_down())
    print(coffee_table.put_items())

# =============== 测试代码 ===============

if __name__ == "__main__":
    print("测试现代风格家具:")
    client_code(ModernFurnitureFactory())
    
    print("\n测试古典风格家具:")
    client_code(ClassicFurnitureFactory())
