# 组合模式 (Composite Pattern)

## 1. 模式简介
组合模式是一种结构型设计模式，它允许你将对象组合成树形结构来表示"部分-整体"的层次结构。组合模式使得客户端可以统一地处理单个对象和组合对象。

## 2. 核心概念
1. **组件（Component）**：定义所有对象的通用接口
2. **叶子（Leaf）**：表示组合中的叶子节点对象
3. **组合（Composite）**：定义有子部件的那些部件的行为

## 3. 模式结构
```
Component (抽象组件)
├── operation()
├── add()
└── remove()

├── Leaf (叶子节点)
│   └── operation()
│
└── Composite (组合节点)
    ├── children[]
    ├── operation()
    ├── add()
    └── remove()
```

## 4. 基础实现
```python
from abc import ABC, abstractmethod

# 抽象组件
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# 叶子节点
class Leaf(Component):
    def operation(self):
        return "Leaf operation"

# 组合节点
class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite operation with {results}"
```

## 5. 实现示例

### 5.1 基础示例：文件系统结构 ⭐
```python
# 文件系统示例展示了最基本的组合模式实现
- 抽象组件：FileSystemComponent
- 叶子节点：File（文件）
- 组合节点：Folder（文件夹）
```
这个示例展示了组合模式的基本结构，通过文件系统这个直观的例子，帮助理解组件、叶子和组合的关系。

### 5.2 进阶示例：餐厅菜单系统 ⭐⭐
```python
# 餐厅菜单示例展示了组合模式在业务场景中的应用
- 抽象组件：MenuComponent
- 叶子节点：MenuItem（具体菜品）
- 组合节点：MenuCategory（菜单分类）
```
这个示例增加了价格计算、描述等业务属性，展示了组合模式在实际业务中的应用。

### 5.3 高级示例：智能家居系统 ⭐⭐⭐
```python
# 智能家居示例展示了组合模式在复杂系统中的应用
- 抽象组件：SmartDevice
- 叶子节点：Light（灯）、Thermostat（温控器）
- 组合节点：Room（房间）、SmartHome（智能家居系统）
```
这个示例展示了组合模式在复杂系统中的应用，包含了状态管理、功耗计算等高级功能。

## 6. 适用场景
- 需要表示对象的部分-整体层次结构
- 希望用户忽略组合对象与单个对象的不同
- 需要统一处理组合结构和单个对象
- 需要动态地组合对象

## 7. 优缺点分析

### 7.1 优点
1. 定义了包含基本对象和组合对象的类层次结构
2. 简化了客户端代码，客户端可以一致地使用组合结构和单个对象
3. 使得更容易增加新类型的组件
4. 提供了灵活性和可扩展性

### 7.2 缺点
1. 使得设计变得更加抽象
2. 可能难以限制组合中的组件类型
3. 在特定情况下可能导致系统过于一般化

## 8. 实现要点
1. **抽象组件设计**
   - 定义所有对象共有的接口
   - 声明管理子组件的接口
   - 实现默认行为

2. **叶子节点实现**
   - 实现组件接口
   - 不包含子组件
   - 实现具体业务逻辑

3. **组合节点实现**
   - 实现组件接口
   - 管理子组件集合
   - 实现子组件管理方法

## 9. 常见问题与解决方案

### 9.1 类型安全问题
**问题**：如何确保组合中只能添加特定类型的组件？
**解决方案**：
```python
class Composite(Component):
    def add(self, component):
        if not isinstance(component, Component):
            raise TypeError("只能添加Component类型的对象")
        self._children.append(component)
```

### 9.2 性能优化
**问题**：如何处理大型组合结构的性能问题？
**解决方案**：
- 使用缓存机制
- 实现延迟加载
- 采用迭代器模式遍历

### 9.3 循环引用
**问题**：如何避免组合结构中的循环引用？
**解决方案**：
```python
class Composite(Component):
    def add(self, component):
        if component is self:
            raise ValueError("不能添加自身作为子组件")
        if self._is_ancestor(component):
            raise ValueError("不能添加祖先作为子组件")
        self._children.append(component)

    def _is_ancestor(self, component):
        for child in self._children:
            if child is component or child._is_ancestor(component):
                return True
        return False
```

## 10. 进阶应用

### 10.1 组合模式与访问者模式结合
```python
class Visitor:
    def visit_leaf(self, leaf):
        pass

    def visit_composite(self, composite):
        pass

class Component:
    def accept(self, visitor):
        pass

class Leaf(Component):
    def accept(self, visitor):
        visitor.visit_leaf(self)

class Composite(Component):
    def accept(self, visitor):
        visitor.visit_composite(self)
        for child in self._children:
            child.accept(visitor)
```

### 10.2 组合模式与命令模式结合
```python
class Command:
    def execute(self):
        pass

class CompositeCommand(Command):
    def __init__(self):
        self._commands = []

    def add(self, command):
        self._commands.append(command)

    def execute(self):
        for command in self._commands:
            command.execute()
```

## 11. 测试策略

### 11.1 单元测试
- 测试叶子节点的行为
- 测试组合节点的管理方法
- 测试异常情况

### 11.2 集成测试
- 测试组合结构的完整性
- 测试组件间的交互
- 测试性能表现

## 12. 性能考虑

### 12.1 内存使用
- 注意组合结构的深度
- 考虑使用享元模式减少对象创建
- 适当使用缓存机制

### 12.2 时间复杂度
- 遍历操作：O(n)
- 查找操作：O(n)
- 添加/删除操作：O(1)

## 13. 相关设计模式
- **适配器模式**：用于将不兼容的接口转换为可兼容的接口
- **装饰器模式**：用于动态地给对象添加新的职责
- **代理模式**：用于控制对其他对象的访问
- **桥接模式**：用于将抽象部分与实现部分分离
- **外观模式**：用于为子系统提供一个统一的接口
- **享元模式**：用于减少对象的创建，降低内存占用

## 14. 最佳实践
1. 确保组件接口足够通用，能够支持所有子类
2. 在组合类中实现子组件管理方法
3. 考虑使用迭代器模式遍历组合结构
4. 适当使用缓存优化性能
5. 注意处理异常情况

## 15. 注意事项
1. 避免过度使用组合模式
2. 注意处理循环引用问题
3. 考虑性能影响
4. 合理设计组件接口
5. 注意内存管理

## 16. 扩展阅读
1. 《设计模式：可复用面向对象软件的基础》
2. 《Head First设计模式》
3. 《Python设计模式》
