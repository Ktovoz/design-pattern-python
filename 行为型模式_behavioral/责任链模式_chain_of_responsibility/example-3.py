from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Dict, Any
from datetime import datetime
import json

class DeviceType(Enum):
    SECURITY = auto()
    CLIMATE = auto()
    LIGHTING = auto()
    ENTERTAINMENT = auto()
    APPLIANCE = auto()

class MessagePriority(Enum):
    EMERGENCY = auto()
    HIGH = auto()
    NORMAL = auto()
    LOW = auto()

class MessageType(Enum):
    COMMAND = auto()
    STATUS = auto()
    ALERT = auto()
    DATA = auto()

@dataclass
class SmartHomeMessage:
    device_type: DeviceType
    message_type: MessageType
    priority: MessagePriority
    timestamp: datetime
    device_id: str
    payload: Dict[str, Any]
    processed: bool = False
    processing_history: list = None

    def __post_init__(self):
        if self.processing_history is None:
            self.processing_history = []

    def add_processing_record(self, handler_name: str, action: str):
        self.processing_history.append({
            'timestamp': datetime.now(),
            'handler': handler_name,
            'action': action
        })

class MessageHandler(ABC):
    def __init__(self, name: str):
        self.name = name
        self._next_handler: Optional[MessageHandler] = None
        self._subscribed_devices: set = set()
        self._subscribed_message_types: set = set()

    def set_next(self, handler: 'MessageHandler') -> 'MessageHandler':
        self._next_handler = handler
        return handler

    def subscribe_to_device(self, device_type: DeviceType):
        self._subscribed_devices.add(device_type)

    def subscribe_to_message_type(self, message_type: MessageType):
        self._subscribed_message_types.add(message_type)

    def can_handle(self, message: SmartHomeMessage) -> bool:
        return (message.device_type in self._subscribed_devices and 
                message.message_type in self._subscribed_message_types)

    @abstractmethod
    def process_message(self, message: SmartHomeMessage) -> bool:
        pass

    def handle(self, message: SmartHomeMessage) -> bool:
        if self.can_handle(message):
            result = self.process_message(message)
            if result:
                message.processed = True
            return result
        elif self._next_handler:
            return self._next_handler.handle(message)
        return False

class SecuritySystemHandler(MessageHandler):
    def __init__(self, name: str):
        super().__init__(name)
        self.subscribe_to_device(DeviceType.SECURITY)
        self.subscribe_to_message_type(MessageType.ALERT)
        self.subscribe_to_message_type(MessageType.STATUS)

    def process_message(self, message: SmartHomeMessage) -> bool:
        if message.priority == MessagePriority.EMERGENCY:
            action = "触发紧急响应程序"
            message.add_processing_record(self.name, action)
            # 在这里可以添加实际的紧急响应逻辑
            return True
        elif message.message_type == MessageType.ALERT:
            action = "记录安全警报"
            message.add_processing_record(self.name, action)
            return True
        return False

class ClimateControlHandler(MessageHandler):
    def __init__(self, name: str):
        super().__init__(name)
        self.subscribe_to_device(DeviceType.CLIMATE)
        self.subscribe_to_message_type(MessageType.COMMAND)
        self.subscribe_to_message_type(MessageType.DATA)

    def process_message(self, message: SmartHomeMessage) -> bool:
        if message.message_type == MessageType.COMMAND:
            action = f"执行温控命令: {message.payload.get('command', 'unknown')}"
            message.add_processing_record(self.name, action)
            return True
        elif message.message_type == MessageType.DATA:
            action = "记录温度数据"
            message.add_processing_record(self.name, action)
            return True
        return False

class SmartLightingHandler(MessageHandler):
    def __init__(self, name: str):
        super().__init__(name)
        self.subscribe_to_device(DeviceType.LIGHTING)
        self.subscribe_to_message_type(MessageType.COMMAND)
        self.subscribe_to_message_type(MessageType.STATUS)

    def process_message(self, message: SmartHomeMessage) -> bool:
        if message.message_type == MessageType.COMMAND:
            action = f"控制灯光: {message.payload.get('command', 'unknown')}"
            message.add_processing_record(self.name, action)
            return True
        return False

class LoggingHandler(MessageHandler):
    def __init__(self, name: str):
        super().__init__(name)
        # 订阅所有设备类型和消息类型
        for device_type in DeviceType:
            self.subscribe_to_device(device_type)
        for message_type in MessageType:
            self.subscribe_to_message_type(message_type)

    def process_message(self, message: SmartHomeMessage) -> bool:
        action = "记录消息到系统日志"
        message.add_processing_record(self.name, action)
        return True

# 客户端代码
if __name__ == "__main__":
    # 创建处理器链
    security_handler = SecuritySystemHandler("安全系统处理器")
    climate_handler = ClimateControlHandler("温控系统处理器")
    lighting_handler = SmartLightingHandler("智能照明处理器")
    logging_handler = LoggingHandler("日志处理器")

    # 设置处理器链
    security_handler.set_next(climate_handler).set_next(lighting_handler).set_next(logging_handler)

    # 创建测试消息
    messages = [
        SmartHomeMessage(
            device_type=DeviceType.SECURITY,
            message_type=MessageType.ALERT,
            priority=MessagePriority.EMERGENCY,
            timestamp=datetime.now(),
            device_id="security_cam_01",
            payload={"alert_type": "intrusion", "location": "front_door"}
        ),
        SmartHomeMessage(
            device_type=DeviceType.CLIMATE,
            message_type=MessageType.COMMAND,
            priority=MessagePriority.NORMAL,
            timestamp=datetime.now(),
            device_id="thermostat_01",
            payload={"command": "set_temperature", "value": 23}
        ),
        SmartHomeMessage(
            device_type=DeviceType.LIGHTING,
            message_type=MessageType.COMMAND,
            priority=MessagePriority.LOW,
            timestamp=datetime.now(),
            device_id="living_room_lights",
            payload={"command": "dim", "level": 50}
        )
    ]

    # 处理消息
    for message in messages:
        print(f"\n处理来自 {message.device_id} 的消息:")
        security_handler.handle(message)
        print(f"消息类型: {message.message_type.name}")
        print(f"处理历史:")
        for record in message.processing_history:
            print(f"- {record['handler']}: {record['action']}")
