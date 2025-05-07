from abc import ABC, abstractmethod

# 抽象状态类
class LampState(ABC):
    @abstractmethod
    def switch(self, lamp):
        pass

    @abstractmethod
    def get_state(self):
        pass

# 具体状态类：关闭状态
class OffState(LampState):
    def switch(self, lamp):
        lamp.set_state(WeakLightState())
    
    def get_state(self):
        return "关闭状态"

# 具体状态类：弱光状态
class WeakLightState(LampState):
    def switch(self, lamp):
        lamp.set_state(StrongLightState())
    
    def get_state(self):
        return "弱光状态"

# 具体状态类：强光状态
class StrongLightState(LampState):
    def switch(self, lamp):
        lamp.set_state(OffState())
    
    def get_state(self):
        return "强光状态"

# 环境类：台灯
class DeskLamp:
    def __init__(self):
        self._state = OffState()
    
    def set_state(self, state):
        self._state = state
    
    def get_state(self):
        return self._state.get_state()
    
    def press_switch(self):
        self._state.switch(self)

# 客户端代码
if __name__ == "__main__":
    lamp = DeskLamp()
    print(f"当前状态：{lamp.get_state()}")  # 关闭状态
    
    lamp.press_switch()
    print(f"当前状态：{lamp.get_state()}")  # 弱光状态
    
    lamp.press_switch()
    print(f"当前状态：{lamp.get_state()}")  # 强光状态
    
    lamp.press_switch()
    print(f"当前状态：{lamp.get_state()}")  # 关闭状态
