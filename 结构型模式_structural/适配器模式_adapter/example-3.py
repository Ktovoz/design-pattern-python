from abc import ABC, abstractmethod
from typing import Dict, Any, List
from enum import Enum

class DeviceType(Enum):
    LIGHT = "light"
    THERMOSTAT = "thermostat"
    SPEAKER = "speaker"

# 目标接口 - 智能家居系统
class SmartHomeSystem(ABC):
    @abstractmethod
    def control_device(self, device_id: str, command: str, params: Dict[str, Any] = None) -> str:
        pass

    @abstractmethod
    def get_device_status(self, device_id: str) -> Dict[str, Any]:
        pass

# 适配者接口 - 智能设备
class SmartDevice(ABC):
    @abstractmethod
    def execute_command(self, command: str, params: Dict[str, Any] = None) -> bool:
        pass

    @abstractmethod
    def get_status(self) -> Dict[str, Any]:
        pass

# 具体适配者 - 小米智能灯
class XiaomiLight(SmartDevice):
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.brightness = 0
        self.is_on = False

    def execute_command(self, command: str, params: Dict[str, Any] = None) -> bool:
        if command == "turn_on":
            self.is_on = True
            return True
        elif command == "turn_off":
            self.is_on = False
            return True
        elif command == "set_brightness" and params and "level" in params:
            self.brightness = params["level"]
            return True
        return False

    def get_status(self) -> Dict[str, Any]:
        return {
            "device_id": self.device_id,
            "type": DeviceType.LIGHT.value,
            "is_on": self.is_on,
            "brightness": self.brightness
        }

# 具体适配者 - 华为智能音箱
class HuaweiSpeaker(SmartDevice):
    def __init__(self, device_id: str):
        self.device_id = device_id
        self.volume = 50
        self.is_playing = False

    def execute_command(self, command: str, params: Dict[str, Any] = None) -> bool:
        if command == "play":
            self.is_playing = True
            return True
        elif command == "stop":
            self.is_playing = False
            return True
        elif command == "set_volume" and params and "level" in params:
            self.volume = params["level"]
            return True
        return False

    def get_status(self) -> Dict[str, Any]:
        return {
            "device_id": self.device_id,
            "type": DeviceType.SPEAKER.value,
            "is_playing": self.is_playing,
            "volume": self.volume
        }

# 适配器 - 智能家居适配器
class SmartHomeAdapter(SmartHomeSystem):
    def __init__(self):
        self.devices: Dict[str, SmartDevice] = {}

    def add_device(self, device: SmartDevice):
        self.devices[device.device_id] = device

    def control_device(self, device_id: str, command: str, params: Dict[str, Any] = None) -> str:
        if device_id not in self.devices:
            return f"设备 {device_id} 未找到"
        
        device = self.devices[device_id]
        success = device.execute_command(command, params)
        if success:
            return f"设备 {device_id} 执行命令 {command} 成功"
        return f"设备 {device_id} 执行命令 {command} 失败"

    def get_device_status(self, device_id: str) -> Dict[str, Any]:
        if device_id not in self.devices:
            return {"error": f"设备 {device_id} 未找到"}
        return self.devices[device_id].get_status()

def main():
    # 创建智能家居适配器
    smart_home = SmartHomeAdapter()
    
    # 创建设备
    light = XiaomiLight("light_001")
    speaker = HuaweiSpeaker("speaker_001")
    
    # 添加设备到系统
    smart_home.add_device(light)
    smart_home.add_device(speaker)
    
    # 控制设备
    print(smart_home.control_device("light_001", "turn_on"))
    print(smart_home.control_device("light_001", "set_brightness", {"level": 80}))
    print(smart_home.control_device("speaker_001", "play"))
    print(smart_home.control_device("speaker_001", "set_volume", {"level": 75}))
    
    # 获取设备状态
    print("\n设备状态:")
    print(smart_home.get_device_status("light_001"))
    print(smart_home.get_device_status("speaker_001"))

if __name__ == "__main__":
    main()
