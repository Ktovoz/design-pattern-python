# 模板方法模式 (Template Method Pattern)

## 一、模式简介
模板方法模式是一种行为型设计模式，它在父类中定义了一个算法的骨架，允许子类在不改变算法结构的情况下重写算法的特定步骤。这种模式非常适合处理有固定流程，但每个步骤实现可能不同的场景。

### 1. 模式的本质
模板方法模式体现了"好莱坞原则"（Don't call us, we'll call you）：
- 父类控制整体算法流程
- 子类提供具体实现细节
- 父类在合适的时候调用子类方法

### 2. 模式结构
- **抽象类（Abstract Class）**：定义模板方法和原语操作
- **具体类（Concrete Class）**：实现原语操作
- **模板方法（Template Method）**：定义算法骨架
- **钩子方法（Hook Method）**：提供默认实现，子类可选择性重写

### 3. 主要角色
1. **抽象类**：
   - 定义抽象的原语操作（Primitive Operations）
   - 实现模板方法定义算法的顺序
   - 提供钩子操作（Hook Operations）

2. **具体类**：
   - 实现原语操作以完成算法中特定步骤
   - 可以重写钩子操作

### 4. 核心组成
```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):  # 模板方法
        self.step1()
        self.step2()
        if self.hook():
            self.step3()
    
    @abstractmethod
    def step1(self): pass  # 必须实现
    
    @abstractmethod
    def step2(self): pass  # 必须实现
    
    def step3(self):  # 具体方法
        pass
    
    def hook(self):   # 钩子方法
        return True

class ConcreteClass(AbstractClass):
    def step1(self):
        print("具体实现步骤1")
    
    def step2(self):
        print("具体实现步骤2")
    
    def hook(self):
        return False  # 改变算法流程
```

### 5. 适用场景
1. 算法的整体步骤固定，但某些步骤的实现可能不同
2. 多个类共有相同的行为，但实现细节不同
3. 需要控制子类扩展的场景

### 6. 优缺点
**优点：**
1. **代码复用**：将公共代码放在父类中
2. **扩展性好**：可以通过子类来扩展新的行为
3. **封装性好**：对算法步骤进行封装
4. **好莱坞原则**：父类调用子类方法，而不是相反

**缺点：**
1. 每个不同的实现都需要一个子类，可能导致类的数量增加
2. 父类中的模板方法会约束子类的行为
3. 继承关系自身的缺点，如果父类改变，所有子类都要改变

## 二、实现示例

### 1. 基础示例：饮料制作（★）
位于 `example-1.py`，展示了最基础的模板方法模式实现：
```python
class Beverage:
    def make_beverage(self):  # 模板方法
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
```
特点：
- 简单的算法骨架
- 基础的钩子方法使用
- 适合初学者理解模式的核心概念
- 实现了饮料制作的基本流程
- 包含咖啡和茶两种具体实现

### 2. 进阶示例：衣物洗涤（★★）
位于 `example-2.py`，展示了更复杂的实现：
- 实现了衣物洗涤的完整流程
- 区分精致衣物和普通衣物的处理方式
- 特点：
  - 参数化的模板方法
  - 多个抽象方法的组合
  - 更复杂的业务逻辑处理

### 3. 高级示例：智能家居系统（★★★）
位于 `example-3.py`，展示了高级的实现方案：
- 实现了智能家居场景控制系统
- 包含多个子系统的协同工作
- 特点：
  - 复杂的状态管理
  - 完整的日志记录
  - 基于时间的场景控制
  - 多层次的抽象和扩展

## 三、设计原则与最佳实践

### 1. 核心设计原则
- **单一职责原则**：每个类专注于一个特定的任务
- **开闭原则**：通过继承扩展，而不是修改
- **里氏替换原则**：子类必须能够替换父类

### 2. 代码规范
1. **命名约定**
```python
def template_method(self):     # 使用 _template 后缀
def _required_operation(self): # 使用下划线前缀表示内部方法
def hook_method(self):         # 使用 hook_ 前缀表示钩子方法
```

2. **错误处理**
```python
class AbstractClass(ABC):
    def template_method(self):
        try:
            self.required_step()
            self.optional_step()
        except Exception as e:
            self.handle_error(e)
    
    def handle_error(self, error):
        print(f"错误处理: {error}")
```

3. **参数传递**
```python
class AbstractClass(ABC):
    def template_method(self, config: dict):
        self.step1(config.get('param1'))
        self.step2(config.get('param2'))
```

### 3. 测试策略
```python
import unittest

class TemplateMethodTest(unittest.TestCase):
    def test_template_method(self):
        concrete = ConcreteClass()
        result = concrete.template_method()
        self.assertEqual(expected_result, result)
```

### 4. 实践建议
1. 优先使用组合而不是继承，除非确实需要使用模板方法模式
2. 清晰地标记哪些方法是钩子，哪些是必须实现的抽象方法
3. 在文档中说明算法的整体流程
4. 模板方法中的步骤要尽量少，保持在5-7个之内
5. 考虑使用钩子方法来使得部分步骤可选

## 四、常见问题与解决方案

### 1. 继承层次问题
- **问题**：继承层次变得复杂，难以维护
- **解决方案**：
  - 使用组合替代部分继承
  - 将复杂逻辑拆分为多个小的模板方法
  - 使用策略模式处理变化较大的部分

### 2. 代码重复问题
- **问题**：子类之间存在重复代码
- **解决方案**：
  - 将共同代码提取到抽象类中
  - 使用辅助方法减少重复
  - 考虑使用组合模式

### 3. 扩展性问题
- **问题**：需要频繁修改算法步骤
- **解决方案**：
  - 使用钩子方法增加灵活性
  - 将可变部分抽取为策略类
  - 使用配置文件控制流程

## 五、实际应用场景

### 1. 数据处理流程
- 数据验证
- 数据转换
- 数据存储

### 2. 构建系统
- 代码编译
- 测试运行
- 部署发布

### 3. 报表生成
- 数据收集
- 数据处理
- 格式化输出

## 六、性能优化与注意事项

### 1. 性能优化建议
- 避免过多的抽象层次
- 合理使用缓存
- 注意方法调用开销

### 2. 扩展性建议
- 预留扩展点
- 使用配置文件
- 考虑插件机制

### 3. 需要避免的做法
- 过度使用钩子方法
- 在模板方法中使用过多的条件判断
- 违反里氏替换原则

## 七、进阶主题

### 1. 与其他模式的组合
- **策略模式**：模板方法使用继承来改变算法的部分内容，策略模式使用组合来改变整个算法
- **工厂方法**：常常和模板方法一起使用，工厂方法可以作为模板方法中的一个步骤
- **观察者模式**：可以用于在模板方法的某些步骤中通知其他对象

### 2. 模式变体
- 参数化模板方法
- 多层次模板方法
- 可配置模板方法

## 八、实践练习
1. **基础练习**：实现一个简单的文件处理模板
2. **进阶练习**：实现一个可配置的数据处理流程
3. **高级练习**：实现一个支持插件的构建系统

## 九、参考资源
1. 设计模式相关书籍
2. 开源项目中的实现
3. 在线教程和文档

## 十、总结
模板方法模式是一个强大的设计模式，它通过固定算法骨架和允许子类定制特定步骤来提供灵活性。通过合理使用这个模式，我们可以：
- 提高代码复用性
- 保持算法结构的稳定
- 支持灵活的扩展
- 降低维护成本
- 实现更好的代码组织和管理
