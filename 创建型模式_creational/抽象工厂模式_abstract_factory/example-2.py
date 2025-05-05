from abc import ABC, abstractmethod
from typing import List

# 抽象产品：处理器
class Processor(ABC):
    @abstractmethod
    def process(self):
        pass

# 抽象产品：显示器
class Display(ABC):
    @abstractmethod
    def show(self):
        pass

# 抽象产品：电池
class Battery(ABC):
    @abstractmethod
    def power(self):
        pass

# 具体产品：高性能处理器
class HighPerformanceProcessor(Processor):
    def process(self):
        print("使用高性能处理器处理任务")

# 具体产品：普通性能处理器
class StandardProcessor(Processor):
    def process(self):
        print("使用普通性能处理器处理任务")

# 具体产品：高清显示器
class HDDisplay(Display):
    def show(self):
        print("高清显示器显示内容")

# 具体产品：普通显示器
class StandardDisplay(Display):
    def show(self):
        print("普通显示器显示内容")

# 具体产品：大容量电池
class LargeBattery(Battery):
    def power(self):
        print("大容量电池供电")

# 具体产品：标准电池
class StandardBattery(Battery):
    def power(self):
        print("标准电池供电")

# 抽象工厂
class DeviceFactory(ABC):
    @abstractmethod
    def create_processor(self) -> Processor:
        pass
    
    @abstractmethod
    def create_display(self) -> Display:
        pass
    
    @abstractmethod
    def create_battery(self) -> Battery:
        pass

# 具体工厂：高端设备工厂
class PremiumDeviceFactory(DeviceFactory):
    def create_processor(self) -> Processor:
        return HighPerformanceProcessor()
    
    def create_display(self) -> Display:
        return HDDisplay()
    
    def create_battery(self) -> Battery:
        return LargeBattery()

# 具体工厂：标准设备工厂
class StandardDeviceFactory(DeviceFactory):
    def create_processor(self) -> Processor:
        return StandardProcessor()
    
    def create_display(self) -> Display:
        return StandardDisplay()
    
    def create_battery(self) -> Battery:
        return StandardBattery()

# 设备类
class Device:
    def __init__(self, processor: Processor, display: Display, battery: Battery):
        self.processor = processor
        self.display = display
        self.battery = battery
    
    def operate(self):
        self.processor.process()
        self.display.show()
        self.battery.power()

# 客户端代码
def create_device(factory: DeviceFactory) -> Device:
    processor = factory.create_processor()
    display = factory.create_display()
    battery = factory.create_battery()
    return Device(processor, display, battery)

# 使用示例
if __name__ == "__main__":
    # 创建高端设备
    premium_factory = PremiumDeviceFactory()
    print("创建高端设备：")
    premium_device = create_device(premium_factory)
    premium_device.operate()
    
    # 创建标准设备
    standard_factory = StandardDeviceFactory()
    print("\n创建标准设备：")
    standard_device = create_device(standard_factory)
    standard_device.operate()
