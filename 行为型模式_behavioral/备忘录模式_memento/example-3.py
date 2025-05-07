from typing import Dict, List, Any
from datetime import datetime
import json

class DeviceState:
    """设备状态类"""
    def __init__(self, device_id: str, status: str, settings: Dict[str, Any]):
        self.device_id = device_id
        self.status = status
        self.settings = settings
        self.timestamp = datetime.now()

class SceneState:
    """场景状态类"""
    def __init__(self, scene_name: str, devices: List[DeviceState]):
        self.scene_name = scene_name
        self.devices = devices
        self.timestamp = datetime.now()

class SceneMemento:
    """场景备忘录类"""
    def __init__(self, state: SceneState):
        self.state = state

class SmartHome:
    """智能家居系统类"""
    def __init__(self):
        self.devices: Dict[str, DeviceState] = {}
        self.scenes: Dict[str, SceneMemento] = {}
        self.current_scene: str = None

    def add_device(self, device_id: str, initial_settings: Dict[str, Any]):
        """添加设备"""
        self.devices[device_id] = DeviceState(
            device_id,
            "off",
            initial_settings
        )

    def update_device(self, device_id: str, status: str = None, settings: Dict[str, Any] = None):
        """更新设备状态"""
        if device_id in self.devices:
            device = self.devices[device_id]
            if status:
                device.status = status
            if settings:
                device.settings.update(settings)

    def create_scene(self, scene_name: str):
        """创建场景"""
        devices_state = [DeviceState(
            device.device_id,
            device.status,
            device.settings.copy()
        ) for device in self.devices.values()]
        
        scene_state = SceneState(scene_name, devices_state)
        self.scenes[scene_name] = SceneMemento(scene_state)

    def activate_scene(self, scene_name: str):
        """激活场景"""
        if scene_name in self.scenes:
            scene = self.scenes[scene_name].state
            for device_state in scene.devices:
                self.devices[device_state.device_id] = DeviceState(
                    device_state.device_id,
                    device_state.status,
                    device_state.settings.copy()
                )
            self.current_scene = scene_name
            return True
        return False

    def get_scene_info(self, scene_name: str) -> Dict[str, Any]:
        """获取场景信息"""
        if scene_name in self.scenes:
            scene = self.scenes[scene_name].state
            return {
                "name": scene.scene_name,
                "timestamp": scene.timestamp,
                "devices": [
                    {
                        "id": device.device_id,
                        "status": device.status,
                        "settings": device.settings
                    }
                    for device in scene.devices
                ]
            }
        return None

def main():
    # 创建智能家居系统
    home = SmartHome()
    
    # 添加设备
    home.add_device("light1", {"brightness": 50, "color": "white"})
    home.add_device("thermostat", {"temperature": 22, "mode": "auto"})
    home.add_device("speaker", {"volume": 30, "source": "bluetooth"})
    
    # 更新设备状态
    home.update_device("light1", "on", {"brightness": 80})
    home.update_device("thermostat", "on", {"temperature": 24})
    
    # 创建"回家"场景
    home.create_scene("回家")
    
    # 更新设备状态
    home.update_device("light1", "off", {"brightness": 0})
    home.update_device("thermostat", "off", {"temperature": 18})
    home.update_device("speaker", "off", {"volume": 0})
    
    # 创建"离家"场景
    home.create_scene("离家")
    
    # 激活"回家"场景
    home.activate_scene("回家")
    print("\n激活'回家'场景后的状态：")
    for device_id, device in home.devices.items():
        print(f"{device_id}: 状态={device.status}, 设置={device.settings}")
    
    # 激活"离家"场景
    home.activate_scene("离家")
    print("\n激活'离家'场景后的状态：")
    for device_id, device in home.devices.items():
        print(f"{device_id}: 状态={device.status}, 设置={device.settings}")
    
    # 获取场景信息
    print("\n'回家'场景信息：")
    print(json.dumps(home.get_scene_info("回家"), indent=2, default=str))

if __name__ == "__main__":
    main()
