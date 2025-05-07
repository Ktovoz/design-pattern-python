#!/usr/bin/env python
# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from datetime import datetime, time
import json

class SmartHomeSystem(ABC):
    """智能家居系统基类"""
    
    def __init__(self, room_name: str):
        self.room_name = room_name
        self.devices: Dict[str, bool] = {}  # 设备状态
        self.temperature: float = 22.0
        self.humidity: float = 50.0
        self.light_intensity: int = 0
        
    def execute_scene(self, time_of_day: str) -> None:
        """模板方法"""
        print(f"\n执行{self.room_name} - {time_of_day}场景")
        self.check_system_status()
        self.adjust_temperature(time_of_day)
        self.adjust_lighting(time_of_day)
        self.control_curtains(time_of_day)
        if self.has_special_requirements():
            self.handle_special_requirements()
        self.save_energy()
        self.log_scene_execution(time_of_day)
    
    def check_system_status(self) -> None:
        """检查系统状态"""
        print(f"检查{self.room_name}所有设备状态")
        self.devices = {
            "空调": True,
            "灯光": True,
            "窗帘": True,
            "新风系统": True
        }
    
    @abstractmethod
    def adjust_temperature(self, time_of_day: str) -> None:
        """调节温度"""
        pass
    
    @abstractmethod
    def adjust_lighting(self, time_of_day: str) -> None:
        """调节灯光"""
        pass
    
    @abstractmethod
    def control_curtains(self, time_of_day: str) -> None:
        """控制窗帘"""
        pass
    
    def has_special_requirements(self) -> bool:
        """是否有特殊要求"""
        return False
    
    @abstractmethod
    def handle_special_requirements(self) -> None:
        """处理特殊要求"""
        pass
    
    def save_energy(self) -> None:
        """节能模式"""
        print(f"检查{self.room_name}是否有未使用的设备并关闭")
        for device, status in self.devices.items():
            if status:
                print(f"关闭未使用的{device}")
    
    def log_scene_execution(self, time_of_day: str) -> None:
        """记录场景执行日志"""
        log = {
            "room": self.room_name,
            "scene": time_of_day,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": self.temperature,
            "humidity": self.humidity,
            "light_intensity": self.light_intensity,
            "devices": self.devices
        }
        print(f"记录日志: {json.dumps(log, ensure_ascii=False, indent=2)}")

class LivingRoom(SmartHomeSystem):
    """客厅"""
    
    def adjust_temperature(self, time_of_day: str) -> None:
        if time_of_day == "早晨":
            self.temperature = 24.0
        elif time_of_day == "晚上":
            self.temperature = 22.0
        print(f"客厅温度调节至 {self.temperature}°C")
    
    def adjust_lighting(self, time_of_day: str) -> None:
        if time_of_day == "早晨":
            self.light_intensity = 80
        elif time_of_day == "晚上":
            self.light_intensity = 30
        print(f"客厅灯光亮度调节至 {self.light_intensity}%")
    
    def control_curtains(self, time_of_day: str) -> None:
        if time_of_day == "早晨":
            print("打开客厅窗帘")
        elif time_of_day == "晚上":
            print("关闭客厅窗帘")
    
    def handle_special_requirements(self) -> None:
        pass

class BedRoom(SmartHomeSystem):
    """卧室"""
    
    def __init__(self, room_name: str):
        super().__init__(room_name)
        self.sleep_mode: bool = False
    
    def adjust_temperature(self, time_of_day: str) -> None:
        if time_of_day == "早晨":
            self.temperature = 23.0
        elif time_of_day == "晚上":
            self.temperature = 20.0
        print(f"卧室温度调节至 {self.temperature}°C")
    
    def adjust_lighting(self, time_of_day: str) -> None:
        if time_of_day == "早晨":
            self.light_intensity = 60
        elif time_of_day == "晚上":
            self.light_intensity = 10
        print(f"卧室灯光亮度调节至 {self.light_intensity}%")
    
    def control_curtains(self, time_of_day: str) -> None:
        if time_of_day == "早晨":
            print("缓慢打开卧室窗帘")
        elif time_of_day == "晚上":
            print("关闭卧室窗帘")
    
    def has_special_requirements(self) -> bool:
        return True
    
    def handle_special_requirements(self) -> None:
        if datetime.now().time() > time(22, 0) or datetime.now().time() < time(6, 0):
            self.sleep_mode = True
            print("启动睡眠模式：")
            print("- 打开空气净化器")
            print("- 播放轻音乐")
            print("- 开启加湿器")

def main():
    # 创建房间
    living_room = LivingRoom("客厅")
    bed_room = BedRoom("主卧")
    
    # 执行早晨场景
    living_room.execute_scene("早晨")
    bed_room.execute_scene("早晨")
    
    # 执行晚上场景
    living_room.execute_scene("晚上")
    bed_room.execute_scene("晚上")

if __name__ == "__main__":
    main()
