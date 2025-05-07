class Light:
    def __init__(self, location):
        self.location = location
        self.brightness = 0
    
    def on(self):
        print(f"{self.location}的灯已开启")
    
    def off(self):
        print(f"{self.location}的灯已关闭")
    
    def dim(self, level):
        self.brightness = level
        print(f"{self.location}的灯亮度设置为: {level}")

class Thermostat:
    def __init__(self):
        self.temperature = 25
    
    def set_temperature(self, temp):
        self.temperature = temp
        print(f"温度设置为: {temp}°C")
    
    def get_temperature(self):
        return self.temperature

class SecuritySystem:
    def __init__(self):
        self.armed = False
    
    def arm(self):
        self.armed = True
        print("安全系统已启动")
    
    def disarm(self):
        self.armed = False
        print("安全系统已关闭")
    
    def check_status(self):
        return "已启动" if self.armed else "已关闭"

class SmartHomeFacade:
    def __init__(self):
        self.living_room_light = Light("客厅")
        self.bedroom_light = Light("卧室")
        self.thermostat = Thermostat()
        self.security = SecuritySystem()
    
    def good_morning(self):
        print("早安模式启动...")
        self.living_room_light.on()
        self.living_room_light.dim(70)
        self.thermostat.set_temperature(22)
        self.security.disarm()
    
    def good_night(self):
        print("晚安模式启动...")
        self.living_room_light.off()
        self.bedroom_light.dim(30)
        self.thermostat.set_temperature(20)
        self.security.arm()
    
    def leave_home(self):
        print("离家模式启动...")
        self.living_room_light.off()
        self.bedroom_light.off()
        self.thermostat.set_temperature(18)
        self.security.arm()
    
    def get_status(self):
        print("\n当前家居状态:")
        print(f"客厅灯: {'开启' if self.living_room_light.brightness > 0 else '关闭'}")
        print(f"卧室灯: {'开启' if self.bedroom_light.brightness > 0 else '关闭'}")
        print(f"温度: {self.thermostat.get_temperature()}°C")
        print(f"安全系统: {self.security.check_status()}")

# 使用示例
if __name__ == "__main__":
    home = SmartHomeFacade()
    
    print("=== 早晨场景 ===")
    home.good_morning()
    home.get_status()
    
    print("\n=== 离家场景 ===")
    home.leave_home()
    home.get_status()
    
    print("\n=== 夜晚场景 ===")
    home.good_night()
    home.get_status()
