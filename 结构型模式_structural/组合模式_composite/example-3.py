from abc import ABC, abstractmethod
from typing import List, Dict
from enum import Enum
import time

class DeviceStatus(Enum):
    ON = "开启"
    OFF = "关闭"
    STANDBY = "待机"

class SmartDevice(ABC):
    def __init__(self, name: str):
        self._name = name
        self._status = DeviceStatus.OFF
        self._power_consumption = 0.0

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

    @abstractmethod
    def get_power_consumption(self) -> float:
        pass

# 叶子节点 - 具体设备
class Light(SmartDevice):
    def __init__(self, name: str, brightness: int = 100):
        super().__init__(name)
        self._brightness = brightness
        self._power_consumption = 0.05  # 千瓦时

    def turn_on(self):
        self._status = DeviceStatus.ON
        print(f"{self._name} 已开启，亮度: {self._brightness}%")

    def turn_off(self):
        self._status = DeviceStatus.OFF
        print(f"{self._name} 已关闭")

    def get_status(self) -> str:
        return f"{self._name}: {self._status.value}"

    def get_power_consumption(self) -> float:
        return self._power_consumption if self._status == DeviceStatus.ON else 0.0

class Thermostat(SmartDevice):
    def __init__(self, name: str, temperature: float = 25.0):
        super().__init__(name)
        self._temperature = temperature
        self._power_consumption = 1.5  # 千瓦时

    def turn_on(self):
        self._status = DeviceStatus.ON
        print(f"{self._name} 已开启，温度设置为 {self._temperature}°C")

    def turn_off(self):
        self._status = DeviceStatus.OFF
        print(f"{self._name} 已关闭")

    def get_status(self) -> str:
        return f"{self._name}: {self._status.value}, 温度: {self._temperature}°C"

    def get_power_consumption(self) -> float:
        return self._power_consumption if self._status == DeviceStatus.ON else 0.0

# 组合节点 - 房间
class Room(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self._devices: List[SmartDevice] = []

    def add_device(self, device: SmartDevice):
        self._devices.append(device)

    def remove_device(self, device: SmartDevice):
        self._devices.remove(device)

    def turn_on(self):
        self._status = DeviceStatus.ON
        print(f"\n{self._name} 所有设备开启中...")
        for device in self._devices:
            device.turn_on()

    def turn_off(self):
        self._status = DeviceStatus.OFF
        print(f"\n{self._name} 所有设备关闭中...")
        for device in self._devices:
            device.turn_off()

    def get_status(self) -> str:
        status = f"{self._name} 状态:\n"
        for device in self._devices:
            status += f"  - {device.get_status()}\n"
        return status

    def get_power_consumption(self) -> float:
        return sum(device.get_power_consumption() for device in self._devices)

# 组合节点 - 智能家居系统
class SmartHome(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self._rooms: Dict[str, Room] = {}

    def add_room(self, room: Room):
        self._rooms[room._name] = room

    def remove_room(self, room_name: str):
        if room_name in self._rooms:
            del self._rooms[room_name]

    def turn_on(self):
        self._status = DeviceStatus.ON
        print(f"\n=== {self._name} 系统启动 ===")
        for room in self._rooms.values():
            room.turn_on()

    def turn_off(self):
        self._status = DeviceStatus.OFF
        print(f"\n=== {self._name} 系统关闭 ===")
        for room in self._rooms.values():
            room.turn_off()

    def get_status(self) -> str:
        status = f"\n=== {self._name} 系统状态 ===\n"
        for room in self._rooms.values():
            status += room.get_status()
        return status

    def get_power_consumption(self) -> float:
        return sum(room.get_power_consumption() for room in self._rooms.values())

# 使用示例
if __name__ == "__main__":
    # 创建智能家居系统
    smart_home = SmartHome("我的智能家居")

    # 创建客厅
    living_room = Room("客厅")
    living_room.add_device(Light("主灯"))
    living_room.add_device(Light("氛围灯"))
    living_room.add_device(Thermostat("空调", 26.0))

    # 创建卧室
    bedroom = Room("主卧")
    bedroom.add_device(Light("床头灯"))
    bedroom.add_device(Thermostat("空调", 24.0))

    # 添加房间到系统
    smart_home.add_room(living_room)
    smart_home.add_room(bedroom)

    # 演示系统操作
    print("\n=== 智能家居系统演示 ===")
    
    # 开启系统
    smart_home.turn_on()
    time.sleep(1)
    
    # 显示状态
    print(smart_home.get_status())
    
    # 显示总功耗
    print(f"\n当前总功耗: {smart_home.get_power_consumption():.2f} 千瓦时")
    
    # 关闭系统
    smart_home.turn_off()
