from abc import ABC, abstractmethod

# 目标接口 - 欧式插座
class EuropeanSocket(ABC):
    @abstractmethod
    def european_plug(self):
        pass

# 适配者 - 美式插头
class AmericanPlug:
    def american_plug(self):
        return "美式插头插入"

# 适配器 - 电源转换器
class PowerAdapter(EuropeanSocket):
    def __init__(self, american_plug: AmericanPlug):
        self.american_plug = american_plug

    def european_plug(self):
        return f"通过转换器: {self.american_plug.american_plug()} -> 适配到欧式插座"

def main():
    # 创建美式插头
    american_plug = AmericanPlug()
    
    # 创建适配器
    adapter = PowerAdapter(american_plug)
    
    # 使用适配器
    print(adapter.european_plug())

if __name__ == "__main__":
    main()
