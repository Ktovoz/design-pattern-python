from copy import deepcopy
from abc import ABC, abstractmethod
from typing import Dict, List

class FurnitureComponent(ABC):
    def __init__(self, name: str, material: str):
        self.name = name
        self.material = material
        self.dimensions = {}
    
    @abstractmethod
    def clone(self):
        pass
    
    def set_dimension(self, dimension: str, value: float):
        self.dimensions[dimension] = value
    
    def __str__(self):
        dims = ", ".join([f"{k}: {v}cm" for k, v in self.dimensions.items()])
        return f"{self.name} ({self.material}) - 尺寸: {dims}"

class Drawer(FurnitureComponent):
    def __init__(self, name: str, material: str):
        super().__init__(name, material)
        self.set_dimension("宽度", 40)
        self.set_dimension("深度", 30)
        self.set_dimension("高度", 15)
    
    def clone(self):
        return deepcopy(self)

class Door(FurnitureComponent):
    def __init__(self, name: str, material: str):
        super().__init__(name, material)
        self.set_dimension("宽度", 60)
        self.set_dimension("高度", 180)
        self.set_dimension("厚度", 2)
    
    def clone(self):
        return deepcopy(self)

class Cabinet(FurnitureComponent):
    def __init__(self, name: str, material: str):
        super().__init__(name, material)
        self.set_dimension("宽度", 120)
        self.set_dimension("深度", 60)
        self.set_dimension("高度", 200)
        self.components: List[FurnitureComponent] = []
    
    def add_component(self, component: FurnitureComponent):
        self.components.append(component)
    
    def clone(self):
        return deepcopy(self)
    
    def __str__(self):
        base_info = super().__str__()
        components_info = "\n  组件:"
        for comp in self.components:
            components_info += f"\n    - {comp}"
        return base_info + components_info

class FurnitureRegistry:
    def __init__(self):
        self._prototypes: Dict[str, FurnitureComponent] = {}
    
    def register(self, name: str, prototype: FurnitureComponent):
        self._prototypes[name] = prototype
    
    def clone(self, name: str) -> FurnitureComponent:
        if name not in self._prototypes:
            raise ValueError(f"原型 '{name}' 未注册")
        return self._prototypes[name].clone()

# 使用示例
if __name__ == "__main__":
    # 创建原型注册表
    registry = FurnitureRegistry()
    
    # 创建并注册基础组件原型
    drawer_prototype = Drawer("标准抽屉", "实木")
    door_prototype = Door("标准门", "实木")
    cabinet_prototype = Cabinet("标准柜子", "实木")
    
    # 为柜子添加组件
    cabinet_prototype.add_component(drawer_prototype.clone())
    cabinet_prototype.add_component(door_prototype.clone())
    
    # 注册原型
    registry.register("drawer", drawer_prototype)
    registry.register("door", door_prototype)
    registry.register("cabinet", cabinet_prototype)
    
    # 克隆并修改
    custom_cabinet = registry.clone("cabinet")
    custom_cabinet.material = "红木"
    custom_cabinet.set_dimension("宽度", 150)
    
    # 添加新的抽屉
    new_drawer = registry.clone("drawer")
    new_drawer.set_dimension("宽度", 50)
    custom_cabinet.add_component(new_drawer)
    
    print("原始柜子:")
    print(registry.clone("cabinet"))
    print("\n定制柜子:")
    print(custom_cabinet)
