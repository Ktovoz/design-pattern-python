# 原型模式 (Prototype Pattern)

## 简介
原型模式是一种创建型设计模式，它允许你通过复制现有对象来创建新对象，而无需重新创建对象。这种模式特别适用于当创建对象的成本较大时，通过克隆已有对象来创建新对象可以显著提高性能。

## 核心概念
1. **原型接口/抽象类**：定义了克隆方法的接口
2. **具体原型类**：实现克隆方法的具体类
3. **客户端**：使用原型对象创建新对象

## UML类图
```
+----------------+       +-----------------+
|    Client      |------>|   Prototype     |
+----------------+       +-----------------+
                         | +clone()        |
                         +-----------------+
                                ^
                                |
                        +-----------------+
                        |  ConcretePrototype |
                        +-----------------+
                        | +clone()        |
                        +-----------------+
```

## 适用场景
- 当要实例化的类是在运行时刻指定时
- 为了避免创建一个与产品类层次平行的工厂类层次时
- 当一个类的实例只能有几个不同状态组合中的一种时
- 当创建对象的成本较大时
- 当需要避免使用工厂类时

## 优点
- 性能提高：通过克隆已有对象来创建新对象，避免了重复的初始化过程
- 逃避构造函数的约束：可以创建任意复杂度的对象
- 简化对象的创建：不需要知道对象的具体类型
- 减少子类的数量：不需要为每种产品创建对应的工厂类

## 缺点
- 需要为每一个类配备一个克隆方法
- 克隆方法比较难实现，特别是当对象包含循环引用时
- 需要正确实现深拷贝和浅拷贝
- 可能违反开闭原则

## 实现方式
在Python中，我们可以通过以下方式实现原型模式：
1. 使用 `copy` 模块的 `deepcopy` 函数
2. 实现自定义的 `clone` 方法
3. 使用原型注册表管理多个原型

## 原型模式的实现步骤

### 1. 创建原型接口
```python
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
```

### 2. 实现具体原型类
```python
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value
    
    def clone(self):
        return deepcopy(self)
```

### 3. 使用原型对象
```python
# 创建原型对象
prototype = ConcretePrototype("原始值")

# 克隆对象
clone1 = prototype.clone()
clone2 = prototype.clone()
```

## 实现注意事项

### 1. 深拷贝vs浅拷贝
- 浅拷贝：只复制对象的第一层属性
- 深拷贝：递归复制对象的所有层级属性
- 在Python中使用`copy.deepcopy()`实现深拷贝

### 2. 克隆方法的实现
```python
def clone(self):
    return deepcopy(self)  # 深拷贝
    # 或
    return copy(self)      # 浅拷贝
```

### 3. 原型注册表的使用
```python
class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}
    
    def register(self, name, prototype):
        self._prototypes[name] = prototype
    
    def clone(self, name):
        return self._prototypes[name].clone()
```

## 常见问题及解决方案

### 1. 循环引用问题
```python
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def clone(self):
        # 使用深拷贝处理循环引用
        return deepcopy(self)
```

### 2. 性能优化
```python
class CachedPrototype:
    def __init__(self):
        self._cache = {}
    
    def get_clone(self, key):
        if key not in self._cache:
            self._cache[key] = self.clone()
        return deepcopy(self._cache[key])
```

### 3. 部分克隆
```python
class PartialClone:
    def __init__(self, data):
        self.data = data
    
    def clone(self, attributes=None):
        if attributes is None:
            return deepcopy(self)
        
        new_obj = self.__class__.__new__(self.__class__)
        for attr in attributes:
            setattr(new_obj, attr, deepcopy(getattr(self, attr)))
        return new_obj
```

## 性能考虑

1. **内存使用**
   - 深拷贝会创建完整的对象副本
   - 对于大型对象，考虑使用浅拷贝
   - 使用缓存机制减少克隆次数

2. **克隆速度**
   - 使用 `__slots__` 优化属性访问
   - 实现自定义的 `__copy__` 和 `__deepcopy__` 方法
   - 考虑使用 `copyreg` 模块优化特定类型的复制

3. **缓存策略**
   ```python
   class CachedPrototype:
       def __init__(self):
           self._cache = {}
       
       def get_clone(self, key):
           if key not in self._cache:
               self._cache[key] = self.clone()
           return deepcopy(self._cache[key])
   ```

## 示例说明

### 示例1：文具原型（简单）⭐
```python
# 使用文具（铅笔）作为例子
class Stationery:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    def clone(self):
        return deepcopy(self)
```
这个示例展示了原型模式的基本用法：
- 简单的属性复制
- 基本的克隆功能
- 适合初学者理解原型模式的核心概念

### 示例2：电子产品原型（中等）⭐⭐
```python
class ElectronicDevice(ABC):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.specs = {}
```
这个示例展示了更复杂的应用：
- 抽象基类的使用
- 继承关系
- 动态属性管理
- 适合理解原型模式在复杂对象中的应用

### 示例3：家具原型（复杂）⭐⭐⭐
```python
class FurnitureRegistry:
    def __init__(self):
        self._prototypes: Dict[str, FurnitureComponent] = {}
```
这个示例展示了原型模式的高级应用：
- 原型注册表
- 组合关系
- 复杂对象结构
- 类型提示
- 适合理解原型模式在企业级应用中的应用

## 实际应用场景

### 1. 游戏开发
```python
class GameObject:
    def __init__(self, name, position, properties):
        self.name = name
        self.position = position
        self.properties = properties
    
    def clone(self):
        return deepcopy(self)

# 使用示例
enemy_prototype = GameObject("敌人", (0, 0), {"health": 100, "speed": 5})
enemy1 = enemy_prototype.clone()
enemy2 = enemy_prototype.clone()
```

### 2. 文档处理
```python
class Document:
    def __init__(self, content, style):
        self.content = content
        self.style = style
    
    def clone(self):
        return deepcopy(self)

# 使用示例
template = Document("模板内容", {"font": "Arial", "size": 12})
document1 = template.clone()
document2 = template.clone()
```

### 3. 配置管理
```python
class Configuration:
    def __init__(self, settings):
        self.settings = settings
    
    def clone(self):
        return deepcopy(self)

# 使用示例
default_config = Configuration({"theme": "dark", "language": "zh"})
user_config = default_config.clone()
user_config.settings["theme"] = "light"
```

## 测试策略

### 1. 单元测试
```python
def test_prototype_clone():
    # 创建原型
    original = ConcretePrototype("test")
    
    # 克隆对象
    clone = original.clone()
    
    # 验证克隆
    assert clone is not original
    assert clone.value == original.value
```

### 2. 集成测试
```python
def test_prototype_registry():
    registry = PrototypeRegistry()
    prototype = ConcretePrototype("test")
    
    # 注册原型
    registry.register("test", prototype)
    
    # 获取克隆
    clone = registry.clone("test")
    
    # 验证克隆
    assert clone is not prototype
    assert clone.value == prototype.value
```

## 相关设计模式
- 工厂方法模式：两者都用于创建对象，但原型模式通过克隆创建，工厂方法通过实例化创建
- 抽象工厂模式：可以结合使用，使用原型模式来创建具体产品
- 单例模式：可以结合使用，将单例对象作为原型
- 建造者模式：可以结合使用，使用原型模式来创建基础对象

## 最佳实践
1. 在实现克隆方法时，考虑使用深拷贝还是浅拷贝
2. 使用原型注册表管理多个原型
3. 在克隆方法中处理循环引用
4. 考虑使用抽象基类定义克隆接口
5. 在需要创建大量相似对象时使用原型模式

## 总结
原型模式是一种强大的创建型设计模式，它通过克隆现有对象来创建新对象，避免了重复的初始化过程。在Python中，我们可以通过 `copy` 模块和自定义的克隆方法来实现原型模式。通过合理使用原型模式，我们可以提高代码的可维护性和性能。
