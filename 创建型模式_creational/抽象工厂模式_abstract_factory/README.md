# 抽象工厂模式 (Abstract Factory Pattern)

## 简介
抽象工厂模式是一种创建型设计模式，它提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。该模式通过抽象工厂接口来创建一组相关的产品，而不需要关心具体的实现类。

## 模式结构
```
+----------------+       +----------------+       +----------------+
| AbstractFactory|       | AbstractProduct|       | ConcreteProduct|
+----------------+       +----------------+       +----------------+
| +createProduct()|      | +operation()   |      | +operation()   |
+----------------+       +----------------+       +----------------+
        ^                        ^                        ^
        |                        |                        |
+----------------+       +----------------+       +----------------+
| ConcreteFactory|       | Client         |       | ProductFamily  |
+----------------+       +----------------+       +----------------+
| +createProduct()|      | +useProducts() |      | +getProducts() |
+----------------+       +----------------+       +----------------+
```

## 适用场景
- 当需要创建的产品族中配置对象是相关的或依赖的
- 当系统需要独立于产品创建、组合和表示时
- 当系统需要使用的产品族是相关的
- 当需要确保产品族的一致性时
- 当需要隐藏产品族的实现细节时

## 优点
- 将一个系列的产品对象的构建与使用解耦
- 更容易添加新的产品系列
- 更容易复用已有的产品系列
- 确保产品族的一致性
- 符合开闭原则，便于扩展

## 缺点
- 系统中类的个数将增加
- 系统配置复杂
- 增加新的产品族容易，但增加新的产品等级结构困难
- 抽象工厂接口需要支持所有可能的产品族

## 相关设计模式
- 工厂方法模式：抽象工厂模式通常使用工厂方法模式来实现
- 建造者模式：两者都用于创建复杂对象，但建造者模式更关注对象的构建过程
- 单例模式：抽象工厂通常使用单例模式来实现具体的工厂类
- 原型模式：可以用于创建产品对象的副本

## 示例说明

### 示例1：家具工厂（简单难度 ⭐）
**文件**：`example-1.py`

**特点**：
- 产品族简单：只包含椅子和桌子两种产品
- 工厂类型少：只有现代风格和古典风格两种工厂
- 产品关系简单：产品之间没有复杂的依赖关系
- 实现直观：适合初学者理解抽象工厂模式的基本概念

**为什么是简单难度**：
- 产品种类少，结构清晰
- 没有复杂的依赖关系
- 不需要处理多个实例的创建
- 接口设计简单，易于理解

**代码结构**：
```python
# 抽象产品
class Chair(ABC)
class Table(ABC)

# 具体产品
class ModernChair(Chair)
class ModernTable(Table)
class ClassicChair(Chair)
class ClassicTable(Table)

# 抽象工厂
class FurnitureFactory(ABC)

# 具体工厂
class ModernFurnitureFactory(FurnitureFactory)
class ClassicFurnitureFactory(FurnitureFactory)
```

### 示例2：电子设备工厂（中等难度 ⭐⭐）
**文件**：`example-2.py`

**特点**：
- 产品族扩展：包含处理器、显示器和电池三种产品
- 工厂类型：高端设备和标准设备两种工厂
- 产品组合：引入了设备类来组合多个产品
- 类型提示：使用了Python的类型提示功能

**为什么是中等难度**：
- 产品种类增加，需要管理更多组件
- 引入了产品组合的概念
- 需要处理多个组件的协同工作
- 使用了更现代的Python特性

**代码结构**：
```python
# 抽象产品
class Processor(ABC)
class Display(ABC)
class Battery(ABC)

# 具体产品
class HighPerformanceProcessor(Processor)
class StandardProcessor(Processor)
class HDDisplay(Display)
class StandardDisplay(Display)
class LargeBattery(Battery)
class StandardBattery(Battery)

# 抽象工厂
class DeviceFactory(ABC)

# 具体工厂
class PremiumDeviceFactory(DeviceFactory)
class StandardDeviceFactory(DeviceFactory)

# 产品组合
class Device
```

### 示例3：汽车制造工厂（复杂难度 ⭐⭐⭐）
**文件**：`example-3.py`

**特点**：
- 产品族复杂：包含引擎、车身和轮胎三种产品
- 工厂类型多样：经济型、豪华型和电动型三种工厂
- 高级特性：
  - 使用枚举类型定义引擎类型
  - 产品之间有复杂的依赖关系
  - 引入了规格说明功能
  - 需要创建多个轮胎实例
- 类型系统：使用了完整的类型注解

**为什么是复杂难度**：
- 产品之间的依赖关系复杂
- 需要处理多个实例的创建（如轮胎）
- 使用了枚举等高级特性
- 包含了完整的规格说明系统
- 产品组合逻辑更复杂
- 类型系统更完善

**代码结构**：
```python
# 枚举类型
class EngineType(Enum)

# 抽象产品
class Engine(ABC)
class Body(ABC)
class Tire(ABC)

# 具体产品
class GasolineEngine(Engine)
class ElectricEngine(Engine)
class HybridEngine(Engine)
class SteelBody(Body)
class CarbonFiberBody(Body)
class StandardTire(Tire)
class PerformanceTire(Tire)

# 抽象工厂
class CarFactory(ABC)

# 具体工厂
class EconomyCarFactory(CarFactory)
class LuxuryCarFactory(CarFactory)
class ElectricCarFactory(CarFactory)

# 产品组合
class Car
```

## 学习建议
1. 建议从简单示例开始，理解抽象工厂模式的基本概念
2. 然后学习中等示例，了解如何处理多个组件的组合
3. 最后研究复杂示例，掌握抽象工厂模式的高级应用
4. 尝试自己实现一个抽象工厂模式的例子
5. 思考如何扩展现有示例，添加新的产品族或产品等级

## 运行示例
每个示例都可以直接运行，查看不同工厂创建的产品组合：
```bash
python example-1.py  # 运行家具工厂示例
python example-2.py  # 运行电子设备工厂示例
python example-3.py  # 运行汽车制造工厂示例
```

## 进阶学习资源
1. 《设计模式：可复用面向对象软件的基础》- GoF
2. 《Head First设计模式》- Eric Freeman
3. Python设计模式相关博客和教程
4. 开源项目中的抽象工厂模式应用实例

## 常见问题
1. 抽象工厂模式和工厂方法模式的区别是什么？
2. 如何选择使用抽象工厂模式还是建造者模式？
3. 抽象工厂模式如何支持开闭原则？
4. 如何处理抽象工厂模式中的产品族扩展？
5. 如何确保产品族的一致性？
