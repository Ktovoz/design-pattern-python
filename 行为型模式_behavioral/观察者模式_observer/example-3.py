from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Set
import random
import time
from datetime import datetime

class DeviceStatus(Enum):
    ON = "开启"
    OFF = "关闭"
    ERROR = "错误"

class DeviceType(Enum):
    LIGHT = "智能灯"
    AC = "空调"
    CURTAIN = "窗帘"
    SECURITY = "安防系统"

class HomeEvent:
    def __init__(self, event_type: str, device_type: DeviceType, status: DeviceStatus, data: dict = None):
        self.timestamp = datetime.now()
        self.event_type = event_type
        self.device_type = device_type
        self.status = status
        self.data = data or {}

class SmartHomeHub:
    def __init__(self):
        self._observers: Dict[str, Set['HomeObserver']] = {}
        self._devices: Dict[str, 'SmartDevice'] = {}
        self._initialize_event_types()

    def _initialize_event_types(self):
        self._observers = {
            "status_change": set(),
            "security_alert": set(),
            "energy_report": set(),
            "automation": set()
        }

    def attach(self, event_type: str, observer: 'HomeObserver'):
        if event_type in self._observers:
            self._observers[event_type].add(observer)

    def detach(self, event_type: str, observer: 'HomeObserver'):
        if event_type in self._observers:
            self._observers[event_type].discard(observer)

    def notify(self, event_type: str, event: HomeEvent):
        if event_type in self._observers:
            for observer in self._observers[event_type]:
                observer.update(event)

    def add_device(self, device: 'SmartDevice'):
        self._devices[device.id] = device
        device.set_hub(self)

    def process_event(self, event: HomeEvent):
        self.notify(event.event_type, event)

class SmartDevice:
    def __init__(self, device_id: str, device_type: DeviceType):
        self.id = device_id
        self.type = device_type
        self.status = DeviceStatus.OFF
        self._hub = None

    def set_hub(self, hub: SmartHomeHub):
        self._hub = hub

    def change_status(self, new_status: DeviceStatus, additional_data: dict = None):
        self.status = new_status
        if self._hub:
            event = HomeEvent("status_change", self.type, new_status, additional_data)
            self._hub.process_event(event)

class HomeObserver(ABC):
    @abstractmethod
    def update(self, event: HomeEvent):
        pass

class MobileApp(HomeObserver):
    def __init__(self, user_name: str):
        self.user_name = user_name

    def update(self, event: HomeEvent):
        print(f"\n[手机APP - {self.user_name}] 收到通知:")
        print(f"时间: {event.timestamp.strftime('%H:%M:%S')}")
        print(f"设备: {event.device_type.value}")
        print(f"状态: {event.status.value}")
        if event.data:
            print("详细信息:", event.data)

class AutomationController(HomeObserver):
    def update(self, event: HomeEvent):
        if event.event_type == "status_change":
            if event.device_type == DeviceType.LIGHT and event.status == DeviceStatus.ON:
                print(f"\n[自动化控制器] 检测到灯光开启，正在调整窗帘...")
                # 这里可以触发窗帘的相关操作

class SecuritySystem(HomeObserver):
    def update(self, event: HomeEvent):
        if event.event_type == "security_alert":
            print(f"\n[安防系统] ⚠️ 安全警报！")
            print(f"时间: {event.timestamp.strftime('%H:%M:%S')}")
            print(f"设备: {event.device_type.value}")
            print(f"详情: {event.data.get('alert_message', '未知警报')}")

class EnergyMonitor(HomeObserver):
    def __init__(self):
        self.device_runtime: Dict[str, float] = {}

    def update(self, event: HomeEvent):
        if event.event_type == "status_change":
            device_id = f"{event.device_type.value}"
            if event.status == DeviceStatus.ON:
                print(f"\n[能源监控] 设备 {device_id} 开始运行")
                self.device_runtime[device_id] = time.time()
            elif event.status == DeviceStatus.OFF and device_id in self.device_runtime:
                runtime = time.time() - self.device_runtime[device_id]
                print(f"\n[能源监控] 设备 {device_id} 运行时长: {runtime:.1f} 秒")
                del self.device_runtime[device_id]

# 使用示例
if __name__ == "__main__":
    # 创建智能家居中枢
    smart_home = SmartHomeHub()

    # 创建设备
    living_room_light = SmartDevice("light_001", DeviceType.LIGHT)
    bedroom_ac = SmartDevice("ac_001", DeviceType.AC)
    security_system = SmartDevice("security_001", DeviceType.SECURITY)

    # 添加设备到中枢
    smart_home.add_device(living_room_light)
    smart_home.add_device(bedroom_ac)
    smart_home.add_device(security_system)

    # 创建观察者
    mobile_app = MobileApp("张三")
    automation = AutomationController()
    security = SecuritySystem()
    energy = EnergyMonitor()

    # 注册观察者
    smart_home.attach("status_change", mobile_app)
    smart_home.attach("status_change", automation)
    smart_home.attach("status_change", energy)
    smart_home.attach("security_alert", security)

    # 模拟一天中的设备操作
    print("模拟智能家居系统运行...")
    
    # 模拟开灯
    living_room_light.change_status(DeviceStatus.ON, {"brightness": "80%"})
    time.sleep(2)

    # 模拟开空调
    bedroom_ac.change_status(DeviceStatus.ON, {"temperature": "24°C", "mode": "制冷"})
    time.sleep(2)

    # 模拟安防警报
    security_event = HomeEvent(
        "security_alert",
        DeviceType.SECURITY,
        DeviceStatus.ERROR,
        {"alert_message": "检测到异常移动"}
    )
    smart_home.process_event(security_event)
    time.sleep(2)

    # 模拟关闭设备
    living_room_light.change_status(DeviceStatus.OFF)
    bedroom_ac.change_status(DeviceStatus.OFF)
