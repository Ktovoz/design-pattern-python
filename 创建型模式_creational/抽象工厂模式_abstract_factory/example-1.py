from abc import ABC, abstractmethod

# 抽象产品：椅子
class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

# 抽象产品：桌子
class Table(ABC):
    @abstractmethod
    def put(self):
        pass

# 具体产品：现代风格椅子
class ModernChair(Chair):
    def sit(self):
        print("坐在现代风格的椅子上")

# 具体产品：现代风格桌子
class ModernTable(Table):
    def put(self):
        print("在现代风格的桌子上放置物品")

# 具体产品：古典风格椅子
class ClassicChair(Chair):
    def sit(self):
        print("坐在古典风格的椅子上")

# 具体产品：古典风格桌子
class ClassicTable(Table):
    def put(self):
        print("在古典风格的桌子上放置物品")

# 抽象工厂
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    
    @abstractmethod
    def create_table(self) -> Table:
        pass

# 具体工厂：现代风格家具工厂
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_table(self) -> Table:
        return ModernTable()

# 具体工厂：古典风格家具工厂
class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ClassicChair()
    
    def create_table(self) -> Table:
        return ClassicTable()

# 客户端代码
def create_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    
    chair.sit()
    table.put()

# 使用示例
if __name__ == "__main__":
    # 创建现代风格家具
    modern_factory = ModernFurnitureFactory()
    print("创建现代风格家具：")
    create_furniture(modern_factory)
    
    # 创建古典风格家具
    classic_factory = ClassicFurnitureFactory()
    print("\n创建古典风格家具：")
    create_furniture(classic_factory)
