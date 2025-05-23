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

本项目提供了四个不同难度级别的单例模式实现示例：

### 1. 基础版 (example-1.py) - 难度：★☆☆☆☆
最简单的单例模式实现，适合初学者：
- 使用基本的 `__new__` 方法实现单例
- 展示了单例模式的核心概念
- 包含简单的属性访问和实例验证
- 适合理解单例模式的基本原理

**运行方法：**
```bash
python example-1.py
```

**预期输出：**
```
第一个实例: 这是一个简单的单例示例
第二个实例: 这是一个简单的单例示例

验证是否是同一个对象:
singleton1 的内存地址: 140712345678912
singleton2 的内存地址: 140712345678912
singleton1 和 singleton2 是否是同一个对象: True

修改singleton1后，singleton2的值: 修改后的值
```

### 2. 中级版 (example-2.py) - 难度：★★★☆☆
线程安全的单例模式实现，适合进阶学习：
- 使用双重检查锁定模式确保线程安全
- 实现了线程安全的计数器
- 包含多线程操作示例
- 展示了并发环境下的单例模式应用

**运行方法：**
```bash
python example-2.py
```

**预期输出：**
```
线程 Thread-1 (worker) - 计数器: 1
线程 Thread-2 (worker) - 计数器: 2
线程 Thread-3 (worker) - 计数器: 3
线程 Thread-1 (worker) - 计数器: 4
线程 Thread-2 (worker) - 计数器: 5
线程 Thread-3 (worker) - 计数器: 6
线程 Thread-1 (worker) - 计数器: 7
线程 Thread-2 (worker) - 计数器: 8
线程 Thread-3 (worker) - 计数器: 9

最终结果:
计数器最终值: 9
数据内容: {'key_1': 'value_1', 'key_2': 'value_2', ...}
```

### 3. 装饰器版 (example-decorator.py) - 难度：★★★☆☆
使用装饰器实现单例模式，展示更灵活的实现方式：
- 使用装饰器模式实现单例
- 模拟数据库连接的实际应用场景
- 展示装饰器单例的优势和使用方法
- 包含完整的业务逻辑示例

**运行方法：**
```bash
python example-decorator.py
```

**预期输出：**
```
=== 装饰器单例模式示例 ===

1. 创建第一个数据库连接实例:
创建数据库连接: localhost:5432/mydb

2. 创建第二个数据库连接实例:

3. 验证单例:
db1 的内存地址: 140712345678912
db2 的内存地址: 140712345678912
db1 和 db2 是否是同一个对象: True

4. 连接信息:
db1 连接信息: {'host': 'localhost', 'port': 5432, 'database': 'mydb', 'is_connected': False, 'connection_count': 0}
db2 连接信息: {'host': 'localhost', 'port': 5432, 'database': 'mydb', 'is_connected': False, 'connection_count': 0}

5. 使用数据库连接:
连接到数据库 localhost:5432/mydb
执行查询: SELECT * FROM users
查询结果: 查询结果: SELECT * FROM users 执行成功

6. 通过db2查看连接状态:
db2 连接状态: True
执行查询: SELECT * FROM products

7. 断开连接:
断开数据库连接
db1 连接状态: False
```

### 4. 高级版 (example-3.py) - 难度：★★★★★
完整的配置管理器实现，适合实际项目应用：
- 使用元类实现单例模式
- 实现了完整的配置管理功能
- 包含文件持久化和线程安全
- 使用类型提示和完整的错误处理
- 展示了单例模式在实际项目中的应用

**运行方法：**
```bash
python example-3.py
```

**预期输出：**
```
验证单例模式:
config1 的内存地址: 140712345678912
config2 的内存地址: 140712345678912
config1 和 config2 是否是同一个对象: True

初始配置:
应用名称: 示例应用
设置: {'debug': True, 'max_connections': 100}

更新后的配置:
应用名称: 新应用名称
设置: {'debug': False, 'max_connections': 200}
config2的应用名称: 新应用名称

重置后的配置:
应用名称: 示例应用
设置: {'debug': True, 'max_connections': 100}
```

**注意：** 运行example-3.py会在当前目录生成一个`config.json`配置文件。

## 学习路径建议

1. **初学者**：从 `example-1.py` 开始，理解单例模式的基本概念
2. **进阶学习**：学习 `example-2.py`，了解线程安全的重要性
3. **装饰器方式**：研究 `example-decorator.py`，学习装饰器实现单例的优势
4. **实际应用**：研究 `example-3.py`，学习如何在真实项目中应用单例模式

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
