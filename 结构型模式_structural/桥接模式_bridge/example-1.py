from abc import ABC, abstractmethod

# 实现部分接口
class TV(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

# 具体实现
class SonyTV(TV):
    def turn_on(self):
        print("索尼电视开机")
    
    def turn_off(self):
        print("索尼电视关机")

class SamsungTV(TV):
    def turn_on(self):
        print("三星电视开机")
    
    def turn_off(self):
        print("三星电视关机")

# 抽象部分
class RemoteControl:
    def __init__(self, tv: TV):
        self.tv = tv
    
    def turn_on(self):
        self.tv.turn_on()
    
    def turn_off(self):
        self.tv.turn_off()

# 使用示例
if __name__ == "__main__":
    # 创建索尼电视和遥控器
    sony_tv = SonyTV()
    sony_remote = RemoteControl(sony_tv)
    
    # 创建三星电视和遥控器
    samsung_tv = SamsungTV()
    samsung_remote = RemoteControl(samsung_tv)
    
    # 使用遥控器控制电视
    print("使用索尼遥控器：")
    sony_remote.turn_on()
    sony_remote.turn_off()
    
    print("\n使用三星遥控器：")
    samsung_remote.turn_on()
    samsung_remote.turn_off()
