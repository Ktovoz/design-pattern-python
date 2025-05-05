from abc import ABC, abstractmethod

# 抽象产品类 - 交通工具
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

# 具体产品类 - 汽车
class Car(Vehicle):
    def drive(self):
        return "驾驶汽车"

# 具体产品类 - 自行车
class Bicycle(Vehicle):
    def drive(self):
        return "骑自行车"

# 具体产品类 - 摩托车
class Motorcycle(Vehicle):
    def drive(self):
        return "骑摩托车"

# 抽象创建者类
class VehicleCreator(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass
    
    def use_vehicle(self):
        vehicle = self.create_vehicle()
        return vehicle.drive()

# 具体创建者类 - 汽车创建者
class CarCreator(VehicleCreator):
    def create_vehicle(self) -> Vehicle:
        return Car()

# 具体创建者类 - 自行车创建者
class BicycleCreator(VehicleCreator):
    def create_vehicle(self) -> Vehicle:
        return Bicycle()

# 具体创建者类 - 摩托车创建者
class MotorcycleCreator(VehicleCreator):
    def create_vehicle(self) -> Vehicle:
        return Motorcycle()

def main():
    # 创建不同类型的交通工具创建者
    car_creator = CarCreator()
    bicycle_creator = BicycleCreator()
    motorcycle_creator = MotorcycleCreator()

    # 使用创建者来创建和使用交通工具
    print(car_creator.use_vehicle())
    print(bicycle_creator.use_vehicle())
    print(motorcycle_creator.use_vehicle())

if __name__ == "__main__":
    main()
