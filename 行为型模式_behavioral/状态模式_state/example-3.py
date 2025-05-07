from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional
import time

# 空调模式枚举
class AirConditionerMode(Enum):
    COOL = "制冷模式"
    HEAT = "制热模式"
    DRY = "除湿模式"
    FAN = "送风模式"
    AUTO = "自动模式"

# 风速枚举
class FanSpeed(Enum):
    LOW = "低速"
    MEDIUM = "中速"
    HIGH = "高速"
    AUTO = "自动"

# 抽象状态类
class ACState(ABC):
    @abstractmethod
    def turn_on(self, ac) -> None:
        pass
    
    @abstractmethod
    def turn_off(self, ac) -> None:
        pass
    
    @abstractmethod
    def set_temperature(self, ac, temp: float) -> None:
        pass
    
    @abstractmethod
    def set_mode(self, ac, mode: AirConditionerMode) -> None:
        pass
    
    @abstractmethod
    def set_fan_speed(self, ac, speed: FanSpeed) -> None:
        pass
    
    @abstractmethod
    def get_state_name(self) -> str:
        pass

# 关机状态
class PowerOffState(ACState):
    def turn_on(self, ac) -> None:
        ac.set_state(StandbyState())
        print("空调已开机，进入待机状态")
    
    def turn_off(self, ac) -> None:
        print("空调已经处于关机状态")
    
    def set_temperature(self, ac, temp: float) -> None:
        print("关机状态无法设置温度")
    
    def set_mode(self, ac, mode: AirConditionerMode) -> None:
        print("关机状态无法设置模式")
    
    def set_fan_speed(self, ac, speed: FanSpeed) -> None:
        print("关机状态无法设置风速")
    
    def get_state_name(self) -> str:
        return "关机状态"

# 待机状态
class StandbyState(ACState):
    def turn_on(self, ac) -> None:
        print("空调已经处于开机状态")
    
    def turn_off(self, ac) -> None:
        ac.set_state(PowerOffState())
        print("空调已关机")
    
    def set_temperature(self, ac, temp: float) -> None:
        if not 16 <= temp <= 30:
            print("温度设置范围：16-30℃")
            return
        ac.target_temperature = temp
        ac.set_state(WorkingState())
        print(f"温度已设置为{temp}℃，进入工作状态")
    
    def set_mode(self, ac, mode: AirConditionerMode) -> None:
        ac.mode = mode
        ac.set_state(WorkingState())
        print(f"模式已设置为{mode.value}，进入工作状态")
    
    def set_fan_speed(self, ac, speed: FanSpeed) -> None:
        ac.fan_speed = speed
        print(f"风速已设置为{speed.value}")
    
    def get_state_name(self) -> str:
        return "待机状态"

# 工作状态
class WorkingState(ACState):
    def turn_on(self, ac) -> None:
        print("空调已经处于工作状态")
    
    def turn_off(self, ac) -> None:
        ac.set_state(PowerOffState())
        print("空调已关机")
    
    def set_temperature(self, ac, temp: float) -> None:
        if not 16 <= temp <= 30:
            print("温度设置范围：16-30℃")
            return
        ac.target_temperature = temp
        print(f"温度已调整为{temp}℃")
    
    def set_mode(self, ac, mode: AirConditionerMode) -> None:
        if mode == ac.mode:
            print(f"当前已经是{mode.value}")
            return
        ac.mode = mode
        print(f"模式已切换为{mode.value}")
    
    def set_fan_speed(self, ac, speed: FanSpeed) -> None:
        if speed == ac.fan_speed:
            print(f"当前已经是{speed.value}")
            return
        ac.fan_speed = speed
        print(f"风速已调整为{speed.value}")
    
    def get_state_name(self) -> str:
        return "工作状态"

# 智能空调类
class SmartAirConditioner:
    def __init__(self):
        self._state: ACState = PowerOffState()
        self.current_temperature: float = 26.0
        self.target_temperature: float = 24.0
        self.mode: AirConditionerMode = AirConditionerMode.COOL
        self.fan_speed: FanSpeed = FanSpeed.AUTO
        self.humidity: float = 50.0
    
    def set_state(self, state: ACState) -> None:
        self._state = state
    
    def get_state(self) -> str:
        return self._state.get_state_name()
    
    def turn_on(self) -> None:
        self._state.turn_on(self)
    
    def turn_off(self) -> None:
        self._state.turn_off(self)
    
    def set_temperature(self, temp: float) -> None:
        self._state.set_temperature(self, temp)
    
    def set_mode(self, mode: AirConditionerMode) -> None:
        self._state.set_mode(self, mode)
    
    def set_fan_speed(self, speed: FanSpeed) -> None:
        self._state.set_fan_speed(self, speed)
    
    def get_status(self) -> str:
        return f"""
当前状态：{self.get_state()}
运行模式：{self.mode.value}
目标温度：{self.target_temperature}℃
当前温度：{self.current_temperature}℃
当前风速：{self.fan_speed.value}
当前湿度：{self.humidity}%
"""

# 模拟环境控制器
class EnvironmentController:
    def __init__(self, ac: SmartAirConditioner):
        self.ac = ac
    
    def simulate_temperature_change(self):
        if self.ac.get_state() == "工作状态":
            if self.ac.mode == AirConditionerMode.COOL:
                self.ac.current_temperature -= 0.5
            elif self.ac.mode == AirConditionerMode.HEAT:
                self.ac.current_temperature += 0.5
            elif self.ac.mode == AirConditionerMode.DRY:
                self.ac.humidity -= 2
    
    def run_simulation(self, duration: int = 3):
        for _ in range(duration):
            self.simulate_temperature_change()
            print(self.ac.get_status())
            time.sleep(1)

# 客户端代码
if __name__ == "__main__":
    # 创建空调实例
    ac = SmartAirConditioner()
    env_controller = EnvironmentController(ac)
    
    print("=== 测试基本功能 ===")
    print(ac.get_status())
    
    ac.turn_on()
    ac.set_temperature(23.0)
    ac.set_mode(AirConditionerMode.COOL)
    ac.set_fan_speed(FanSpeed.HIGH)
    
    print("\n=== 模拟运行 ===")
    env_controller.run_simulation()
    
    print("\n=== 测试模式切换 ===")
    ac.set_mode(AirConditionerMode.HEAT)
    ac.set_fan_speed(FanSpeed.LOW)
    env_controller.run_simulation()
    
    print("\n=== 关机测试 ===")
    ac.turn_off()
    print(ac.get_status())
