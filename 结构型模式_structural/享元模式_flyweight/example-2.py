from typing import Dict, List
from dataclasses import dataclass

@dataclass
class CupStyle:
    """咖啡杯样式享元类"""
    material: str  # 材质
    color: str     # 颜色
    size: str      # 尺寸
    pattern: str   # 图案

    def __str__(self):
        return f"材质: {self.material}, 颜色: {self.color}, 尺寸: {self.size}, 图案: {self.pattern}"

class CupStyleFactory:
    """咖啡杯样式工厂类"""
    _styles: Dict[str, CupStyle] = {}

    @classmethod
    def get_style(cls, material: str, color: str, size: str, pattern: str) -> CupStyle:
        key = f"{material}_{color}_{size}_{pattern}"
        if key not in cls._styles:
            cls._styles[key] = CupStyle(material, color, size, pattern)
        return cls._styles[key]

class CoffeeCup:
    """咖啡杯类"""
    def __init__(self, style: CupStyle, owner: str, temperature: float):
        self.style = style
        self.owner = owner  # 外部状态
        self.temperature = temperature  # 外部状态

    def serve(self):
        print(f"为 {self.owner} 提供咖啡")
        print(f"杯子样式: {self.style}")
        print(f"咖啡温度: {self.temperature}°C")

class CoffeeShop:
    """咖啡店类"""
    def __init__(self):
        self.cups: List[CoffeeCup] = []

    def add_cup(self, cup: CoffeeCup):
        self.cups.append(cup)

    def serve_all(self):
        for cup in self.cups:
            cup.serve()
            print("-" * 40)

def main():
    # 创建咖啡店
    shop = CoffeeShop()

    # 创建共享的杯子样式
    ceramic_style = CupStyleFactory.get_style("陶瓷", "白色", "中杯", "简约")
    glass_style = CupStyleFactory.get_style("玻璃", "透明", "大杯", "条纹")

    # 创建不同的咖啡杯实例
    cup1 = CoffeeCup(ceramic_style, "张三", 75.5)
    cup2 = CoffeeCup(ceramic_style, "李四", 80.0)
    cup3 = CoffeeCup(glass_style, "王五", 70.0)

    # 添加到咖啡店
    shop.add_cup(cup1)
    shop.add_cup(cup2)
    shop.add_cup(cup3)

    # 提供服务
    shop.serve_all()

if __name__ == "__main__":
    main()
