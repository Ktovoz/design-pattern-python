# 单例模式 (Singleton Pattern)

## 简介
单例模式是一种创建型设计模式，它确保一个类只有一个实例，并提供一个全局访问点。

## 适用场景
- 当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时
- 当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时

## 实现方式

### 1. 使用 `__new__` 方法（基础实现）
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### 2. 使用装饰器（灵活实现）
```python
def singleton_decorator(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
```

### 3. 使用元类（高级实现）
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
```

## 实现示例

本项目提供了三个不同难度级别的单例模式实现示例：

### 1. 基础版 (example-1.py) - 难度：★☆☆☆☆
最简单的单例模式实现，适合初学者：
- 使用基本的 `__new__` 方法实现单例
- 展示了单例模式的核心概念
- 包含简单的属性访问和实例验证
- 适合理解单例模式的基本原理

### 2. 中级版 (example-2.py) - 难度：★★★☆☆
线程安全的单例模式实现，适合进阶学习：
- 使用双重检查锁定模式确保线程安全
- 实现了线程安全的计数器
- 包含多线程操作示例
- 展示了并发环境下的单例模式应用

### 3. 高级版 (example-3.py) - 难度：★★★★★
完整的配置管理器实现，适合实际项目应用：
- 同时使用装饰器和元类两种方式实现单例
- 实现了完整的配置管理功能
- 包含文件持久化和线程安全
- 使用类型提示和完整的错误处理
- 展示了单例模式在实际项目中的应用

## 注意事项

### 1. 线程安全
- 在多线程环境中，需要考虑线程安全问题
- 使用锁机制确保线程安全
- 考虑使用双重检查锁定模式优化性能

### 2. 序列化问题
- 单例对象序列化后可能破坏单例特性
- 需要实现 `__reduce__` 方法处理序列化
- 考虑使用 `pickle` 模块的特殊处理

### 3. 继承问题
- 单例类的子类可能破坏单例特性
- 需要谨慎设计继承关系
- 考虑使用元类控制继承行为

## 最佳实践

### 1. 何时使用单例模式
- 配置管理
- 数据库连接池
- 日志记录器
- 缓存管理器
- 线程池

### 2. 何时避免使用单例模式
- 需要多个实例的场景
- 需要频繁创建和销毁的对象
- 需要依赖注入的场景
- 需要单元测试的类

### 3. 实现建议
- 优先使用装饰器方式，更灵活
- 考虑线程安全需求
- 提供清晰的访问接口
- 添加适当的文档说明
- 考虑使用依赖注入替代

## 优点
- 确保系统内存中该类只存在一个对象
- 允许对唯一实例的受控访问
- 单例模式可以充当全局变量，但避免了全局变量带来的问题

## 缺点
- 违反了单一职责原则
- 对测试是不利的
- 可能隐藏依赖关系
- 可能造成代码耦合
- 可能违反开闭原则

## 相关设计模式
- 工厂方法模式
- 抽象工厂模式
- 建造者模式
- 原型模式

## 常见问题解答

### 1. 如何测试单例类？
- 使用依赖注入
- 提供重置方法
- 使用模拟对象
- 考虑使用工厂方法

### 2. 如何处理单例的销毁？
- 实现 `__del__` 方法
- 提供显式的销毁方法
- 使用上下文管理器
- 考虑使用弱引用

### 3. 如何扩展单例类？
- 使用工厂方法
- 实现注册表模式
- 使用策略模式
- 考虑使用组合模式

## 扩展阅读
- [Python 单例模式最佳实践](https://python-patterns.guide/gang-of-four/singleton/)
- [线程安全的单例模式实现](https://en.wikipedia.org/wiki/Double-checked_locking)
- [Python 元类编程](https://docs.python.org/3/reference/datamodel.html#metaclasses)
