from abc import ABC, abstractmethod
from typing import List

# 设备接口（实现部分）
class SmartDevice(ABC):
    @abstractmethod
    def get_status(self) -> str:
        pass
    
    @abstractmethod
    def turn_on(self) -> str:
        pass
    
    @abstractmethod
    def turn_off(self) -> str:
        pass

# 具体设备实现
class SmartLight(SmartDevice):
    def __init__(self, location: str):
        self.location = location
        self.is_on = False
    
    def get_status(self) -> str:
        return f"{self.location}的灯：{'开启' if self.is_on else '关闭'}"
    
    def turn_on(self) -> str:
        self.is_on = True
        return f"{self.location}的灯已开启"
    
    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.location}的灯已关闭"

class SmartThermostat(SmartDevice):
    def __init__(self, location: str):
        self.location = location
        self.temperature = 25
        self.is_on = False
    
    def get_status(self) -> str:
        return f"{self.location}的温控器：{'开启' if self.is_on else '关闭'}，温度：{self.temperature}°C"
    
    def turn_on(self) -> str:
        self.is_on = True
        return f"{self.location}的温控器已开启"
    
    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.location}的温控器已关闭"

# 控制接口（抽象部分）
class SmartController(ABC):
    def __init__(self, devices: List[SmartDevice]):
        self.devices = devices
    
    @abstractmethod
    def control_all_devices(self, action: str) -> List[str]:
        pass

# 具体控制器实现
class VoiceController(SmartController):
    def control_all_devices(self, action: str) -> List[str]:
        results = []
        for device in self.devices:
            if action == "开启":
                results.append(f"语音控制：{device.turn_on()}")
            elif action == "关闭":
                results.append(f"语音控制：{device.turn_off()}")
            elif action == "状态":
                results.append(f"语音查询：{device.get_status()}")
        return results

class AppController(SmartController):
    def control_all_devices(self, action: str) -> List[str]:
        results = []
        for device in self.devices:
            if action == "开启":
                results.append(f"APP控制：{device.turn_on()}")
            elif action == "关闭":
                results.append(f"APP控制：{device.turn_off()}")
            elif action == "状态":
                results.append(f"APP查询：{device.get_status()}")
        return results

# 使用示例
if __name__ == "__main__":
    # 创建智能设备
    living_room_light = SmartLight("客厅")
    bedroom_light = SmartLight("卧室")
    living_room_thermostat = SmartThermostat("客厅")
    bedroom_thermostat = SmartThermostat("卧室")
    
    # 创建设备列表
    all_devices = [
        living_room_light,
        bedroom_light,
        living_room_thermostat,
        bedroom_thermostat
    ]
    
    # 创建不同类型的控制器
    voice_controller = VoiceController(all_devices)
    app_controller = AppController(all_devices)
    
    # 使用语音控制器
    print("=== 使用语音控制器 ===")
    print("\n开启所有设备：")
    for result in voice_controller.control_all_devices("开启"):
        print(result)
    
    print("\n查询所有设备状态：")
    for result in voice_controller.control_all_devices("状态"):
        print(result)
    
    # 使用APP控制器
    print("\n=== 使用APP控制器 ===")
    print("\n关闭所有设备：")
    for result in app_controller.control_all_devices("关闭"):
        print(result)
    
    print("\n查询所有设备状态：")
    for result in app_controller.control_all_devices("状态"):
        print(result)
