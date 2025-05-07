#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 接收者
class Television:
    def turn_on(self):
        print("电视打开了")
        
    def turn_off(self):
        print("电视关闭了")
        
    def change_channel(self, channel):
        print(f"切换到频道 {channel}")

# 命令接口
class Command:
    def execute(self):
        pass

# 具体命令
class TurnOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv
        
    def execute(self):
        self.tv.turn_on()

class TurnOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv
        
    def execute(self):
        self.tv.turn_off()

class ChangeChannelCommand(Command):
    def __init__(self, tv, channel):
        self.tv = tv
        self.channel = channel
        
    def execute(self):
        self.tv.change_channel(self.channel)

# 调用者
class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command
        
    def press_button(self):
        self.command.execute()

# 客户端代码
def main():
    # 创建接收者
    tv = Television()
    
    # 创建命令
    turn_on = TurnOnCommand(tv)
    turn_off = TurnOffCommand(tv)
    change_channel = ChangeChannelCommand(tv, 5)
    
    # 创建调用者
    remote = RemoteControl()
    
    # 执行命令
    remote.set_command(turn_on)
    remote.press_button()  # 打开电视
    
    remote.set_command(change_channel)
    remote.press_button()  # 换台
    
    remote.set_command(turn_off)
    remote.press_button()  # 关闭电视

if __name__ == "__main__":
    main()
