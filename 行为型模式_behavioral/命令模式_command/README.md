# 命令模式 (Command Pattern)

## 一、基础概念

### 1.1 简介
命令模式是一种行为型设计模式，它将请求封装成对象，让你可以使用不同的请求参数化客户端，实现请求的排队、记录日志、撤销操作等功能。这种模式将发出请求的对象和执行请求的对象解耦，提高了系统的灵活性。

### 1.2 主要角色
1. **命令(Command)**：声明执行操作的接口
2. **具体命令(ConcreteCommand)**：实现命令接口，定义动作和接收者之间的绑定关系
3. **调用者(Invoker)**：要求命令执行请求
4. **接收者(Receiver)**：知道如何执行命令相关的操作
5. **客户端(Client)**：创建具体命令对象并设定接收者

### 1.3 UML类图
```
┌───────────────┐         ┌───────────────┐
│    Client     │         │    Invoker    │
└───────────────┘         └───────────────┘
        │                        │
        │                        │
        ▼                        ▼
┌───────────────┐    uses    ┌───────────────┐
│   Command     │◄───────────│ ConcreteCommand│
└───────────────┘            └───────────────┘
                                     │
                                     │ has-a
                                     ▼
                            ┌───────────────┐
                            │   Receiver    │
                            └───────────────┘
```

## 二、核心实现

### 2.1 基础接口设计
```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
        
    @abstractmethod
    def undo(self):
        pass
```

### 2.2 命令对象状态管理
- **状态存储**：命令对象需要存储执行命令所需的状态
- **参数传递**：通过构造函数或setter方法设置命令参数
- **状态恢复**：用于实现撤销功能时的状态回滚

### 2.3 命令队列
```python
class CommandQueue:
    def __init__(self):
        self._commands = []
        
    def add_command(self, command):
        self._commands.append(command)
        
    def process_commands(self):
        for command in self._commands:
            command.execute()
            
    def clear(self):
        self._commands.clear()
```

## 三、示例实现
本项目提供了三个不同难度的命令模式示例：

### 3.1 基础示例：电视遥控器 (example-1.py)
**难度：★☆☆☆☆ 入门级**
- 实现了简单的电视遥控器控制功能
- 包含开关机和换台等基本操作
- 展示命令模式的基本结构
- 适合初学者理解命令模式的核心概念

### 3.2 进阶示例：智能家居控制 (example-2.py)
**难度：★★★☆☆ 进阶级**
- 实现了智能家居设备的控制系统
- 包含多个设备（灯光、空调）的控制
- 引入了命令撤销功能
- 展示了命令模式在实际应用中的扩展

### 3.3 高级示例：智能咖啡机 (example-3.py)
**难度：★★★★★ 高级应用**
- 实现了一个复杂的咖啡机控制系统
- 包含多种咖啡制作流程
- 引入了宏命令（组合命令）
- 添加了命令日志记录功能
- 完整的异常处理和状态管理

## 四、高级特性

### 4.1 宏命令实现
```python
class MacroCommand(Command):
    def __init__(self, commands):
        self._commands = commands
        
    def execute(self):
        for command in self._commands:
            command.execute()
            
    def undo(self):
        for command in reversed(self._commands):
            command.undo()
```

### 4.2 事务支持
```python
class Transaction:
    def __init__(self):
        self._commands = []
        self._state = "new"  # new, committed, rolled_back
        
    def commit(self):
        try:
            for command in self._commands:
                command.execute()
            self._state = "committed"
        except Exception:
            self.rollback()
            raise
```

### 4.3 命令日志系统
```python
class CommandLogger:
    def log_execution(self, command, result):
        timestamp = datetime.now()
        command_name = command.__class__.__name__
        log_entry = f"{timestamp}: Executed {command_name} - Result: {result}"
```

## 五、最佳实践

### 5.1 命名规范
- 命令类名应以动词开头：`SaveCommand`、`DeleteCommand`
- 方法名应清晰表达意图：`execute()`、`undo()`、`redo()`

### 5.2 异常处理
```python
class RobustCommand(Command):
    def execute(self):
        try:
            self._do_execute()
        except Exception as e:
            self._handle_error(e)
            raise
```

### 5.3 性能优化
1. 使用命令对象池复用命令对象
2. 延迟加载接收者
3. 批量处理命令
4. 实现命令缓存
5. 异步执行命令

### 5.4 测试策略
1. **单元测试**
   - 测试命令执行
   - 测试撤销功能
   - 测试异常处理
2. **集成测试**
   - 测试命令队列
   - 测试事务完整性
   - 测试日志记录

## 六、设计模式对比

### 6.1 命令模式 vs 策略模式
| 特性 | 命令模式 | 策略模式 |
|------|----------|----------|
| 目的 | 将请求封装为对象 | 定义算法族 |
| 关注点 | 请求的发送者和接收者解耦 | 算法的互换性 |
| 扩展性 | 容易添加新命令 | 容易添加新策略 |

### 6.2 命令模式 vs 观察者模式
| 特性 | 命令模式 | 观察者模式 |
|------|----------|------------|
| 通信方式 | 单向调用 | 发布/订阅 |
| 耦合度 | 发送者和接收者完全解耦 | 观察者与主题松耦合 |
| 用途 | 封装调用 | 状态变化通知 |

## 七、进阶主题

### 7.1 响应式命令模式
- 结合RxPY实现响应式命令
- 处理异步命令执行
- 实现命令流水线

### 7.2 分布式命令模式
- 命令序列化
- 网络传输
- 分布式事务处理

### 7.3 智能命令系统
- 命令优先级管理
- 命令冲突解决
- 自适应命令调度

## 八、学习路径

### 8.1 基础阶段
- 理解命令模式的基本概念
- 学习示例1：电视遥控器
- 掌握基本命令实现

### 8.2 进阶阶段
- 学习撤销/重做机制
- 研究示例2：智能家居控制
- 理解状态管理

### 8.3 高级阶段
- 掌握宏命令和日志
- 学习示例3：智能咖啡机
- 深入理解事务和异常处理

### 8.4 专家阶段
- 设计可扩展的命令系统
- 实现分布式命令处理
- 优化性能和可维护性

## 九、常见问题与解决方案

### 9.1 命令对象过多
- 使用工厂模式创建命令
- 使用组合命令减少类数量
- 考虑使用享元模式

### 9.2 状态维护复杂
- 使用备忘录模式保存状态
- 实现增量式撤销
- 使用状态快照

### 9.3 性能问题
- 使用命令缓存
- 实现批处理
- 异步执行命令

## 十、实际应用场景
1. GUI按钮和菜单项的点击事件处理
2. 多级撤销功能的实现
3. 事务管理系统
4. 工作流系统
5. 游戏中的按键映射系统

## 十一、相关设计模式
- **策略模式**：命令模式和策略模式都可以参数化对象的行为
- **观察者模式**：命令对象可以实现观察者接口
- **组合模式**：可用于实现宏命令
- **备忘录模式**：可与命令模式结合实现可撤销操作
- **原型模式**：可用于复制命令对象
