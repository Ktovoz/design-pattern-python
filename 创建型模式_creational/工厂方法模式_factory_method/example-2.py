# -*- coding: utf-8 -*-
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
    
    @abstractmethod
    def get_device_info(self) -> str:
        pass

# 具体产品类 - 手机
class Smartphone(ElectronicProduct):
    def __init__(self):
        super().__init__()
        self.model = "智能手机"
        self.storage = "128GB"
    
    def power_on(self) -> str:
        if not self.is_powered_on:
            self.is_powered_on = True
            self.battery_level -= 5
            return f"{self.model}开机中...系统启动完成"
        return f"{self.model}已经处于开机状态"
    
    def power_off(self) -> str:
        if self.is_powered_on:
            self.is_powered_on = False
            return f"{self.model}关机中...已关机"
        return f"{self.model}已经处于关机状态"
    
    def get_battery_status(self) -> str:
        status = "开机" if self.is_powered_on else "关机"
        return f"{self.model}电池电量: {self.battery_level}% (状态: {status})"
    
    def get_device_info(self) -> str:
        return f"{self.model} - 存储: {self.storage}, 电量: {self.battery_level}%"

# 具体产品类 - 笔记本电脑
class Laptop(ElectronicProduct):
    def __init__(self):
        super().__init__()
        self.model = "笔记本电脑"
        self.cpu = "Intel i7"
        self.ram = "16GB"
    
    def power_on(self) -> str:
        if not self.is_powered_on:
            self.is_powered_on = True
            self.battery_level -= 10
            return f"{self.model}启动中...系统加载完成"
        return f"{self.model}已经处于开机状态"
    
    def power_off(self) -> str:
        if self.is_powered_on:
            self.is_powered_on = False
            return f"{self.model}关机中...已关机"
        return f"{self.model}已经处于关机状态"
    
    def get_battery_status(self) -> str:
        status = "开机" if self.is_powered_on else "关机"
        return f"{self.model}电池电量: {self.battery_level}% (状态: {status})"
    
    def get_device_info(self) -> str:
        return f"{self.model} - CPU: {self.cpu}, 内存: {self.ram}, 电量: {self.battery_level}%"

# 具体产品类 - 平板电脑
class Tablet(ElectronicProduct):
    def __init__(self):
        super().__init__()
        self.model = "平板电脑"
        self.screen_size = "10.1英寸"
        self.os = "Android"
    
    def power_on(self) -> str:
        if not self.is_powered_on:
            self.is_powered_on = True
            self.battery_level -= 3
            return f"{self.model}启动中...系统就绪"
        return f"{self.model}已经处于开机状态"
    
    def power_off(self) -> str:
        if self.is_powered_on:
            self.is_powered_on = False
            return f"{self.model}关机中...已关机"
        return f"{self.model}已经处于关机状态"
    
    def get_battery_status(self) -> str:
        status = "开机" if self.is_powered_on else "关机"
        return f"{self.model}电池电量: {self.battery_level}% (状态: {status})"
    
    def get_device_info(self) -> str:
        return f"{self.model} - 屏幕: {self.screen_size}, 系统: {self.os}, 电量: {self.battery_level}%"

# 抽象创建者类
class ElectronicCreator(ABC):
    def __init__(self):
        self._product = None
    
    @abstractmethod
    def create_product(self) -> ElectronicProduct:
        pass
    
    def get_product(self) -> ElectronicProduct:
        if self._product is None:
            self._product = self.create_product()
        return self._product
    
    def start_device(self) -> str:
        product = self.get_product()
        return product.power_on()
    
    def stop_device(self) -> str:
        product = self.get_product()
        return product.power_off()
    
    def check_battery(self) -> str:
        product = self.get_product()
        return product.get_battery_status()
    
    def get_device_info(self) -> str:
        product = self.get_product()
        return product.get_device_info()

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
    print(phone_creator.get_device_info())
    print(phone_creator.start_device())
    print(phone_creator.check_battery())
    print(phone_creator.start_device())  # 测试重复开机
    print(phone_creator.stop_device())
    print(phone_creator.check_battery())
    
    # 测试笔记本电脑
    print("\n=== 测试笔记本电脑 ===")
    print(laptop_creator.get_device_info())
    print(laptop_creator.start_device())
    print(laptop_creator.check_battery())
    print(laptop_creator.stop_device())
    print(laptop_creator.check_battery())
    
    # 测试平板电脑
    print("\n=== 测试平板电脑 ===")
    print(tablet_creator.get_device_info())
    print(tablet_creator.start_device())
    print(tablet_creator.check_battery())
    print(tablet_creator.stop_device())
    print(tablet_creator.check_battery())

if __name__ == "__main__":
    main() 