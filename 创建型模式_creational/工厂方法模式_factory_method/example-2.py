from abc import ABC, abstractmethod
from typing import List

# 抽象产品类 - 电子产品
class ElectronicProduct(ABC):
    def __init__(self):
        self.battery_level = 100
        self.is_powered_on = False
    
    @abstractmethod
    def power_on(self) -> str:
        pass
    
    @abstractmethod
    def power_off(self) -> str:
        pass
    
    @abstractmethod
    def get_battery_status(self) -> str:
        pass

# 具体产品类 - 手机
class Smartphone(ElectronicProduct):
    def power_on(self) -> str:
        if not self.is_powered_on:
            self.is_powered_on = True
            self.battery_level -= 5
            return "手机开机中...系统启动完成"
        return "手机已经处于开机状态"
    
    def power_off(self) -> str:
        if self.is_powered_on:
            self.is_powered_on = False
            return "手机关机中...已关机"
        return "手机已经处于关机状态"
    
    def get_battery_status(self) -> str:
        return f"手机电池电量: {self.battery_level}%"

# 具体产品类 - 笔记本电脑
class Laptop(ElectronicProduct):
    def power_on(self) -> str:
        if not self.is_powered_on:
            self.is_powered_on = True
            self.battery_level -= 10
            return "笔记本电脑启动中...系统加载完成"
        return "笔记本电脑已经处于开机状态"
    
    def power_off(self) -> str:
        if self.is_powered_on:
            self.is_powered_on = False
            return "笔记本电脑关机中...已关机"
        return "笔记本电脑已经处于关机状态"
    
    def get_battery_status(self) -> str:
        return f"笔记本电脑电池电量: {self.battery_level}%"

# 具体产品类 - 平板电脑
class Tablet(ElectronicProduct):
    def power_on(self) -> str:
        if not self.is_powered_on:
            self.is_powered_on = True
            self.battery_level -= 3
            return "平板电脑启动中...系统就绪"
        return "平板电脑已经处于开机状态"
    
    def power_off(self) -> str:
        if self.is_powered_on:
            self.is_powered_on = False
            return "平板电脑关机中...已关机"
        return "平板电脑已经处于关机状态"
    
    def get_battery_status(self) -> str:
        return f"平板电脑电池电量: {self.battery_level}%"

# 抽象创建者类
class ElectronicCreator(ABC):
    @abstractmethod
    def create_product(self) -> ElectronicProduct:
        pass
    
    def start_device(self) -> str:
        product = self.create_product()
        return product.power_on()
    
    def stop_device(self) -> str:
        product = self.create_product()
        return product.power_off()
    
    def check_battery(self) -> str:
        product = self.create_product()
        return product.get_battery_status()

# 具体创建者类 - 手机创建者
class SmartphoneCreator(ElectronicCreator):
    def create_product(self) -> ElectronicProduct:
        return Smartphone()

# 具体创建者类 - 笔记本电脑创建者
class LaptopCreator(ElectronicCreator):
    def create_product(self) -> ElectronicProduct:
        return Laptop()

# 具体创建者类 - 平板电脑创建者
class TabletCreator(ElectronicCreator):
    def create_product(self) -> ElectronicProduct:
        return Tablet()

def main():
    # 创建不同类型的电子产品创建者
    phone_creator = SmartphoneCreator()
    laptop_creator = LaptopCreator()
    tablet_creator = TabletCreator()

    # 测试手机
    print("=== 测试手机 ===")
    print(phone_creator.start_device())
    print(phone_creator.check_battery())
    print(phone_creator.start_device())  # 测试重复开机
    print(phone_creator.stop_device())
    
    # 测试笔记本电脑
    print("\n=== 测试笔记本电脑 ===")
    print(laptop_creator.start_device())
    print(laptop_creator.check_battery())
    print(laptop_creator.stop_device())
    
    # 测试平板电脑
    print("\n=== 测试平板电脑 ===")
    print(tablet_creator.start_device())
    print(tablet_creator.check_battery())
    print(tablet_creator.stop_device())

if __name__ == "__main__":
    main() 