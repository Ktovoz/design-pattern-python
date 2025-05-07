"""
简单的智能家居控制中心示例
展示了最基础的中介者模式实现
"""

class SmartHomeMediator:
    def __init__(self):
        self._light = None
        self._tv = None
        
    def register_light(self, light):
        self._light = light
        
    def register_tv(self, tv):
        self._tv = tv
        
    def turn_on_all(self):
        self._light.turn_on()
        self._tv.turn_on()
        
    def turn_off_all(self):
        self._light.turn_off()
        self._tv.turn_off()

class Light:
    def __init__(self, name):
        self.name = name
        
    def turn_on(self):
        print(f"{self.name}开启")
        
    def turn_off(self):
        print(f"{self.name}关闭")

class TV:
    def __init__(self, name):
        self.name = name
        
    def turn_on(self):
        print(f"{self.name}开启")
        
    def turn_off(self):
        print(f"{self.name}关闭")

# 使用示例
if __name__ == "__main__":
    # 创建中介者
    home_center = SmartHomeMediator()
    
    # 创建设备
    living_room_light = Light("客厅灯")
    living_room_tv = TV("客厅电视")
    
    # 注册设备到中介者
    home_center.register_light(living_room_light)
    home_center.register_tv(living_room_tv)
    
    # 通过中介者控制所有设备
    print("=== 回家场景 ===")
    home_center.turn_on_all()
    
    print("\n=== 睡觉场景 ===")
    home_center.turn_off_all()
