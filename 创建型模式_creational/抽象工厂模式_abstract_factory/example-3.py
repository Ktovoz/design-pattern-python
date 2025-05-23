from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import json

# 引擎类型枚举
class EngineType(Enum):
    GASOLINE = "汽油"
    ELECTRIC = "电动"
    HYBRID = "混合动力"

# 车型等级枚举
class CarGrade(Enum):
    ECONOMY = "经济型"
    LUXURY = "豪华型"
    ELECTRIC = "电动型"

# 环保等级枚举
class EmissionLevel(Enum):
    LOW = "低排放"
    MEDIUM = "中等排放"
    HIGH = "高排放"
    ZERO = "零排放"

@dataclass
class CarSpecification:
    """汽车规格数据类"""
    name: str
    value: str
    unit: str = ""
    description: str = ""

@dataclass
class PerformanceMetrics:
    """性能指标数据类"""
    acceleration: float  # 0-100km/h 加速时间（秒）
    max_speed: int       # 最高时速（km/h）
    fuel_consumption: float  # 油耗（L/100km）或电耗（kWh/100km）
    emission_level: EmissionLevel

# 抽象产品：引擎
class Engine(ABC):
    """引擎抽象基类"""
    
    def __init__(self, power: int, torque: int):
        self.power = power  # 功率（马力）
        self.torque = torque  # 扭矩（牛·米）
        self.is_running = False
        self.temperature = 20  # 引擎温度（°C）
        self.runtime_hours = 0.0
    
    @abstractmethod
    def start(self) -> str:
        """启动引擎"""
        pass
    
    @abstractmethod
    def stop(self) -> str:
        """停止引擎"""
        pass
    
    @abstractmethod
    def get_type(self) -> EngineType:
        """获取引擎类型"""
        pass
    
    @abstractmethod
    def get_specifications(self) -> List[CarSpecification]:
        """获取引擎规格"""
        pass
    
    @abstractmethod
    def get_performance_metrics(self) -> PerformanceMetrics:
        """获取性能指标"""
        pass
    
    def run(self, hours: float) -> str:
        """运行引擎指定时间"""
        if not self.is_running:
            return "引擎未启动，无法运行"
        
        self.runtime_hours += hours
        self.temperature = min(95, self.temperature + hours * 10)
        return f"引擎已运行 {hours:.1f} 小时，总运行时间：{self.runtime_hours:.1f} 小时，当前温度：{self.temperature:.1f}°C"

# 抽象产品：车身
class Body(ABC):
    """车身抽象基类"""
    
    def __init__(self, weight: int, drag_coefficient: float):
        self.weight = weight  # 重量（kg）
        self.drag_coefficient = drag_coefficient  # 风阻系数
        self.structural_integrity = 100  # 结构完整性（%）
    
    @abstractmethod
    def get_material(self) -> str:
        """获取车身材料"""
        pass
    
    @abstractmethod
    def get_color(self) -> str:
        """获取车身颜色"""
        pass
    
    @abstractmethod
    def get_specifications(self) -> List[CarSpecification]:
        """获取车身规格"""
        pass
    
    @abstractmethod
    def get_safety_rating(self) -> int:
        """获取安全评级（1-5星）"""
        pass

# 抽象产品：轮胎
class Tire(ABC):
    """轮胎抽象基类"""
    
    def __init__(self, grip_coefficient: float, wear_resistance: int):
        self.grip_coefficient = grip_coefficient  # 抓地力系数
        self.wear_resistance = wear_resistance  # 耐磨指数
        self.wear_level = 0  # 磨损程度（%）
        self.pressure = 2.5  # 胎压（bar）
    
    @abstractmethod
    def get_size(self) -> str:
        """获取轮胎尺寸"""
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """获取轮胎类型"""
        pass
    
    @abstractmethod
    def get_specifications(self) -> List[CarSpecification]:
        """获取轮胎规格"""
        pass
    
    def check_condition(self) -> str:
        """检查轮胎状况"""
        if self.wear_level < 20:
            condition = "优秀"
        elif self.wear_level < 50:
            condition = "良好"
        elif self.wear_level < 80:
            condition = "一般"
        else:
            condition = "需更换"
        
        return f"轮胎状况：{condition}（磨损：{self.wear_level}%，胎压：{self.pressure}bar）"

# 具体产品：汽油引擎
class GasolineEngine(Engine):
    """汽油引擎"""
    
    def __init__(self):
        super().__init__(180, 250)
        self.displacement = 2.0  # 排量（L）
        self.fuel_level = 100  # 燃油量（%）
    
    def start(self) -> str:
        if not self.is_running:
            self.is_running = True
            self.temperature = 25
            self.fuel_level -= 1
            return f"汽油引擎启动成功！排量：{self.displacement}L，功率：{self.power}马力，剩余燃油：{self.fuel_level}%"
        return "汽油引擎已经在运行中"
    
    def stop(self) -> str:
        if self.is_running:
            self.is_running = False
            self.temperature = max(20, self.temperature - 15)
            return f"汽油引擎已停止，温度下降至：{self.temperature}°C"
        return "汽油引擎已经停止"
    
    def get_type(self) -> EngineType:
        return EngineType.GASOLINE
    
    def get_specifications(self) -> List[CarSpecification]:
        return [
            CarSpecification("引擎类型", "自然吸气汽油引擎", "", "传统内燃机技术"),
            CarSpecification("排量", str(self.displacement), "L", "引擎工作容积"),
            CarSpecification("最大功率", str(self.power), "马力", "在6000转时的最大输出功率"),
            CarSpecification("最大扭矩", str(self.torque), "牛·米", "在4000转时的最大扭矩"),
            CarSpecification("燃料类型", "95号汽油", "", "推荐使用无铅汽油"),
            CarSpecification("缸数", "4", "缸", "四缸发动机配置")
        ]
    
    def get_performance_metrics(self) -> PerformanceMetrics:
        return PerformanceMetrics(
            acceleration=9.5,
            max_speed=180,
            fuel_consumption=7.8,
            emission_level=EmissionLevel.MEDIUM
        )

# 具体产品：电动引擎
class ElectricEngine(Engine):
    """电动引擎"""
    
    def __init__(self):
        super().__init__(300, 400)
        self.battery_capacity = 75.0  # 电池容量（kWh）
        self.battery_level = 100  # 电池电量（%）
        self.efficiency = 95  # 能量转换效率（%）
    
    def start(self) -> str:
        if not self.is_running:
            self.is_running = True
            self.temperature = 22
            return f"电动引擎启动成功！功率：{self.power}马力，电池容量：{self.battery_capacity}kWh，剩余电量：{self.battery_level}%"
        return "电动引擎已经在运行中"
    
    def stop(self) -> str:
        if self.is_running:
            self.is_running = False
            return f"电动引擎已停止，剩余电量：{self.battery_level}%"
        return "电动引擎已经停止"
    
    def get_type(self) -> EngineType:
        return EngineType.ELECTRIC
    
    def get_specifications(self) -> List[CarSpecification]:
        return [
            CarSpecification("引擎类型", "永磁同步电机", "", "高效电动动力系统"),
            CarSpecification("最大功率", str(self.power), "马力", "电机最大输出功率"),
            CarSpecification("最大扭矩", str(self.torque), "牛·米", "电机瞬时最大扭矩"),
            CarSpecification("电池容量", str(self.battery_capacity), "kWh", "锂离子电池组容量"),
            CarSpecification("能效比", str(self.efficiency), "%", "电能转换效率"),
            CarSpecification("充电时间", "45", "分钟", "快充至80%电量所需时间")
        ]
    
    def get_performance_metrics(self) -> PerformanceMetrics:
        return PerformanceMetrics(
            acceleration=6.8,
            max_speed=200,
            fuel_consumption=16.5,  # kWh/100km
            emission_level=EmissionLevel.ZERO
        )

# 具体产品：混合动力引擎
class HybridEngine(Engine):
    """混合动力引擎"""
    
    def __init__(self):
        super().__init__(250, 320)
        self.displacement = 2.5  # 汽油引擎排量（L）
        self.electric_power = 100  # 电机功率（马力）
        self.fuel_level = 100
        self.battery_level = 100
    
    def start(self) -> str:
        if not self.is_running:
            self.is_running = True
            self.temperature = 23
            return f"混合动力引擎启动成功！总功率：{self.power}马力（汽油{self.power-self.electric_power}+电动{self.electric_power}），燃油：{self.fuel_level}%，电量：{self.battery_level}%"
        return "混合动力引擎已经在运行中"
    
    def stop(self) -> str:
        if self.is_running:
            self.is_running = False
            self.temperature = max(20, self.temperature - 10)
            return f"混合动力引擎已停止，燃油：{self.fuel_level}%，电量：{self.battery_level}%"
        return "混合动力引擎已经停止"
    
    def get_type(self) -> EngineType:
        return EngineType.HYBRID
    
    def get_specifications(self) -> List[CarSpecification]:
        return [
            CarSpecification("引擎类型", "油电混合动力系统", "", "汽油引擎+电动机组合"),
            CarSpecification("汽油引擎排量", str(self.displacement), "L", "内燃机排量"),
            CarSpecification("电机功率", str(self.electric_power), "马力", "电动机辅助功率"),
            CarSpecification("系统总功率", str(self.power), "马力", "汽油+电动综合功率"),
            CarSpecification("最大扭矩", str(self.torque), "牛·米", "系统综合扭矩输出"),
            CarSpecification("混动系统", "串并联", "", "智能切换驱动模式")
        ]
    
    def get_performance_metrics(self) -> PerformanceMetrics:
        return PerformanceMetrics(
            acceleration=7.8,
            max_speed=190,
            fuel_consumption=5.2,
            emission_level=EmissionLevel.LOW
        )

# 具体产品：钢制车身
class SteelBody(Body):
    """钢制车身"""
    
    def __init__(self):
        super().__init__(1450, 0.32)
        self.material_grade = "高强度钢"
        self.coating = "防腐涂层"
    
    def get_material(self) -> str:
        return "高强度钢"
    
    def get_color(self) -> str:
        return "银色"
    
    def get_specifications(self) -> List[CarSpecification]:
        return [
            CarSpecification("车身材料", self.material_grade, "", "采用高强度钢材制造"),
            CarSpecification("车身重量", str(self.weight), "kg", "优化重量设计"),
            CarSpecification("风阻系数", str(self.drag_coefficient), "Cd", "空气动力学设计"),
            CarSpecification("防腐处理", self.coating, "", "12层防腐工艺"),
            CarSpecification("车身颜色", self.get_color(), "", "金属漆面处理"),
            CarSpecification("质保期", "6", "年", "车身结构质保")
        ]
    
    def get_safety_rating(self) -> int:
        return 4  # 4星安全评级

# 具体产品：碳纤维车身
class CarbonFiberBody(Body):
    """碳纤维车身"""
    
    def __init__(self):
        super().__init__(980, 0.25)
        self.material_grade = "T800级碳纤维"
        self.coating = "UV防护涂层"
    
    def get_material(self) -> str:
        return "碳纤维"
    
    def get_color(self) -> str:
        return "黑色"
    
    def get_specifications(self) -> List[CarSpecification]:
        return [
            CarSpecification("车身材料", self.material_grade, "", "航空级碳纤维材料"),
            CarSpecification("车身重量", str(self.weight), "kg", "轻量化设计，减重32%"),
            CarSpecification("风阻系数", str(self.drag_coefficient), "Cd", "优化空气动力学"),
            CarSpecification("强度重量比", "5倍于钢材", "", "超高强度重量比"),
            CarSpecification("车身颜色", self.get_color(), "", "碳纤维原色纹理"),
            CarSpecification("制造工艺", "预浸料成型", "", "高温高压成型工艺")
        ]
    
    def get_safety_rating(self) -> int:
        return 5  # 5星安全评级

# 具体产品：普通轮胎
class StandardTire(Tire):
    """标准轮胎"""
    
    def __init__(self):
        super().__init__(0.7, 300)
        self.brand = "米其林"
        self.model = "Energy Saver"
    
    def get_size(self) -> str:
        return "205/55R16"
    
    def get_type(self) -> str:
        return "节能轮胎"
    
    def get_specifications(self) -> List[CarSpecification]:
        return [
            CarSpecification("轮胎品牌", self.brand, "", "知名轮胎制造商"),
            CarSpecification("轮胎型号", self.model, "", "节能环保型轮胎"),
            CarSpecification("轮胎尺寸", self.get_size(), "", "16英寸轮毂配套"),
            CarSpecification("抓地力系数", str(self.grip_coefficient), "", "湿地抓地力表现"),
            CarSpecification("耐磨指数", str(self.wear_resistance), "", "轮胎耐用性指标"),
            CarSpecification("节能等级", "A", "", "欧盟轮胎标签节能等级")
        ]

# 具体产品：高性能轮胎
class PerformanceTire(Tire):
    """高性能轮胎"""
    
    def __init__(self):
        super().__init__(0.95, 250)
        self.brand = "倍耐力"
        self.model = "P Zero"
    
    def get_size(self) -> str:
        return "245/40R19"
    
    def get_type(self) -> str:
        return "高性能运动轮胎"
    
    def get_specifications(self) -> List[CarSpecification]:
        return [
            CarSpecification("轮胎品牌", self.brand, "", "顶级运动轮胎品牌"),
            CarSpecification("轮胎型号", self.model, "", "F1级别运动轮胎"),
            CarSpecification("轮胎尺寸", self.get_size(), "", "19英寸大尺寸轮毂"),
            CarSpecification("抓地力系数", str(self.grip_coefficient), "", "卓越的抓地力性能"),
            CarSpecification("耐磨指数", str(self.wear_resistance), "", "运动取向设计"),
            CarSpecification("速度等级", "Y", "", "300km/h高速级别")
        ]

# 抽象工厂
class CarFactory(ABC):
    """汽车工厂抽象基类"""
    
    @abstractmethod
    def create_engine(self) -> Engine:
        """创建引擎"""
        pass
    
    @abstractmethod
    def create_body(self) -> Body:
        """创建车身"""
        pass
    
    @abstractmethod
    def create_tires(self) -> List[Tire]:
        """创建轮胎"""
        pass
    
    @abstractmethod
    def get_car_grade(self) -> CarGrade:
        """获取汽车等级"""
        pass
    
    @abstractmethod
    def get_base_price(self) -> int:
        """获取基础价格（万元）"""
        pass

# 具体工厂：经济型汽车工厂
class EconomyCarFactory(CarFactory):
    """经济型汽车工厂"""
    
    def create_engine(self) -> Engine:
        return GasolineEngine()
    
    def create_body(self) -> Body:
        return SteelBody()
    
    def create_tires(self) -> List[Tire]:
        return [StandardTire() for _ in range(4)]
    
    def get_car_grade(self) -> CarGrade:
        return CarGrade.ECONOMY
    
    def get_base_price(self) -> int:
        return 12  # 12万元

# 具体工厂：豪华型汽车工厂
class LuxuryCarFactory(CarFactory):
    """豪华型汽车工厂"""
    
    def create_engine(self) -> Engine:
        return HybridEngine()
    
    def create_body(self) -> Body:
        return CarbonFiberBody()
    
    def create_tires(self) -> List[Tire]:
        return [PerformanceTire() for _ in range(4)]
    
    def get_car_grade(self) -> CarGrade:
        return CarGrade.LUXURY
    
    def get_base_price(self) -> int:
        return 45  # 45万元

# 具体工厂：电动型汽车工厂
class ElectricCarFactory(CarFactory):
    """电动型汽车工厂"""
    
    def create_engine(self) -> Engine:
        return ElectricEngine()
    
    def create_body(self) -> Body:
        return CarbonFiberBody()
    
    def create_tires(self) -> List[Tire]:
        return [PerformanceTire() for _ in range(4)]
    
    def get_car_grade(self) -> CarGrade:
        return CarGrade.ELECTRIC
    
    def get_base_price(self) -> int:
        return 35  # 35万元

# 汽车类
class Car:
    """汽车组合类"""
    
    def __init__(self, engine: Engine, body: Body, tires: List[Tire], car_grade: CarGrade, base_price: int):
        if len(tires) != 4:
            raise ValueError("汽车必须有4个轮胎")
        
        self.engine = engine
        self.body = body
        self.tires = tires
        self.car_grade = car_grade
        self.base_price = base_price
        self.mileage = 0.0  # 里程（km）
        self.maintenance_due = False
    
    def start_engine(self) -> str:
        """启动引擎"""
        return self.engine.start()
    
    def stop_engine(self) -> str:
        """停止引擎"""
        return self.engine.stop()
    
    def drive(self, distance: float) -> List[str]:
        """驾驶指定距离"""
        if not self.engine.is_running:
            return ["请先启动引擎"]
        
        results = []
        self.mileage += distance
        
        # 增加轮胎磨损
        wear_increase = distance / 10000  # 每10000km磨损1%
        for tire in self.tires:
            tire.wear_level = min(100, tire.wear_level + wear_increase)
        
        # 检查是否需要保养
        if self.mileage % 5000 < distance:
            self.maintenance_due = True
        
        results.append(f"驾驶了 {distance:.1f} 公里，总里程：{self.mileage:.1f} 公里")
        
        if self.maintenance_due:
            results.append("⚠️ 提醒：车辆行驶里程已到保养周期，请及时保养")
        
        return results
    
    def get_full_specifications(self) -> Dict[str, List[CarSpecification]]:
        """获取完整规格"""
        specs = {
            "引擎": self.engine.get_specifications(),
            "车身": self.body.get_specifications(),
            "轮胎": self.tires[0].get_specifications()
        }
        
        # 添加车辆基本信息
        specs["基本信息"] = [
            CarSpecification("车型等级", self.car_grade.value, "", "车辆定位级别"),
            CarSpecification("指导价格", str(self.base_price), "万元", "厂商建议零售价"),
            CarSpecification("安全评级", f"{self.body.get_safety_rating()}星", "", "碰撞安全评级"),
            CarSpecification("总里程", f"{self.mileage:.1f}", "公里", "车辆累计行驶里程")
        ]
        
        return specs
    
    def get_performance_summary(self) -> Dict[str, any]:
        """获取性能汇总"""
        metrics = self.engine.get_performance_metrics()
        
        # 计算综合评分
        performance_score = 100
        performance_score -= (metrics.acceleration - 6) * 5  # 加速性能
        performance_score += (metrics.max_speed - 150) * 0.1  # 最高速度
        performance_score -= metrics.fuel_consumption * 2  # 燃油经济性
        performance_score = max(0, min(100, performance_score))
        
        return {
            "加速性能": f"{metrics.acceleration}秒 (0-100km/h)",
            "最高时速": f"{metrics.max_speed}km/h",
            "能耗水平": f"{metrics.fuel_consumption}{'L' if metrics.emission_level != EmissionLevel.ZERO else 'kWh'}/100km",
            "排放等级": metrics.emission_level.value,
            "综合评分": f"{performance_score:.1f}/100",
            "安全评级": f"{self.body.get_safety_rating()}星"
        }
    
    def export_config(self) -> str:
        """导出配置为JSON格式"""
        config = {
            "car_grade": self.car_grade.value,
            "engine_type": self.engine.get_type().value,
            "body_material": self.body.get_material(),
            "tire_type": self.tires[0].get_type(),
            "base_price": self.base_price,
            "mileage": self.mileage,
            "performance": self.get_performance_summary()
        }
        return json.dumps(config, ensure_ascii=False, indent=2)

# 客户端代码
def create_and_test_car(factory: CarFactory) -> None:
    """创建并测试汽车"""
    car_grade = factory.get_car_grade()
    print(f"\n{'='*70}")
    print(f"🏭 正在使用 {car_grade.value} 汽车工厂制造车辆")
    print(f"{'='*70}")
    
    try:
        # 创建汽车组件
        engine = factory.create_engine()
        body = factory.create_body()
        tires = factory.create_tires()
        base_price = factory.get_base_price()
        
        # 组装汽车
        car = Car(engine, body, tires, car_grade, base_price)
        
        # 显示详细规格
        print(f"\n📋 {car_grade.value} 详细规格：")
        specs = car.get_full_specifications()
        
        for component_name, component_specs in specs.items():
            print(f"\n  🔧 {component_name}：")
            for spec in component_specs:
                unit_str = f" {spec.unit}" if spec.unit else ""
                desc_str = f" ({spec.description})" if spec.description else ""
                print(f"     • {spec.name}：{spec.value}{unit_str}{desc_str}")
        
        # 显示性能汇总
        print(f"\n🚗 {car_grade.value} 性能汇总：")
        performance = car.get_performance_summary()
        for key, value in performance.items():
            print(f"  📊 {key}：{value}")
        
        # 测试车辆功能
        print(f"\n🔄 {car_grade.value} 功能测试：")
        
        # 启动引擎
        print(f"  🔑 {car.start_engine()}")
        
        # 运行引擎测试
        engine_test = car.engine.run(0.5)
        print(f"  ⚙️ {engine_test}")
        
        # 驾驶测试
        drive_results = car.drive(150.0)
        for result in drive_results:
            print(f"  🛣️ {result}")
        
        # 检查轮胎状况
        tire_condition = car.tires[0].check_condition()
        print(f"  🛞 {tire_condition}")
        
        # 停止引擎
        print(f"  🔒 {car.stop_engine()}")
        
        # 导出配置
        print(f"\n📄 车辆配置信息（JSON格式）：")
        config = car.export_config()
        print(config)
        
    except ValueError as e:
        print(f"❌ 创建车辆时发生错误：{e}")
    except Exception as e:
        print(f"❌ 未知错误：{e}")

# 使用示例
if __name__ == "__main__":
    print("🚗 汽车制造工厂抽象工厂模式演示")
    print("本示例展示了如何使用抽象工厂模式创建不同等级的汽车")
    
    # 创建经济型汽车
    economy_factory = EconomyCarFactory()
    create_and_test_car(economy_factory)
    
    # 创建豪华型汽车
    luxury_factory = LuxuryCarFactory()
    create_and_test_car(luxury_factory)
    
    # 创建电动型汽车
    electric_factory = ElectricCarFactory()
    create_and_test_car(electric_factory)
    
    print(f"\n{'='*70}")
    print("✨ 演示完成！三种等级的汽车都已成功制造并测试。")
    print("💡 注意：同一工厂创建的组件保持了设计理念和性能等级的一致性。")
    print("🔧 提示：车辆具有里程记录、保养提醒等实用功能。")
    print("📊 特色：提供详细的性能指标和规格信息。")
    print(f"{'='*70}") 