from abc import ABC, abstractmethod
from datetime import datetime
import json

# 访问者接口
class SmartHomeVisitor(ABC):
    @abstractmethod
    def visit_light(self, light):
        pass
    
    @abstractmethod
    def visit_thermostat(self, thermostat):
        pass
    
    @abstractmethod
    def visit_security_camera(self, camera):
        pass
    
    @abstractmethod
    def visit_speaker(self, speaker):
        pass

# 具体访问者 - 状态监控器
class StatusMonitor(SmartHomeVisitor):
    def visit_light(self, light):
        return {
            "设备类型": "智能灯",
            "状态": "开启" if light.is_on else "关闭",
            "亮度": f"{light.brightness}%",
            "最后更新时间": light.last_update
        }

    def visit_thermostat(self, thermostat):
        return {
            "设备类型": "温控器",
            "当前温度": f"{thermostat.current_temp}°C",
            "目标温度": f"{thermostat.target_temp}°C",
            "模式": thermostat.mode,
            "最后更新时间": thermostat.last_update
        }

    def visit_security_camera(self, camera):
        return {
            "设备类型": "安防摄像头",
            "状态": "在线" if camera.is_online else "离线",
            "录制状态": "正在录制" if camera.is_recording else "未录制",
            "最后更新时间": camera.last_update
        }

    def visit_speaker(self, speaker):
        return {
            "设备类型": "智能音箱",
            "状态": "播放中" if speaker.is_playing else "待机",
            "音量": f"{speaker.volume}%",
            "当前播放": speaker.current_track,
            "最后更新时间": speaker.last_update
        }

# 具体访问者 - 能源消耗分析器
class EnergyAnalyzer(SmartHomeVisitor):
    def __init__(self):
        self.total_consumption = 0
        self.device_consumption = {}

    def visit_light(self, light):
        consumption = light.brightness * 0.1 if light.is_on else 0
        self.device_consumption[light.name] = consumption
        self.total_consumption += consumption

    def visit_thermostat(self, thermostat):
        consumption = abs(thermostat.current_temp - thermostat.target_temp) * 2
        self.device_consumption[thermostat.name] = consumption
        self.total_consumption += consumption

    def visit_security_camera(self, camera):
        consumption = 5 if camera.is_recording else 1
        self.device_consumption[camera.name] = consumption
        self.total_consumption += consumption

    def visit_speaker(self, speaker):
        consumption = speaker.volume * 0.05 if speaker.is_playing else 0.1
        self.device_consumption[speaker.name] = consumption
        self.total_consumption += consumption

    def get_report(self):
        return {
            "总能耗": f"{self.total_consumption:.2f} kWh",
            "设备能耗": self.device_consumption
        }

# 智能家居设备接口
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @abstractmethod
    def accept(self, visitor):
        pass

# 具体设备类
class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.is_on = False
        self.brightness = 0

    def accept(self, visitor):
        return visitor.visit_light(self)

    def turn_on(self, brightness=100):
        self.is_on = True
        self.brightness = brightness
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Thermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.current_temp = 25
        self.target_temp = 22
        self.mode = "自动"

    def accept(self, visitor):
        return visitor.visit_thermostat(self)

    def set_temperature(self, temp):
        self.target_temp = temp
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class SecurityCamera(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.is_online = True
        self.is_recording = False

    def accept(self, visitor):
        return visitor.visit_security_camera(self)

    def start_recording(self):
        self.is_recording = True
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def stop_recording(self):
        self.is_recording = False
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class SmartSpeaker(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.is_playing = False
        self.volume = 50
        self.current_track = None

    def accept(self, visitor):
        return visitor.visit_speaker(self)

    def play_music(self, track, volume=50):
        self.is_playing = True
        self.volume = volume
        self.current_track = track
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def stop_music(self):
        self.is_playing = False
        self.current_track = None
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 使用示例
if __name__ == "__main__":
    # 创建智能家居设备
    living_room_light = SmartLight("客厅灯")
    bedroom_thermostat = Thermostat("卧室温控器")
    front_door_camera = SecurityCamera("前门摄像头")
    kitchen_speaker = SmartSpeaker("厨房音箱")
    
    # 设置设备状态
    living_room_light.turn_on(80)
    bedroom_thermostat.set_temperature(23)
    front_door_camera.start_recording()
    kitchen_speaker.play_music("轻音乐", 60)
    
    # 创建访问者
    status_monitor = StatusMonitor()
    energy_analyzer = EnergyAnalyzer()
    
    # 获取设备状态
    print("设备状态监控：")
    devices = [living_room_light, bedroom_thermostat, front_door_camera, kitchen_speaker]
    for device in devices:
        print(f"\n{device.name}状态：")
        print(json.dumps(device.accept(status_monitor), ensure_ascii=False, indent=2))
    
    # 分析能源消耗
    print("\n能源消耗分析：")
    for device in devices:
        device.accept(energy_analyzer)
    print(json.dumps(energy_analyzer.get_report(), ensure_ascii=False, indent=2))
