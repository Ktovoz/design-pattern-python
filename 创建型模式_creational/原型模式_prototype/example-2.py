from copy import deepcopy
from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.specs = {}
    
    @abstractmethod
    def clone(self):
        pass
    
    def set_spec(self, key, value):
        self.specs[key] = value
    
    def __str__(self):
        specs_str = ", ".join([f"{k}: {v}" for k, v in self.specs.items()])
        return f"{self.brand} {self.model} - 价格: {self.price}元, 规格: {specs_str}"

class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
        self.set_spec("操作系统", "Android")
        self.set_spec("屏幕尺寸", "6.1英寸")
    
    def clone(self):
        return deepcopy(self)

class Laptop(ElectronicDevice):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
        self.set_spec("处理器", "Intel i7")
        self.set_spec("内存", "16GB")
    
    def clone(self):
        return deepcopy(self)

# 使用示例
if __name__ == "__main__":
    # 创建手机原型
    phone_prototype = Smartphone("小米", "13", 3999)
    phone_prototype.set_spec("电池容量", "4500mAh")
    
    # 创建笔记本原型
    laptop_prototype = Laptop("联想", "ThinkPad", 6999)
    laptop_prototype.set_spec("硬盘", "512GB SSD")
    
    # 克隆并修改
    phone1 = phone_prototype.clone()
    phone1.set_spec("颜色", "黑色")
    
    laptop1 = laptop_prototype.clone()
    laptop1.set_spec("显卡", "RTX 3060")
    
    print("原始手机:", phone_prototype)
    print("克隆手机:", phone1)
    print("\n原始笔记本:", laptop_prototype)
    print("克隆笔记本:", laptop1)
