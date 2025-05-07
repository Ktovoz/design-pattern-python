from abc import ABC, abstractmethod

# 抽象表达式
class HomeApplianceExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 终结符表达式 - 设备
class DeviceExpression(HomeApplianceExpression):
    def __init__(self, device):
        self.device = device
    
    def interpret(self, context):
        return self.device in context

# 终结符表达式 - 动作
class ActionExpression(HomeApplianceExpression):
    def __init__(self, action):
        self.action = action
    
    def interpret(self, context):
        return self.action in context

# 环境类
class HomeContext:
    def __init__(self, input_str):
        self.input = input_str.lower()

# 客户端代码
def main():
    # 简单的家电控制命令解释
    commands = [
        "打开电视",
        "关闭空调",
        "开灯",
        "关电视"
    ]
    
    # 创建表达式
    tv = DeviceExpression("电视")
    ac = DeviceExpression("空调")
    light = DeviceExpression("灯")
    turn_on = ActionExpression("打开")
    turn_off = ActionExpression("关")
    
    # 解释命令
    for command in commands:
        context = HomeContext(command)
        if tv.interpret(context.input):
            if turn_on.interpret(context.input):
                print("执行操作：打开电视")
            elif turn_off.interpret(context.input):
                print("执行操作：关闭电视")
        elif ac.interpret(context.input):
            if turn_on.interpret(context.input):
                print("执行操作：打开空调")
            elif turn_off.interpret(context.input):
                print("执行操作：关闭空调")
        elif light.interpret(context.input):
            if turn_on.interpret(context.input):
                print("执行操作：打开灯")
            elif turn_off.interpret(context.input):
                print("执行操作：关闭灯")

if __name__ == "__main__":
    main()
