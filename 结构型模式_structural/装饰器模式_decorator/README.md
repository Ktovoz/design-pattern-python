# 装饰器模式 (Decorator Pattern)

## 1. 模式简介
装饰器模式是一种结构型设计模式，它允许你将对象放入包含行为的特殊封装对象中，以增强其功能。这种模式的核心思想是：不改变原有对象的情况下，动态地给对象添加新的职责。

## 2. 模式结构

### 2.1 UML类图
```
                    +----------------+
                    |   Component    |
                    +----------------+
                    | +operation()   |
                    +----------------+
                           ^
                           |
        +------------------+------------------+
        |                                     |
+---------------+                    +----------------+
|ConcreteComponent|                    |   Decorator    |
+---------------+                    +----------------+
| +operation()   |                    | -component     |
+---------------+                    | +operation()   |
                                    +----------------+
                                           ^
                                           |
                           +---------------+---------------+
                           |                               |
                    +---------------+              +---------------+
                    |ConcreteDecoratorA|              |ConcreteDecoratorB|
                    +---------------+              +---------------+
                    | +operation()   |              | +operation()   |
                    | +addedBehavior()|             | +addedBehavior()|
                    +---------------+              +---------------+
```

### 2.2 核心角色
1. **Component（抽象组件）**：定义对象的接口，可以给这些对象动态地添加职责
2. **ConcreteComponent（具体组件）**：定义具体的对象，可以给这个对象添加一些职责
3. **Decorator（抽象装饰类）**：继承自Component，从外类来扩展Component类的功能
4. **ConcreteDecorator（具体装饰类）**：继承自Decorator，负责给Component添加职责

## 3. 实现指南

### 3.1 实现步骤
1. **定义基础接口**
   - 创建抽象组件接口（Component）
   - 声明所有具体组件和装饰器共有的方法

2. **创建具体组件**
   - 实现基础接口
   - 定义基本行为

3. **创建装饰器基类**
   - 继承自组件接口
   - 持有组件对象的引用
   - 实现基础方法，委托给被装饰对象

4. **实现具体装饰器**
   - 继承装饰器基类
   - 添加新的行为
   - 在原有行为基础上进行扩展

### 3.2 代码模板
```python
# 1. 接口设计
class Component:
    def operation(self):
        pass

# 2. 具体组件
class ConcreteComponent(Component):
    def operation(self):
        return "基本操作"

# 3. 装饰器基类
class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

# 4. 具体装饰器
class ConcreteDecorator(Decorator):
    def operation(self):
        return f"装饰后的{self._component.operation()}"
```

## 4. 示例代码

### 4.1 咖啡装饰器（初级）
```python
# 基础组件：咖啡
# 装饰器：牛奶、糖
# 功能：动态添加配料，计算价格
```
特点：
- 使用咖啡作为基础组件
- 通过装饰器添加牛奶、糖等配料
- 动态计算最终价格和描述

### 4.2 手机壳装饰器（中级）
```python
# 基础组件：手机
# 装饰器：硅胶壳、防摔边框、钢化膜
# 功能：组合多种保护方案，计算保护等级
```
特点：
- 多个装饰器的组合使用
- 属性的动态计算
- 功能列表的维护

### 4.3 智能家居装饰器（高级）
```python
# 基础组件：智能灯
# 装饰器：颜色控制、亮度控制、定时控制
# 功能：状态管理、命令处理、能耗计算
```
特点：
- 复杂的状态管理
- 命令模式与装饰器模式的结合
- 动态能耗计算
- 定时任务处理

## 5. 设计原则与最佳实践

### 5.1 设计原则
1. **单一职责原则**
   - 每个装饰器只负责一个功能
   - 避免装饰器之间的职责重叠

2. **开闭原则**
   - 对扩展开放
   - 对修改关闭

3. **里氏替换原则**
   - 装饰器必须能够替代被装饰的组件
   - 保持接口的一致性

4. **接口隔离原则**
   - 装饰器接口应该精简
   - 避免不必要的方法

### 5.2 最佳实践
1. 保持装饰器类的简单性
2. 避免装饰器之间的依赖
3. 合理使用装饰器的组合
4. 注意装饰器的顺序
5. 控制装饰器的数量

## 6. 常见问题与解决方案

### 6.1 装饰器顺序问题
**问题**：多个装饰器的应用顺序会影响最终结果
**解决方案**：
- 明确定义装饰器的优先级
- 使用组合模式管理装饰器顺序
- 在文档中清晰说明装饰器顺序的影响

### 6.2 性能开销
**问题**：多层装饰可能导致性能下降
**解决方案**：
- 控制装饰器层数
- 使用缓存机制
- 考虑使用其他模式（如策略模式）替代

### 6.3 调试困难
**问题**：多层装饰使调试变得复杂
**解决方案**：
- 添加日志记录
- 实现调试模式
- 使用装饰器标识

## 7. 测试策略

### 7.1 单元测试
- 测试每个装饰器的独立功能
- 验证装饰器组合的正确性

### 7.2 集成测试
- 测试装饰器链的完整性
- 验证装饰器顺序的影响

### 7.3 性能测试
- 测试多层装饰的性能影响
- 验证内存使用情况

## 8. 实际应用场景

### 8.1 常见应用
1. GUI组件库
2. I/O流处理
3. 日志记录
4. 缓存实现
5. 权限控制
6. 数据验证
7. 性能监控

### 8.2 实际示例
1. **日志装饰器**
```python
class LogDecorator:
    def __init__(self, component):
        self._component = component

    def operation(self):
        print("开始操作")
        result = self._component.operation()
        print("结束操作")
        return result
```

2. **缓存装饰器**
```python
class CacheDecorator:
    def __init__(self, component):
        self._component = component
        self._cache = {}

    def operation(self, key):
        if key in self._cache:
            return self._cache[key]
        result = self._component.operation(key)
        self._cache[key] = result
        return result
```

3. **权限装饰器**
```python
class PermissionDecorator:
    def __init__(self, component):
        self._component = component

    def operation(self, user):
        if self._check_permission(user):
            return self._component.operation()
        raise PermissionError("权限不足")
```

## 9. 进阶主题

### 9.1 装饰器模式与AOP
- 横切关注点的处理
- 面向切面编程的实现

### 9.2 装饰器模式与函数式编程
- 高阶函数的使用
- 函数组合的实现

### 9.3 装饰器模式与元编程
- 动态类生成
- 属性装饰器

## 10. 学习资源

### 10.1 推荐书籍
- 《Head First设计模式》
- 《设计模式：可复用面向对象软件的基础》

### 10.2 在线教程
- Python装饰器教程
- 设计模式实战案例

### 10.3 开源项目
- Django框架中的装饰器应用
- Flask框架中的装饰器实现

## 11. 练习建议
1. 实现一个简单的日志装饰器
2. 创建一个缓存装饰器
3. 设计一个权限控制装饰器
4. 实现装饰器的组合使用
5. 尝试解决装饰器顺序问题

## 12. 相关设计模式
1. **适配器模式**
   - 装饰器模式改变对象的接口
   - 适配器模式给对象一个全新的接口

2. **代理模式**
   - 装饰器模式为对象添加功能
   - 代理模式控制对对象的访问

3. **组合模式**
   - 装饰器模式可以看作是一个退化的组合模式
   - 装饰器模式只有一个子组件

4. **策略模式**
   - 装饰器模式改变对象的外表
   - 策略模式改变对象的内核
