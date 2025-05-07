from abc import ABC, abstractmethod
from typing import List, Dict
from dataclasses import dataclass
from enum import Enum

class Material(Enum):
    WOOD = "木材"
    CONCRETE = "混凝土"
    STEEL = "钢材"
    BRICK = "砖块"
    GLASS = "玻璃"

@dataclass
class Room:
    name: str
    area: float
    windows: int
    doors: int
    materials: List[Material]

@dataclass
class Floor:
    level: int
    rooms: List[Room]
    material: Material

# 产品类
class House:
    def __init__(self):
        self.floors: List[Floor] = []
        self.foundation: Material = None
        self.roof: Material = None
        self.garden: bool = False
        self.garage: bool = False
        self.swimming_pool: bool = False
        self.total_area: float = 0.0

    def __str__(self):
        result = [f"房屋信息："]
        result.append(f"地基材料：{self.foundation.value}")
        result.append(f"屋顶材料：{self.roof.value}")
        result.append(f"花园：{'有' if self.garden else '无'}")
        result.append(f"车库：{'有' if self.garage else '无'}")
        result.append(f"游泳池：{'有' if self.swimming_pool else '无'}")
        result.append(f"总面积：{self.total_area}平方米")
        result.append("\n楼层信息：")
        
        for floor in self.floors:
            result.append(f"\n第{floor.level}层（{floor.material.value}）：")
            for room in floor.rooms:
                result.append(f"  - {room.name}：")
                result.append(f"    面积：{room.area}平方米")
                result.append(f"    窗户：{room.windows}个")
                result.append(f"    门：{room.doors}个")
                result.append(f"    材料：{', '.join(m.value for m in room.materials)}")
        
        return "\n".join(result)

# 抽象建造者
class HouseBuilder(ABC):
    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_floor(self, level: int):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def add_garden(self):
        pass

    @abstractmethod
    def add_garage(self):
        pass

    @abstractmethod
    def add_swimming_pool(self):
        pass

# 具体建造者 - 现代别墅
class ModernVillaBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = Material.CONCRETE
        return self

    def build_floor(self, level: int):
        rooms = []
        if level == 1:
            rooms = [
                Room("客厅", 50.0, 3, 2, [Material.GLASS, Material.STEEL]),
                Room("厨房", 30.0, 2, 1, [Material.STEEL, Material.GLASS]),
                Room("餐厅", 25.0, 2, 1, [Material.GLASS, Material.WOOD])
            ]
        elif level == 2:
            rooms = [
                Room("主卧", 40.0, 2, 1, [Material.WOOD, Material.GLASS]),
                Room("次卧", 30.0, 2, 1, [Material.WOOD, Material.GLASS]),
                Room("书房", 25.0, 2, 1, [Material.WOOD, Material.GLASS])
            ]
        elif level == 3:
            rooms = [
                Room("娱乐室", 35.0, 3, 1, [Material.GLASS, Material.STEEL]),
                Room("健身房", 30.0, 2, 1, [Material.STEEL, Material.GLASS])
            ]

        floor = Floor(level, rooms, Material.CONCRETE)
        self.house.floors.append(floor)
        self.house.total_area += sum(room.area for room in rooms)
        return self

    def build_roof(self):
        self.house.roof = Material.STEEL
        return self

    def add_garden(self):
        self.house.garden = True
        return self

    def add_garage(self):
        self.house.garage = True
        return self

    def add_swimming_pool(self):
        self.house.swimming_pool = True
        return self

    def get_result(self):
        return self.house

# 具体建造者 - 传统住宅
class TraditionalHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = Material.BRICK
        return self

    def build_floor(self, level: int):
        rooms = []
        if level == 1:
            rooms = [
                Room("客厅", 40.0, 2, 2, [Material.WOOD, Material.BRICK]),
                Room("厨房", 25.0, 1, 1, [Material.BRICK, Material.WOOD]),
                Room("餐厅", 20.0, 1, 1, [Material.WOOD, Material.BRICK])
            ]
        elif level == 2:
            rooms = [
                Room("主卧", 35.0, 2, 1, [Material.WOOD, Material.BRICK]),
                Room("次卧", 30.0, 1, 1, [Material.WOOD, Material.BRICK]),
                Room("书房", 20.0, 1, 1, [Material.WOOD, Material.BRICK])
            ]

        floor = Floor(level, rooms, Material.BRICK)
        self.house.floors.append(floor)
        self.house.total_area += sum(room.area for room in rooms)
        return self

    def build_roof(self):
        self.house.roof = Material.WOOD
        return self

    def add_garden(self):
        self.house.garden = True
        return self

    def add_garage(self):
        self.house.garage = False
        return self

    def add_swimming_pool(self):
        self.house.swimming_pool = False
        return self

    def get_result(self):
        return self.house

# 指导者
class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_modern_villa(self):
        return (self.builder
                .build_foundation()
                .build_floor(1)
                .build_floor(2)
                .build_floor(3)
                .build_roof()
                .add_garden()
                .add_garage()
                .add_swimming_pool()
                .get_result())

    def build_traditional_house(self):
        return (self.builder
                .build_foundation()
                .build_floor(1)
                .build_floor(2)
                .build_roof()
                .add_garden()
                .get_result())

# 使用示例
if __name__ == "__main__":
    # 建造现代别墅
    modern_builder = ModernVillaBuilder()
    modern_director = HouseDirector(modern_builder)
    modern_house = modern_director.build_modern_villa()
    print("现代别墅：")
    print(modern_house)
    print("\n" + "="*100 + "\n")

    # 建造传统住宅
    traditional_builder = TraditionalHouseBuilder()
    traditional_director = HouseDirector(traditional_builder)
    traditional_house = traditional_director.build_traditional_house()
    print("传统住宅：")
    print(traditional_house)