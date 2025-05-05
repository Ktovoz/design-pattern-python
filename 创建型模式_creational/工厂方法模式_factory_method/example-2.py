from abc import ABC, abstractmethod

# 抽象产品类 - 电子产品
class ElectronicProduct(ABC):
    @abstractmethod
    def power_on(self):
        pass

# 具体产品类 - 手机
class Smartphone(ElectronicProduct):
    def power_on(self):
        return "手机开机中..."

# 具体产品类 - 笔记本电脑
class Laptop(ElectronicProduct):
    def power_on(self):
        return "笔记本电脑启动中..."

# 具体产品类 - 平板电脑
class Tablet(ElectronicProduct):
    def power_on(self):
        return "平板电脑启动中..."

# 抽象创建者类
class ElectronicCreator(ABC):
    @abstractmethod
    def create_product(self) -> ElectronicProduct:
        pass
    
    def start_device(self):
        product = self.create_product()
        return product.power_on()

# 具体创建者类 - 手机创建者
class SmartphoneCreator(ElectronicCreator):
    def create_product(self) -> ElectronicProduct:
        return Smartphone()

# 具体创建者类 - 笔记本电脑创建者
class LaptopCreator(ElectronicCreator):
    def create_product(self) -> ElectronicProduct:
        return Laptop()

# 具体创建者类 - 平板电脑创建者
class TabletCreator(ElectronicCreator):
    def create_product(self) -> ElectronicProduct:
        return Tablet()

def main():
    # 创建不同类型的电子产品创建者
    phone_creator = SmartphoneCreator()
    laptop_creator = LaptopCreator()
    tablet_creator = TabletCreator()

    # 使用创建者来创建和启动电子产品
    print(phone_creator.start_device())
    print(laptop_creator.start_device())
    print(tablet_creator.start_device())

if __name__ == "__main__":
    main() 