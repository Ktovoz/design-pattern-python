# 适配器模式 (Adapter Pattern)

## 1. 模式简介
适配器模式是一种结构型设计模式，它允许不兼容的接口协同工作。就像现实生活中的电源适配器一样，它能够将一种接口转换成另一种接口，使得原本不兼容的类可以一起工作。

## 2. 核心概念

### 2.1 UML类图
```
+----------------+       +----------------+       +----------------+
|    Target      |       |    Adapter     |       |    Adaptee     |
+----------------+       +----------------+       +----------------+
| +request()     |<----->| +request()     |------>| +specificRequest()|
+----------------+       +----------------+       +----------------+
```

### 2.2 模式组成
1. **目标接口（Target）**
   - 定义客户端使用的特定接口
   - 例如：`EuropeanSocket`、`ComputerUSB`、`SmartHomeSystem`

2. **适配者（Adaptee）**
   - 需要被适配的类
   - 例如：`AmericanPlug`、`USBDevice`、`SmartDevice`

3. **适配器（Adapter）**
   - 将适配者接口转换为目标接口
   - 例如：`PowerAdapter`、`USBHub`、`SmartHomeAdapter`

### 2.3 实现方式
1. **类适配器（Class Adapter）**
   - 使用继承实现
   - 适配器同时继承目标接口和适配者类
   - 优点：实现简单，代码量少
   - 缺点：不够灵活，只能适配一个类

2. **对象适配器（Object Adapter）**
   - 使用组合实现
   - 适配器持有适配者的实例
   - 优点：更灵活，可以适配多个类
   - 缺点：实现相对复杂

## 3. 设计原则
1. **开闭原则（Open-Closed Principle）**
   - 适配器模式允许在不修改现有代码的情况下添加新的适配器
   - 新的适配器可以轻松地添加到系统中

2. **单一职责原则（Single Responsibility Principle）**
   - 适配器类只负责接口转换
   - 每个适配器只处理一种类型的适配

3. **接口隔离原则（Interface Segregation Principle）**
   - 目标接口应该保持简单
   - 只暴露客户端需要的方法

## 4. 适用场景
- 当希望使用一个已经存在的类，而它的接口不符合要求时
- 当想要创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类协同工作时
- 当需要使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口时

## 5. 代码示例

### 5.1 基础示例：电源适配器（难度：★☆☆☆☆）
```python
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
```

### 5.2 进阶示例：USB设备适配器（难度：★★☆☆☆）
```python
# 目标接口 - 电脑USB接口
class ComputerUSB(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass

# 适配者接口 - 各种USB设备
class USBDevice(ABC):
    @abstractmethod
    def get_data(self) -> List[str]:
        pass

# 适配器 - USB集线器
class USBHub(ComputerUSB):
    def __init__(self):
        self.devices: List[USBDevice] = []

    def add_device(self, device: USBDevice):
        self.devices.append(device)
```

### 5.3 高级示例：智能家居系统适配器（难度：★★★★☆）
```python
# 目标接口 - 智能家居系统
class SmartHomeSystem(ABC):
    @abstractmethod
    def control_device(self, device_id: str, command: str, params: Dict[str, Any] = None) -> str:
        pass

# 适配器 - 智能家居适配器
class SmartHomeAdapter(SmartHomeSystem):
    def __init__(self):
        self.devices: Dict[str, SmartDevice] = {}

    def add_device(self, device: SmartDevice):
        self.devices[device.device_id] = device
```

## 6. 优缺点分析

### 6.1 优点
- 允许接口不兼容的类协同工作
- 增加了类的透明性和复用性
- 将目标类和适配者类解耦
- 符合开闭原则

### 6.2 缺点
- 过多的使用适配器，会让系统非常零乱
- 适配器模式会增加代码的复杂性
- 在某些情况下，可能需要创建多个适配器

## 7. 最佳实践
1. 优先使用组合而不是继承
2. 保持适配器简单，只做必要的转换
3. 考虑使用工厂模式来创建适配器
4. 注意适配器可能带来的性能开销

## 8. 实际应用场景
1. 系统集成：将新系统与旧系统集成
2. 第三方库适配：使用不兼容的第三方库
3. 接口升级：在不破坏现有代码的情况下升级接口
4. 多平台支持：适配不同平台的API

## 9. 常见问题解答（FAQ）

### 9.1 什么时候应该使用适配器模式？
- 当你需要使用一个现有的类，但其接口与你的需求不匹配时
- 当你想创建一个可重用的类，该类可以与其他不相关的类协同工作时
- 当你想使用几个现有的子类，但不可能对每个子类都进行子类化时

### 9.2 适配器模式和装饰器模式有什么区别？
- 适配器模式：改变接口以匹配客户端的需求
- 装饰器模式：不改变接口，而是添加新的职责

### 9.3 如何选择类适配器和对象适配器？
- 类适配器：当你想适配一个类，且不需要适配多个类时
- 对象适配器：当你想适配多个类，或需要更灵活的适配方式时

### 9.4 适配器模式会影响性能吗？
- 是的，适配器会带来一些性能开销
- 在大多数情况下，这种开销是可以接受的
- 如果性能是关键因素，可以考虑其他解决方案

## 10. 学习指南

### 10.1 学习建议
1. 从简单的示例开始（如示例1）
2. 理解适配器模式的核心概念
3. 尝试实现自己的适配器
4. 研究实际项目中的适配器使用案例
5. 注意适配器模式与其他设计模式的区别

### 10.2 进阶主题
1. 双向适配器
2. 默认适配器
3. 适配器链
4. 适配器与依赖注入
5. 适配器与测试

## 11. 相关设计模式
- 装饰器模式：动态地给对象添加新的职责
- 代理模式：控制对其他对象的访问
- 桥接模式：将抽象部分与实现部分分离
- 组合模式：将对象组合成树形结构
- 外观模式：为子系统提供一个统一的接口
- 享元模式：共享细粒度对象
