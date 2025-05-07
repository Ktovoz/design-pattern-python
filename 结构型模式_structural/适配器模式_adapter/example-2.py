from abc import ABC, abstractmethod
from typing import List

# 目标接口 - 电脑USB接口
class ComputerUSB(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass

# 适配者接口 - 各种USB设备
class USBDevice(ABC):
    @abstractmethod
    def get_data(self) -> List[str]:
        pass

# 具体适配者 - USB鼠标
class USBMouse(USBDevice):
    def get_data(self) -> List[str]:
        return ["鼠标移动", "鼠标点击"]

# 具体适配者 - USB键盘
class USBKeyboard(USBDevice):
    def get_data(self) -> List[str]:
        return ["键盘输入", "特殊按键"]

# 适配器 - USB集线器
class USBHub(ComputerUSB):
    def __init__(self):
        self.devices: List[USBDevice] = []

    def add_device(self, device: USBDevice):
        self.devices.append(device)

    def connect(self) -> str:
        results = []
        for device in self.devices:
            data = device.get_data()
            results.extend(data)
        return f"USB集线器连接成功，设备数据: {', '.join(results)}"

def main():
    # 创建USB设备
    mouse = USBMouse()
    keyboard = USBKeyboard()
    
    # 创建USB集线器
    hub = USBHub()
    
    # 添加设备到集线器
    hub.add_device(mouse)
    hub.add_device(keyboard)
    
    # 连接到电脑
    print(hub.connect())

if __name__ == "__main__":
    main()
