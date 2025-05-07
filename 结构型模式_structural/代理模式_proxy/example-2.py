from abc import ABC, abstractmethod
import time
from datetime import datetime

# 抽象主题
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

# 真实主题
class AirConditioner(SmartDevice):
    def __init__(self):
        self._is_on = False
        self._temperature = 26
    
    def turn_on(self):
        self._is_on = True
        return f"空调已开启，当前温度：{self._temperature}°C"
    
    def turn_off(self):
        self._is_on = False
        return "空调已关闭"
    
    def set_temperature(self, temp):
        self._temperature = temp
        return f"温度已设置为 {temp}°C"

# 代理
class SmartHomeProxy(SmartDevice):
    def __init__(self):
        self._ac = AirConditioner()
        self._last_used = None
        self._usage_count = 0
    
    def turn_on(self):
        current_time = datetime.now()
        
        # 检查使用频率
        if self._last_used and (current_time - self._last_used).seconds < 300:
            return "请等待5分钟后再使用"
        
        # 检查使用次数
        if self._usage_count >= 10:
            return "今日使用次数已达上限"
        
        self._last_used = current_time
        self._usage_count += 1
        return self._ac.turn_on()
    
    def turn_off(self):
        return self._ac.turn_off()
    
    def set_temperature(self, temp):
        if not self._ac._is_on:
            return "请先开启空调"
        return self._ac.set_temperature(temp)

# 使用示例
if __name__ == "__main__":
    smart_home = SmartHomeProxy()
    
    # 正常使用
    print(smart_home.turn_on())
    print(smart_home.set_temperature(24))
    print(smart_home.turn_off())
    
    # 快速重复使用
    print(smart_home.turn_on())  # 应该被限制
    
    # 模拟等待
    time.sleep(6)
    print(smart_home.turn_on())  # 应该可以正常使用
