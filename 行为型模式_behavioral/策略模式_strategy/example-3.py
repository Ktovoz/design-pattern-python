from abc import ABC, abstractmethod
from datetime import datetime, time
from typing import Dict, List

# 智能家居设备接口
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_status(self) -> str:
        pass

# 具体设备：智能灯
class SmartLight(SmartDevice):
    def __init__(self, name: str):
        self.name = name
        self.is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        print(f"{self.name}已开启，亮度100%")
    
    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        print(f"{self.name}已关闭")
    
    def get_status(self) -> str:
        return f"{self.name}: {'开启' if self.is_on else '关闭'}，亮度{self.brightness}%"

# 具体设备：智能空调
class SmartAC(SmartDevice):
    def __init__(self, name: str):
        self.name = name
        self.is_on = False
        self.temperature = 26
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name}已开启，温度{self.temperature}°C")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name}已关闭")
    
    def get_status(self) -> str:
        return f"{self.name}: {'开启' if self.is_on else '关闭'}，温度{self.temperature}°C"

# 场景策略接口
class SceneStrategy(ABC):
    @abstractmethod
    def apply(self, devices: Dict[str, SmartDevice]):
        pass

# 具体策略：回家模式
class HomeScene(SceneStrategy):
    def apply(self, devices: Dict[str, SmartDevice]):
        print("\n=== 回家模式 ===")
        devices["客厅灯"].turn_on()
        devices["空调"].turn_on()
        print("欢迎回家！已开启客厅灯和空调")

# 具体策略：睡眠模式
class SleepScene(SceneStrategy):
    def apply(self, devices: Dict[str, SmartDevice]):
        print("\n=== 睡眠模式 ===")
        devices["客厅灯"].turn_off()
        devices["卧室灯"].turn_on()
        devices["空调"].turn_on()
        print("晚安！已调整到睡眠模式")

# 具体策略：离家模式
class AwayScene(SceneStrategy):
    def apply(self, devices: Dict[str, SmartDevice]):
        print("\n=== 离家模式 ===")
        for device in devices.values():
            device.turn_off()
        print("所有设备已关闭，祝您外出愉快！")

# 智能家居控制器
class SmartHomeController:
    def __init__(self):
        self.devices: Dict[str, SmartDevice] = {}
        self._current_scene: SceneStrategy = None
    
    def add_device(self, name: str, device: SmartDevice):
        self.devices[name] = device
    
    def set_scene(self, scene: SceneStrategy):
        self._current_scene = scene
    
    def apply_scene(self):
        if not self._current_scene:
            print("请先设置场景")
            return
        self._current_scene.apply(self.devices)
    
    def get_all_status(self) -> List[str]:
        return [device.get_status() for device in self.devices.values()]

# 使用示例
if __name__ == "__main__":
    # 创建智能家居控制器
    controller = SmartHomeController()
    
    # 添加设备
    controller.add_device("客厅灯", SmartLight("客厅灯"))
    controller.add_device("卧室灯", SmartLight("卧室灯"))
    controller.add_device("空调", SmartAC("空调"))
    
    # 测试不同场景
    print("=== 智能家居场景测试 ===")
    
    # 回家模式
    controller.set_scene(HomeScene())
    controller.apply_scene()
    print("\n当前状态:")
    for status in controller.get_all_status():
        print(status)
    
    # 睡眠模式
    controller.set_scene(SleepScene())
    controller.apply_scene()
    print("\n当前状态:")
    for status in controller.get_all_status():
        print(status)
    
    # 离家模式
    controller.set_scene(AwayScene())
    controller.apply_scene()
    print("\n当前状态:")
    for status in controller.get_all_status():
        print(status)
