from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class DeviceType(Enum):
    """设备类型枚举"""
    PREMIUM = "高端设备"
    STANDARD = "标准设备"

@dataclass
class Specification:
    """设备规格数据类"""
    name: str
    value: str
    unit: str = ""

# 抽象产品：处理器
class Processor(ABC):
    """处理器抽象基类"""
    
    def __init__(self, model: str, cores: int, frequency: float):
        self.model = model
        self.cores = cores
        self.frequency = frequency
        self.temperature = 35  # 初始温度
        self.is_running = False
    
    @abstractmethod
    def process(self) -> str:
        """处理任务"""
        pass
    
    @abstractmethod
    def get_specifications(self) -> List[Specification]:
        """获取处理器规格"""
        pass
    
    def start(self) -> None:
        """启动处理器"""
        self.is_running = True
        self.temperature += 20
    
    def stop(self) -> None:
        """停止处理器"""
        self.is_running = False
        self.temperature = max(35, self.temperature - 20)

# 抽象产品：显示器
class Display(ABC):
    """显示器抽象基类"""
    
    def __init__(self, size: float, resolution: str, panel_type: str):
        self.size = size
        self.resolution = resolution
        self.panel_type = panel_type
        self.brightness = 50  # 亮度百分比
        self.is_on = False
    
    @abstractmethod
    def show(self) -> str:
        """显示内容"""
        pass
    
    @abstractmethod
    def get_specifications(self) -> List[Specification]:
        """获取显示器规格"""
        pass
    
    def turn_on(self) -> None:
        """开启显示器"""
        self.is_on = True
    
    def turn_off(self) -> None:
        """关闭显示器"""
        self.is_on = False

# 抽象产品：电池
class Battery(ABC):
    """电池抽象基类"""
    
    def __init__(self, capacity: int, voltage: float):
        self.capacity = capacity  # mAh
        self.voltage = voltage
        self.current_charge = capacity  # 当前电量
        self.is_charging = False
    
    @abstractmethod
    def power(self) -> str:
        """供电"""
        pass
    
    @abstractmethod
    def get_specifications(self) -> List[Specification]:
        """获取电池规格"""
        pass
    
    @property
    def charge_percentage(self) -> int:
        """电量百分比"""
        return int((self.current_charge / self.capacity) * 100)
    
    def consume_power(self, amount: int) -> None:
        """消耗电力"""
        self.current_charge = max(0, self.current_charge - amount)

# 具体产品：高性能处理器
class HighPerformanceProcessor(Processor):
    """高性能处理器"""
    
    def __init__(self):
        super().__init__("Intel i9-13900K", 24, 3.0)
        self.boost_frequency = 5.8
    
    def process(self) -> str:
        if not self.is_running:
            self.start()
        return f"使用{self.model}高性能处理器处理复杂任务（{self.cores}核心 @ {self.frequency}-{self.boost_frequency}GHz，当前温度：{self.temperature}°C）"
    
    def get_specifications(self) -> List[Specification]:
        return [
            Specification("型号", self.model),
            Specification("核心数", str(self.cores), "核"),
            Specification("基础频率", str(self.frequency), "GHz"),
            Specification("最大睿频", str(self.boost_frequency), "GHz"),
            Specification("架构", "Raptor Lake"),
            Specification("制程", "Intel 7")
        ]

# 具体产品：普通性能处理器
class StandardProcessor(Processor):
    """标准性能处理器"""
    
    def __init__(self):
        super().__init__("Intel i5-12400", 6, 2.5)
        self.boost_frequency = 4.4
    
    def process(self) -> str:
        if not self.is_running:
            self.start()
        return f"使用{self.model}标准处理器处理日常任务（{self.cores}核心 @ {self.frequency}-{self.boost_frequency}GHz，当前温度：{self.temperature}°C）"
    
    def get_specifications(self) -> List[Specification]:
        return [
            Specification("型号", self.model),
            Specification("核心数", str(self.cores), "核"),
            Specification("基础频率", str(self.frequency), "GHz"),
            Specification("最大睿频", str(self.boost_frequency), "GHz"),
            Specification("架构", "Alder Lake"),
            Specification("制程", "Intel 7")
        ]

# 具体产品：高清显示器
class HDDisplay(Display):
    """高清显示器"""
    
    def __init__(self):
        super().__init__(27.0, "2560x1440", "IPS")
        self.refresh_rate = 144
        self.color_gamut = "100% sRGB"
    
    def show(self) -> str:
        if not self.is_on:
            self.turn_on()
        return f"{self.size}英寸高清显示器显示精美内容（{self.resolution} @ {self.refresh_rate}Hz，{self.panel_type}面板，亮度：{self.brightness}%）"
    
    def get_specifications(self) -> List[Specification]:
        return [
            Specification("尺寸", str(self.size), "英寸"),
            Specification("分辨率", self.resolution),
            Specification("面板类型", self.panel_type),
            Specification("刷新率", str(self.refresh_rate), "Hz"),
            Specification("色域", self.color_gamut),
            Specification("亮度", "400", "nits")
        ]

# 具体产品：普通显示器
class StandardDisplay(Display):
    """标准显示器"""
    
    def __init__(self):
        super().__init__(24.0, "1920x1080", "VA")
        self.refresh_rate = 75
        self.color_gamut = "85% sRGB"
    
    def show(self) -> str:
        if not self.is_on:
            self.turn_on()
        return f"{self.size}英寸标准显示器显示清晰内容（{self.resolution} @ {self.refresh_rate}Hz，{self.panel_type}面板，亮度：{self.brightness}%）"
    
    def get_specifications(self) -> List[Specification]:
        return [
            Specification("尺寸", str(self.size), "英寸"),
            Specification("分辨率", self.resolution),
            Specification("面板类型", self.panel_type),
            Specification("刷新率", str(self.refresh_rate), "Hz"),
            Specification("色域", self.color_gamut),
            Specification("亮度", "250", "nits")
        ]

# 具体产品：大容量电池
class LargeBattery(Battery):
    """大容量电池"""
    
    def __init__(self):
        super().__init__(5000, 11.1)
        self.charging_speed = "100W"
        self.battery_type = "锂聚合物"
    
    def power(self) -> str:
        if self.current_charge > 0:
            self.consume_power(50)
            return f"大容量{self.battery_type}电池持续供电中（容量：{self.capacity}mAh，剩余：{self.charge_percentage}%，电压：{self.voltage}V）"
        return "电池电量不足，需要充电"
    
    def get_specifications(self) -> List[Specification]:
        return [
            Specification("容量", str(self.capacity), "mAh"),
            Specification("电压", str(self.voltage), "V"),
            Specification("类型", self.battery_type),
            Specification("充电功率", self.charging_speed),
            Specification("充电时间", "45", "分钟"),
            Specification("循环寿命", "1000", "次")
        ]

# 具体产品：标准电池
class StandardBattery(Battery):
    """标准电池"""
    
    def __init__(self):
        super().__init__(3000, 7.4)
        self.charging_speed = "65W"
        self.battery_type = "锂离子"
    
    def power(self) -> str:
        if self.current_charge > 0:
            self.consume_power(30)
            return f"标准{self.battery_type}电池稳定供电中（容量：{self.capacity}mAh，剩余：{self.charge_percentage}%，电压：{self.voltage}V）"
        return "电池电量不足，需要充电"
    
    def get_specifications(self) -> List[Specification]:
        return [
            Specification("容量", str(self.capacity), "mAh"),
            Specification("电压", str(self.voltage), "V"),
            Specification("类型", self.battery_type),
            Specification("充电功率", self.charging_speed),
            Specification("充电时间", "60", "分钟"),
            Specification("循环寿命", "800", "次")
        ]

# 抽象工厂
class DeviceFactory(ABC):
    """设备工厂抽象基类"""
    
    @abstractmethod
    def create_processor(self) -> Processor:
        """创建处理器"""
        pass
    
    @abstractmethod
    def create_display(self) -> Display:
        """创建显示器"""
        pass
    
    @abstractmethod
    def create_battery(self) -> Battery:
        """创建电池"""
        pass
    
    @abstractmethod
    def get_device_type(self) -> DeviceType:
        """获取设备类型"""
        pass

# 具体工厂：高端设备工厂
class PremiumDeviceFactory(DeviceFactory):
    """高端设备工厂"""
    
    def create_processor(self) -> Processor:
        return HighPerformanceProcessor()
    
    def create_display(self) -> Display:
        return HDDisplay()
    
    def create_battery(self) -> Battery:
        return LargeBattery()
    
    def get_device_type(self) -> DeviceType:
        return DeviceType.PREMIUM

# 具体工厂：标准设备工厂
class StandardDeviceFactory(DeviceFactory):
    """标准设备工厂"""
    
    def create_processor(self) -> Processor:
        return StandardProcessor()
    
    def create_display(self) -> Display:
        return StandardDisplay()
    
    def create_battery(self) -> Battery:
        return StandardBattery()
    
    def get_device_type(self) -> DeviceType:
        return DeviceType.STANDARD

# 设备类
class Device:
    """设备组合类"""
    
    def __init__(self, processor: Processor, display: Display, battery: Battery, device_type: DeviceType):
        self.processor = processor
        self.display = display
        self.battery = battery
        self.device_type = device_type
        self.is_powered_on = False
    
    def power_on(self) -> str:
        """开机"""
        if not self.is_powered_on:
            self.is_powered_on = True
            return f"🔋 {self.device_type.value}正在启动..."
        return f"⚠️ {self.device_type.value}已经处于开机状态"
    
    def operate(self) -> List[str]:
        """运行设备"""
        if not self.is_powered_on:
            return [self.power_on()]
        
        operations = []
        operations.append(f"💻 {self.processor.process()}")
        operations.append(f"🖥️ {self.display.show()}")
        operations.append(f"🔋 {self.battery.power()}")
        return operations
    
    def get_full_specifications(self) -> Dict[str, List[Specification]]:
        """获取完整规格信息"""
        return {
            "处理器": self.processor.get_specifications(),
            "显示器": self.display.get_specifications(),
            "电池": self.battery.get_specifications()
        }
    
    def power_off(self) -> str:
        """关机"""
        if self.is_powered_on:
            self.processor.stop()
            self.display.turn_off()
            self.is_powered_on = False
            return f"📴 {self.device_type.value}已关机"
        return f"⚠️ {self.device_type.value}已经处于关机状态"

# 客户端代码
def create_and_test_device(factory: DeviceFactory) -> None:
    """创建并测试设备"""
    device_type = factory.get_device_type()
    print(f"\n{'='*60}")
    print(f"🏭 正在使用工厂创建 {device_type.value}")
    print(f"{'='*60}")
    
    # 创建设备
    processor = factory.create_processor()
    display = factory.create_display()
    battery = factory.create_battery()
    device = Device(processor, display, battery, device_type)
    
    # 显示设备规格
    print(f"\n📋 {device_type.value}详细规格：")
    specs = device.get_full_specifications()
    
    for component_name, component_specs in specs.items():
        print(f"\n  🔧 {component_name}：")
        for spec in component_specs:
            unit_str = f" {spec.unit}" if spec.unit else ""
            print(f"     • {spec.name}：{spec.value}{unit_str}")
    
    # 测试设备运行
    print(f"\n🔄 {device_type.value}运行测试：")
    
    # 开机
    print(f"  {device.power_on()}")
    
    # 运行操作
    operations = device.operate()
    for operation in operations:
        print(f"  {operation}")
    
    # 再次运行以查看电池消耗
    print(f"\n  ⏳ 继续使用设备...")
    operations = device.operate()
    for operation in operations:
        print(f"  {operation}")
    
    # 关机
    print(f"\n  {device.power_off()}")

# 使用示例
if __name__ == "__main__":
    print("📱 电子设备工厂抽象工厂模式演示")
    print("本示例展示了如何使用抽象工厂模式创建不同等级的电子设备")
    
    # 创建高端设备
    premium_factory = PremiumDeviceFactory()
    create_and_test_device(premium_factory)
    
    # 创建标准设备
    standard_factory = StandardDeviceFactory()
    create_and_test_device(standard_factory)
    
    print(f"\n{'='*60}")
    print("✨ 演示完成！不同等级的设备都已成功创建并测试。")
    print("💡 注意：同一工厂创建的组件保持了性能等级的一致性。")
    print("🔋 提示：电池电量会随着使用而减少。")
    print(f"{'='*60}")
