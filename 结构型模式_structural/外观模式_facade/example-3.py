class WaterHeater:
    def __init__(self):
        self.temperature = 20
        self.is_heating = False
    
    def heat(self, target_temp):
        self.is_heating = True
        print(f"开始加热水温至 {target_temp}°C")
        self.temperature = target_temp
        self.is_heating = False
    
    def get_temperature(self):
        return self.temperature

class Grinder:
    def __init__(self):
        self.coffee_beans = 0
    
    def add_beans(self, amount):
        self.coffee_beans += amount
        print(f"添加了 {amount}g 咖啡豆")
    
    def grind(self, fineness):
        if self.coffee_beans <= 0:
            raise Exception("没有足够的咖啡豆")
        print(f"研磨咖啡豆，细度: {fineness}")
        self.coffee_beans -= 20
        return True

class MilkFrother:
    def __init__(self):
        self.milk_amount = 0
    
    def add_milk(self, amount):
        self.milk_amount += amount
        print(f"添加了 {amount}ml 牛奶")
    
    def froth(self):
        if self.milk_amount <= 0:
            raise Exception("没有足够的牛奶")
        print("打发牛奶")
        self.milk_amount -= 50
        return True

class CoffeeMaker:
    def __init__(self):
        self.water_level = 0
    
    def add_water(self, amount):
        self.water_level += amount
        print(f"添加了 {amount}ml 水")
    
    def brew(self, temperature):
        if self.water_level <= 0:
            raise Exception("没有足够的水")
        print(f"使用 {temperature}°C 的水冲泡咖啡")
        self.water_level -= 100
        return True

class CoffeeMachineFacade:
    def __init__(self):
        self.water_heater = WaterHeater()
        self.grinder = Grinder()
        self.milk_frother = MilkFrother()
        self.coffee_maker = CoffeeMaker()
    
    def prepare_espresso(self):
        print("\n准备制作浓缩咖啡...")
        try:
            self.grinder.add_beans(20)
            self.grinder.grind("细")
            self.coffee_maker.add_water(100)
            self.water_heater.heat(92)
            self.coffee_maker.brew(self.water_heater.get_temperature())
            print("浓缩咖啡制作完成！")
        except Exception as e:
            print(f"制作失败: {str(e)}")
    
    def prepare_latte(self):
        print("\n准备制作拿铁咖啡...")
        try:
            self.grinder.add_beans(20)
            self.grinder.grind("中")
            self.coffee_maker.add_water(100)
            self.water_heater.heat(90)
            self.milk_frother.add_milk(200)
            self.milk_frother.froth()
            self.coffee_maker.brew(self.water_heater.get_temperature())
            print("拿铁咖啡制作完成！")
        except Exception as e:
            print(f"制作失败: {str(e)}")
    
    def prepare_cappuccino(self):
        print("\n准备制作卡布奇诺...")
        try:
            self.grinder.add_beans(20)
            self.grinder.grind("中")
            self.coffee_maker.add_water(100)
            self.water_heater.heat(88)
            self.milk_frother.add_milk(150)
            self.milk_frother.froth()
            self.coffee_maker.brew(self.water_heater.get_temperature())
            print("卡布奇诺制作完成！")
        except Exception as e:
            print(f"制作失败: {str(e)}")
    
    def get_status(self):
        print("\n咖啡机状态:")
        print(f"水温: {self.water_heater.get_temperature()}°C")
        print(f"剩余咖啡豆: {self.grinder.coffee_beans}g")
        print(f"剩余牛奶: {self.milk_frother.milk_amount}ml")
        print(f"剩余水量: {self.coffee_maker.water_level}ml")

# 使用示例
if __name__ == "__main__":
    coffee_machine = CoffeeMachineFacade()
    
    # 制作浓缩咖啡
    coffee_machine.prepare_espresso()
    coffee_machine.get_status()
    
    # 制作拿铁
    coffee_machine.prepare_latte()
    coffee_machine.get_status()
    
    # 制作卡布奇诺
    coffee_machine.prepare_cappuccino()
    coffee_machine.get_status()
