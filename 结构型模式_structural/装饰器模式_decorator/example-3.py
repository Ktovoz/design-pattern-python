from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

# 基础组件接口
class SmartDevice(ABC):
    @abstractmethod
    def get_status(self) -> Dict[str, any]:
        pass

    @abstractmethod
    def execute_command(self, command: str) -> bool:
        pass

    @abstractmethod
    def get_energy_consumption(self) -> float:
        pass

# 具体组件
class BasicLight(SmartDevice):
    def __init__(self):
        self._is_on = False
        self._brightness = 0
        self._color = "white"

    def get_status(self) -> Dict[str, any]:
        return {
            "is_on": self._is_on,
            "brightness": self._brightness,
            "color": self._color,
            "type": "基础灯"
        }

    def execute_command(self, command: str) -> bool:
        if command == "turn_on":
            self._is_on = True
            return True
        elif command == "turn_off":
            self._is_on = False
            return True
        return False

    def get_energy_consumption(self) -> float:
        return 10.0 if self._is_on else 0.0

# 装饰器基类
class SmartDeviceDecorator(SmartDevice):
    def __init__(self, device: SmartDevice):
        self._device = device

    def get_status(self) -> Dict[str, any]:
        return self._device.get_status()

    def execute_command(self, command: str) -> bool:
        return self._device.execute_command(command)

    def get_energy_consumption(self) -> float:
        return self._device.get_energy_consumption()

# 具体装饰器
class ColorControlDecorator(SmartDeviceDecorator):
    def __init__(self, device: SmartDevice):
        super().__init__(device)
        self._available_colors = ["red", "green", "blue", "yellow", "purple"]

    def get_status(self) -> Dict[str, any]:
        status = self._device.get_status()
        status["available_colors"] = self._available_colors
        status["type"] = "彩色灯"
        return status

    def execute_command(self, command: str) -> bool:
        if command.startswith("set_color:"):
            color = command.split(":")[1]
            if color in self._available_colors:
                status = self._device.get_status()
                status["color"] = color
                return True
        return self._device.execute_command(command)

    def get_energy_consumption(self) -> float:
        return self._device.get_energy_consumption() * 1.2

class DimmingControlDecorator(SmartDeviceDecorator):
    def __init__(self, device: SmartDevice):
        super().__init__(device)
        self._max_brightness = 100

    def get_status(self) -> Dict[str, any]:
        status = self._device.get_status()
        status["max_brightness"] = self._max_brightness
        status["type"] = "可调光灯"
        return status

    def execute_command(self, command: str) -> bool:
        if command.startswith("set_brightness:"):
            try:
                brightness = int(command.split(":")[1])
                if 0 <= brightness <= self._max_brightness:
                    status = self._device.get_status()
                    status["brightness"] = brightness
                    return True
            except ValueError:
                pass
        return self._device.execute_command(command)

    def get_energy_consumption(self) -> float:
        status = self._device.get_status()
        brightness_factor = status["brightness"] / self._max_brightness
        return self._device.get_energy_consumption() * brightness_factor

class ScheduleControlDecorator(SmartDeviceDecorator):
    def __init__(self, device: SmartDevice):
        super().__init__(device)
        self._schedule = {}

    def get_status(self) -> Dict[str, any]:
        status = self._device.get_status()
        status["schedule"] = self._schedule
        status["type"] = "定时灯"
        return status

    def execute_command(self, command: str) -> bool:
        if command.startswith("set_schedule:"):
            try:
                time, action = command.split(":")[1].split(",")
                self._schedule[time] = action
                return True
            except ValueError:
                pass
        return self._device.execute_command(command)

    def get_energy_consumption(self) -> float:
        current_time = datetime.now().strftime("%H:%M")
        if current_time in self._schedule:
            command = self._schedule[current_time]
            self._device.execute_command(command)
        return self._device.get_energy_consumption()

# 使用示例
if __name__ == "__main__":
    # 创建基础灯
    light = BasicLight()
    print("基础灯状态：")
    print(light.get_status())
    print(f"能耗: {light.get_energy_consumption()}W")

    # 添加颜色控制
    color_light = ColorControlDecorator(light)
    print("\n添加颜色控制后：")
    color_light.execute_command("set_color:blue")
    print(color_light.get_status())
    print(f"能耗: {color_light.get_energy_consumption()}W")

    # 添加亮度控制
    dimmable_light = DimmingControlDecorator(color_light)
    print("\n添加亮度控制后：")
    dimmable_light.execute_command("set_brightness:50")
    print(dimmable_light.get_status())
    print(f"能耗: {dimmable_light.get_energy_consumption()}W")

    # 添加定时控制
    scheduled_light = ScheduleControlDecorator(dimmable_light)
    print("\n添加定时控制后：")
    scheduled_light.execute_command("set_schedule:08:00,turn_on")
    scheduled_light.execute_command("set_schedule:22:00,turn_off")
    print(scheduled_light.get_status())
    print(f"能耗: {scheduled_light.get_energy_consumption()}W")
