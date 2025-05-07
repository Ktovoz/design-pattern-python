from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import random

class Material(Enum):
    WOOD = "木材"
    METAL = "金属"
    GLASS = "玻璃"
    PLASTIC = "塑料"

class Style(Enum):
    MODERN = "现代"
    CLASSIC = "古典"
    INDUSTRIAL = "工业"
    MINIMALIST = "极简"

@dataclass
class FurnitureStyle:
    """家具样式享元类"""
    material: Material
    style: Style
    color: str
    texture: str
    finish: str

    def __str__(self):
        return (f"材质: {self.material.value}, 风格: {self.style.value}, "
                f"颜色: {self.color}, 纹理: {self.texture}, 表面处理: {self.finish}")

class FurnitureStyleFactory:
    """家具样式工厂类"""
    _styles: Dict[str, FurnitureStyle] = {}

    @classmethod
    def get_style(cls, material: Material, style: Style, color: str, 
                  texture: str, finish: str) -> FurnitureStyle:
        key = f"{material.value}_{style.value}_{color}_{texture}_{finish}"
        if key not in cls._styles:
            cls._styles[key] = FurnitureStyle(material, style, color, texture, finish)
        return cls._styles[key]

class Furniture:
    """家具类"""
    def __init__(self, style: FurnitureStyle, name: str, dimensions: tuple,
                 price: float, location: str):
        self.style = style
        self.name = name
        self.dimensions = dimensions
        self.price = price
        self.location = location

    def display(self):
        print(f"\n家具名称: {self.name}")
        print(f"样式: {self.style}")
        print(f"尺寸: {self.dimensions[0]}x{self.dimensions[1]}x{self.dimensions[2]}cm")
        print(f"价格: ¥{self.price:.2f}")
        print(f"位置: {self.location}")

class FurnitureStore:
    """家具店类"""
    def __init__(self, name: str):
        self.name = name
        self.inventory: List[Furniture] = []

    def add_furniture(self, furniture: Furniture):
        self.inventory.append(furniture)

    def display_inventory(self):
        print(f"\n{self.name} 库存清单:")
        print("=" * 50)
        for furniture in self.inventory:
            furniture.display()
            print("-" * 50)

    def get_furniture_by_style(self, style: Style) -> List[Furniture]:
        return [f for f in self.inventory if f.style.style == style]

def create_sample_furniture() -> List[Furniture]:
    # 创建共享的家具样式
    modern_wood = FurnitureStyleFactory.get_style(
        Material.WOOD, Style.MODERN, "原木色", "自然纹理", "哑光"
    )
    classic_metal = FurnitureStyleFactory.get_style(
        Material.METAL, Style.CLASSIC, "古铜色", "拉丝", "抛光"
    )
    industrial_glass = FurnitureStyleFactory.get_style(
        Material.GLASS, Style.INDUSTRIAL, "透明", "磨砂", "透明"
    )

    # 创建家具实例
    furniture_list = [
        Furniture(modern_wood, "现代书桌", (120, 60, 75), 1299.00, "书房"),
        Furniture(modern_wood, "现代餐桌", (160, 80, 75), 2499.00, "餐厅"),
        Furniture(classic_metal, "古典茶几", (60, 60, 45), 899.00, "客厅"),
        Furniture(industrial_glass, "工业风咖啡桌", (80, 80, 50), 1599.00, "客厅"),
        Furniture(modern_wood, "现代床头柜", (50, 40, 60), 699.00, "卧室")
    ]
    return furniture_list

def main():
    # 创建家具店
    store = FurnitureStore("优品家居")

    # 添加家具到库存
    for furniture in create_sample_furniture():
        store.add_furniture(furniture)

    # 显示所有库存
    store.display_inventory()

    # 按风格筛选家具
    print("\n现代风格家具:")
    print("=" * 50)
    for furniture in store.get_furniture_by_style(Style.MODERN):
        furniture.display()
        print("-" * 50)

if __name__ == "__main__":
    main()
