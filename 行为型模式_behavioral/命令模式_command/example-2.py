#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 智能设备（接收者）
class SmartLight:
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.brightness = 0
        
    def turn_on(self):
        self.is_on = True
        print(f"{self.location}的灯打开了")
        
    def turn_off(self):
        self.is_on = False
        print(f"{self.location}的灯关闭了")
        
    def set_brightness(self, level):
        self.brightness = level
        print(f"{self.location}的灯亮度设置为{level}%")

class SmartAC:
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.temperature = 24
        
    def turn_on(self):
        self.is_on = True
        print(f"{self.location}的空调打开了")
        
    def turn_off(self):
        self.is_on = False
        print(f"{self.location}的空调关闭了")
        
    def set_temperature(self, temp):
        self.temperature = temp
        print(f"{self.location}的空调温度设置为{temp}°C")

# 命令接口
class Command:
    def execute(self):
        pass
        
    def undo(self):
        pass

# 具体命令
class LightCommand(Command):
    def __init__(self, light):
        self.light = light
        self.prev_state = None
        
    def execute(self):
        self.prev_state = self.light.is_on
        self.light.turn_on() if not self.light.is_on else self.light.turn_off()
        
    def undo(self):
        if self.prev_state is not None:
            self.light.turn_on() if self.prev_state else self.light.turn_off()

class ACTempCommand(Command):
    def __init__(self, ac, temperature):
        self.ac = ac
        self.temperature = temperature
        self.prev_temp = None
        
    def execute(self):
        self.prev_temp = self.ac.temperature
        self.ac.set_temperature(self.temperature)
        
    def undo(self):
        if self.prev_temp is not None:
            self.ac.set_temperature(self.prev_temp)

# 调用者
class SmartHomeController:
    def __init__(self):
        self.command_history = []
        
    def execute_command(self, command):
        command.execute()
        self.command_history.append(command)
        
    def undo_last(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()
            print("撤销上一个操作")

# 客户端代码
def main():
    # 创建智能设备
    bedroom_light = SmartLight("卧室")
    living_room_ac = SmartAC("客厅")
    
    # 创建控制器
    controller = SmartHomeController()
    
    # 执行一系列命令
    light_cmd = LightCommand(bedroom_light)
    ac_temp_cmd = ACTempCommand(living_room_ac, 22)
    
    controller.execute_command(light_cmd)  # 开灯
    controller.execute_command(ac_temp_cmd)  # 设置温度
    
    # 撤销操作
    controller.undo_last()  # 撤销温度设置
    controller.undo_last()  # 撤销开灯

if __name__ == "__main__":
    main()
