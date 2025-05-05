from abc import ABC, abstractmethod
from typing import Dict, List
from enum import Enum

# 引擎类型枚举
class EngineType(Enum):
    GASOLINE = "汽油"
    ELECTRIC = "电动"
    HYBRID = "混合动力"

# 抽象产品：引擎
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def get_type(self) -> EngineType:
        pass

# 抽象产品：车身
class Body(ABC):
    @abstractmethod
    def get_material(self) -> str:
        pass
    
    @abstractmethod
    def get_color(self) -> str:
        pass

# 抽象产品：轮胎
class Tire(ABC):
    @abstractmethod
    def get_size(self) -> str:
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        pass

# 具体产品：汽油引擎
class GasolineEngine(Engine):
    def start(self):
        print("汽油引擎启动")
    
    def get_type(self) -> EngineType:
        return EngineType.GASOLINE

# 具体产品：电动引擎
class ElectricEngine(Engine):
    def start(self):
        print("电动引擎启动")
    
    def get_type(self) -> EngineType:
        return EngineType.ELECTRIC

# 具体产品：混合动力引擎
class HybridEngine(Engine):
    def start(self):
        print("混合动力引擎启动")
    
    def get_type(self) -> EngineType:
        return EngineType.HYBRID

# 具体产品：钢制车身
class SteelBody(Body):
    def get_material(self) -> str:
        return "钢"
    
    def get_color(self) -> str:
        return "银色"

# 具体产品：碳纤维车身
class CarbonFiberBody(Body):
    def get_material(self) -> str:
        return "碳纤维"
    
    def get_color(self) -> str:
        return "黑色"

# 具体产品：普通轮胎
class StandardTire(Tire):
    def get_size(self) -> str:
        return "17英寸"
    
    def get_type(self) -> str:
        return "普通轮胎"

# 具体产品：高性能轮胎
class PerformanceTire(Tire):
    def get_size(self) -> str:
        return "19英寸"
    
    def get_type(self) -> str:
        return "高性能轮胎"

# 抽象工厂
class CarFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass
    
    @abstractmethod
    def create_body(self) -> Body:
        pass
    
    @abstractmethod
    def create_tires(self) -> List[Tire]:
        pass

# 具体工厂：经济型汽车工厂
class EconomyCarFactory(CarFactory):
    def create_engine(self) -> Engine:
        return GasolineEngine()
    
    def create_body(self) -> Body:
        return SteelBody()
    
    def create_tires(self) -> List[Tire]:
        return [StandardTire() for _ in range(4)]

# 具体工厂：豪华型汽车工厂
class LuxuryCarFactory(CarFactory):
    def create_engine(self) -> Engine:
        return HybridEngine()
    
    def create_body(self) -> Body:
        return CarbonFiberBody()
    
    def create_tires(self) -> List[Tire]:
        return [PerformanceTire() for _ in range(4)]

# 具体工厂：电动型汽车工厂
class ElectricCarFactory(CarFactory):
    def create_engine(self) -> Engine:
        return ElectricEngine()
    
    def create_body(self) -> Body:
        return CarbonFiberBody()
    
    def create_tires(self) -> List[Tire]:
        return [PerformanceTire() for _ in range(4)]

# 汽车类
class Car:
    def __init__(self, engine: Engine, body: Body, tires: List[Tire]):
        self.engine = engine
        self.body = body
        self.tires = tires
    
    def start(self):
        print(f"启动{self.engine.get_type().value}引擎")
        self.engine.start()
    
    def get_specifications(self) -> Dict:
        return {
            "引擎类型": self.engine.get_type().value,
            "车身材料": self.body.get_material(),
            "车身颜色": self.body.get_color(),
            "轮胎数量": len(self.tires),
            "轮胎尺寸": self.tires[0].get_size(),
            "轮胎类型": self.tires[0].get_type()
        }

# 客户端代码
def create_car(factory: CarFactory) -> Car:
    engine = factory.create_engine()
    body = factory.create_body()
    tires = factory.create_tires()
    return Car(engine, body, tires)

# 使用示例
if __name__ == "__main__":
    # 创建经济型汽车
    economy_factory = EconomyCarFactory()
    print("创建经济型汽车：")
    economy_car = create_car(economy_factory)
    economy_car.start()
    print("汽车规格：", economy_car.get_specifications())
    
    # 创建豪华型汽车
    luxury_factory = LuxuryCarFactory()
    print("\n创建豪华型汽车：")
    luxury_car = create_car(luxury_factory)
    luxury_car.start()
    print("汽车规格：", luxury_car.get_specifications())
    
    # 创建电动型汽车
    electric_factory = ElectricCarFactory()
    print("\n创建电动型汽车：")
    electric_car = create_car(electric_factory)
    electric_car.start()
    print("汽车规格：", electric_car.get_specifications()) 