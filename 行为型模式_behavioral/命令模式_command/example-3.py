#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from datetime import datetime
import json
import os

# 咖啡机组件（接收者）
class CoffeeMachine:
    def __init__(self):
        self.water_level = 1000  # ml
        self.coffee_beans = 500  # g
        self.milk = 500  # ml
        self.is_on = False
        
    def power_on(self):
        self.is_on = True
        print("咖啡机已启动")
        
    def power_off(self):
        self.is_on = False
        print("咖啡机已关闭")
        
    def grind_beans(self, amount):
        if self.coffee_beans >= amount:
            self.coffee_beans -= amount
            print(f"正在研磨{amount}g咖啡豆")
        else:
            raise Exception("咖啡豆不足")
            
    def heat_water(self, amount):
        if self.water_level >= amount:
            self.water_level -= amount
            print(f"正在加热{amount}ml水")
        else:
            raise Exception("水量不足")
            
    def froth_milk(self, amount):
        if self.milk >= amount:
            self.milk -= amount
            print(f"正在打发{amount}ml牛奶")
        else:
            raise Exception("牛奶不足")
            
    def brew_coffee(self):
        print("正在冲泡咖啡")
        
    def add_water(self, amount):
        self.water_level += amount
        print(f"添加了{amount}ml水")
        
    def add_coffee_beans(self, amount):
        self.coffee_beans += amount
        print(f"添加了{amount}g咖啡豆")
        
    def add_milk(self, amount):
        self.milk += amount
        print(f"添加了{amount}ml牛奶")

# 命令接口
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
        
    @abstractmethod
    def undo(self):
        pass

# 具体命令
class PowerCommand(Command):
    def __init__(self, machine):
        self.machine = machine
        
    def execute(self):
        if not self.machine.is_on:
            self.machine.power_on()
        else:
            self.machine.power_off()
            
    def undo(self):
        self.execute()  # 开关命令的撤销就是再执行一次

class MakeCoffeeCommand(Command):
    def __init__(self, machine, coffee_type="美式咖啡"):
        self.machine = machine
        self.coffee_type = coffee_type
        self.executed = False
        
    def execute(self):
        if not self.machine.is_on:
            print("错误：咖啡机未启动")
            return
            
        try:
            if self.coffee_type == "美式咖啡":
                self.machine.grind_beans(20)
                self.machine.heat_water(200)
                self.machine.brew_coffee()
            elif self.coffee_type == "拿铁":
                self.machine.grind_beans(20)
                self.machine.heat_water(150)
                self.machine.froth_milk(100)
                self.machine.brew_coffee()
            self.executed = True
        except Exception as e:
            print(f"制作咖啡失败：{str(e)}")
            
    def undo(self):
        if self.executed:
            print(f"咖啡已经制作完成，无法撤销")
        
class RefillCommand(Command):
    def __init__(self, machine, refill_type, amount):
        self.machine = machine
        self.refill_type = refill_type
        self.amount = amount
        self.previous_amount = 0
        
    def execute(self):
        if self.refill_type == "water":
            self.previous_amount = self.machine.water_level
            self.machine.add_water(self.amount)
        elif self.refill_type == "coffee_beans":
            self.previous_amount = self.machine.coffee_beans
            self.machine.add_coffee_beans(self.amount)
        elif self.refill_type == "milk":
            self.previous_amount = self.machine.milk
            self.machine.add_milk(self.amount)
            
    def undo(self):
        if self.refill_type == "water":
            self.machine.water_level = self.previous_amount
        elif self.refill_type == "coffee_beans":
            self.machine.coffee_beans = self.previous_amount
        elif self.refill_type == "milk":
            self.machine.milk = self.previous_amount
        print(f"已撤销添加{self.refill_type}")

# 宏命令
class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands
        
    def execute(self):
        for command in self.commands:
            command.execute()
            
    def undo(self):
        for command in reversed(self.commands):
            command.undo()

# 命令历史记录器
class CommandLogger:
    def __init__(self, filename="coffee_machine_log.json"):
        self.filename = filename
        
    def log_command(self, command_name, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        log_entry = {
            "command": command_name,
            "timestamp": timestamp
        }
        
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    logs = json.load(f)
            else:
                logs = []
                
            logs.append(log_entry)
            
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(logs, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"日志记录失败：{str(e)}")

# 咖啡机控制器
class CoffeeMachineController:
    def __init__(self):
        self.command_history = []
        self.logger = CommandLogger()
        
    def execute_command(self, command, command_name):
        try:
            command.execute()
            self.command_history.append(command)
            self.logger.log_command(command_name)
        except Exception as e:
            print(f"命令执行失败：{str(e)}")
            
    def undo_last(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()
            self.logger.log_command("撤销操作")

# 客户端代码
def main():
    # 创建咖啡机和控制器
    coffee_machine = CoffeeMachine()
    controller = CoffeeMachineController()
    
    # 创建基本命令
    power_cmd = PowerCommand(coffee_machine)
    make_latte = MakeCoffeeCommand(coffee_machine, "拿铁")
    refill_water = RefillCommand(coffee_machine, "water", 500)
    refill_beans = RefillCommand(coffee_machine, "coffee_beans", 200)
    
    # 创建宏命令（启动并补充物料）
    startup_macro = MacroCommand([
        power_cmd,
        refill_water,
        refill_beans
    ])
    
    # 执行命令序列
    print("=== 开始咖啡机操作 ===")
    controller.execute_command(startup_macro, "启动并补充物料")
    controller.execute_command(make_latte, "制作拿铁")
    
    # 撤销最后的操作
    print("\n=== 撤销上一个操作 ===")
    controller.undo_last()
    
    # 关闭咖啡机
    print("\n=== 关闭咖啡机 ===")
    controller.execute_command(power_cmd, "关闭电源")

if __name__ == "__main__":
    main()
