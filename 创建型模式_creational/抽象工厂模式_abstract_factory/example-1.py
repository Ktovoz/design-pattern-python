from abc import ABC, abstractmethod
from typing import Dict, Any

# 抽象产品：椅子
class Chair(ABC):
    """椅子抽象基类"""
    
    def __init__(self, material: str, color: str):
        self.material = material
        self.color = color
    
    @abstractmethod
    def sit(self) -> str:
        """坐下的行为"""
        pass
    
    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """获取椅子信息"""
        pass

# 抽象产品：桌子
class Table(ABC):
    """桌子抽象基类"""
    
    def __init__(self, material: str, size: str):
        self.material = material
        self.size = size
    
    @abstractmethod
    def put(self) -> str:
        """放置物品的行为"""
        pass
    
    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """获取桌子信息"""
        pass

# 具体产品：现代风格椅子
class ModernChair(Chair):
    """现代风格椅子"""
    
    def __init__(self):
        super().__init__("金属", "黑色")
        self.style = "现代风格"
        self.comfort_level = 8
    
    def sit(self) -> str:
        return f"舒适地坐在{self.style}的{self.color}{self.material}椅子上（舒适度：{self.comfort_level}/10）"
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "类型": "椅子",
            "风格": self.style,
            "材质": self.material,
            "颜色": self.color,
            "舒适度": self.comfort_level
        }

# 具体产品：现代风格桌子
class ModernTable(Table):
    """现代风格桌子"""
    
    def __init__(self):
        super().__init__("钢化玻璃", "大型")
        self.style = "现代风格"
        self.load_capacity = "50kg"
    
    def put(self) -> str:
        return f"在{self.style}的{self.size}{self.material}桌子上整齐地放置物品（承重：{self.load_capacity}）"
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "类型": "桌子",
            "风格": self.style,
            "材质": self.material,
            "尺寸": self.size,
            "承重": self.load_capacity
        }

# 具体产品：古典风格椅子
class ClassicChair(Chair):
    """古典风格椅子"""
    
    def __init__(self):
        super().__init__("实木", "棕色")
        self.style = "古典风格"
        self.comfort_level = 9
    
    def sit(self) -> str:
        return f"优雅地坐在{self.style}的{self.color}{self.material}椅子上（舒适度：{self.comfort_level}/10）"
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "类型": "椅子",
            "风格": self.style,
            "材质": self.material,
            "颜色": self.color,
            "舒适度": self.comfort_level
        }

# 具体产品：古典风格桌子
class ClassicTable(Table):
    """古典风格桌子"""
    
    def __init__(self):
        super().__init__("红木", "中型")
        self.style = "古典风格"
        self.load_capacity = "80kg"
    
    def put(self) -> str:
        return f"在{self.style}的{self.size}{self.material}桌子上优雅地放置物品（承重：{self.load_capacity}）"
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "类型": "桌子",
            "风格": self.style,
            "材质": self.material,
            "尺寸": self.size,
            "承重": self.load_capacity
        }

# 抽象工厂
class FurnitureFactory(ABC):
    """家具工厂抽象基类"""
    
    @abstractmethod
    def create_chair(self) -> Chair:
        """创建椅子"""
        pass
    
    @abstractmethod
    def create_table(self) -> Table:
        """创建桌子"""
        pass
    
    @abstractmethod
    def get_style_name(self) -> str:
        """获取工厂风格名称"""
        pass

# 具体工厂：现代风格家具工厂
class ModernFurnitureFactory(FurnitureFactory):
    """现代风格家具工厂"""
    
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_table(self) -> Table:
        return ModernTable()
    
    def get_style_name(self) -> str:
        return "现代风格"

# 具体工厂：古典风格家具工厂
class ClassicFurnitureFactory(FurnitureFactory):
    """古典风格家具工厂"""
    
    def create_chair(self) -> Chair:
        return ClassicChair()
    
    def create_table(self) -> Table:
        return ClassicTable()
    
    def get_style_name(self) -> str:
        return "古典风格"

# 客户端代码
def create_furniture_set(factory: FurnitureFactory) -> None:
    """使用工厂创建家具套装并展示信息"""
    print(f"\n{'='*50}")
    print(f"正在创建 {factory.get_style_name()} 家具套装")
    print(f"{'='*50}")
    
    # 创建家具
    chair = factory.create_chair()
    table = factory.create_table()
    
    # 展示家具信息
    print("\n📺 家具信息：")
    chair_info = chair.get_info()
    table_info = table.get_info()
    
    print(f"  椅子：{chair_info['风格']} | {chair_info['材质']} | {chair_info['颜色']} | 舒适度：{chair_info['舒适度']}/10")
    print(f"  桌子：{table_info['风格']} | {table_info['材质']} | {table_info['尺寸']} | 承重：{table_info['承重']}")
    
    # 使用家具
    print("\n🪑 使用体验：")
    print(f"  {chair.sit()}")
    print(f"  {table.put()}")

# 使用示例
if __name__ == "__main__":
    print("🏠 家具工厂抽象工厂模式演示")
    print("本示例展示了如何使用抽象工厂模式创建不同风格的家具套装")
    
    # 创建现代风格家具
    modern_factory = ModernFurnitureFactory()
    create_furniture_set(modern_factory)
    
    # 创建古典风格家具
    classic_factory = ClassicFurnitureFactory()
    create_furniture_set(classic_factory)
    
    print(f"\n{'='*50}")
    print("✨ 演示完成！两种风格的家具都已成功创建并使用。")
    print("💡 注意：同一工厂创建的家具保持了风格的一致性。")
    print(f"{'='*50}")
