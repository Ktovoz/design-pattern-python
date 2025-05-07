# 状态模式 (State Pattern)

## 目录
- [模式介绍](#模式介绍)
- [核心概念](#核心概念)
- [模式结构](#模式结构)
- [适用场景](#适用场景)
- [示例代码](#示例代码)
- [实现要点](#实现要点)
- [设计考虑](#设计考虑)
- [优缺点分析](#优缺点分析)
- [最佳实践](#最佳实践)
- [相关设计模式](#相关设计模式)
- [常见问题](#常见问题)

## 模式介绍
状态模式是一种行为型设计模式，它允许一个对象在其内部状态改变时改变它的行为。这种模式将状态相关的行为封装在不同的状态类中，并将对象的行为委托给当前状态对象，使得对象在不同状态下可以有不同的行为，就像改变了对象的类一样。

### 为什么需要状态模式？
在传统的编程方式中，我们经常使用大量的条件语句来处理对象在不同状态下的行为：
```python
class TraditionalImplementation:
    def handle_state(self):
        if self.state == "StateA":
            # 处理 StateA 的逻辑
            pass
        elif self.state == "StateB":
            # 处理 StateB 的逻辑
            pass
        elif self.state == "StateC":
            # 处理 StateC 的逻辑
            pass
```
这种方式存在以下问题：
1. 代码难以维护和扩展
2. 状态逻辑分散在各处
3. 状态转换不明确
4. 违反开闭原则

## 核心概念
### 1. 状态（State）
- **定义**：抽象状态类，声明所有具体状态的共同接口
- **职责**：定义一个或多个行为方法，这些方法将由具体状态类实现
- **特点**：通常使用抽象类或接口实现

### 2. 上下文（Context）
- **定义**：维护当前状态的对象
- **职责**：
  - 保存当前状态对象的引用
  - 将状态相关的操作委托给当前状态对象
  - 提供状态切换的接口
- **特点**：对外提供简单的接口，隐藏内部状态管理的复杂性

### 3. 具体状态（Concrete State）
- **定义**：实现特定状态下的具体行为
- **职责**：
  - 实现状态特定的行为
  - 定义状态转换规则
  - 访问上下文的数据

## 模式结构
### 类图关系
```
┌───────────────┐       ┌───────────────┐
│    Context    │◆─────>│     State     │
└───────────────┘       └───────────────┘
       △                       △
       │                       │
       │                ┌──────┴──────┐
       │                │             │
┌──────┴───────┐ ┌─────┴────┐ ┌──────┴────┐
│ ConcreteCtx  │ │  StateA  │ │  StateB   │
└──────────────┘ └──────────┘ └───────────┘
```

### 代码结构
```python
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context) -> None:
        """定义状态下的行为"""
        pass

    @abstractmethod
    def can_handle(self, event: str) -> bool:
        """检查是否可以处理特定事件"""
        pass

class Context:
    def __init__(self, initial_state: State):
        self._state = initial_state
        self._data = {}  # 上下文数据

    def change_state(self, new_state: State):
        self._state = new_state

    def handle_event(self, event: str):
        if self._state.can_handle(event):
            self._state.handle(self)
```

## 设计考虑
### 1. 状态转换方式
#### 内部转换
```python
class ConcreteStateA(State):
    def handle(self, context):
        # 处理逻辑
        context.change_state(ConcreteStateB())
```

#### 外部转换
```python
class Context:
    def request(self):
        self._state.handle(self)
        if self._should_change_state():
            self.change_state(self._next_state())
```

### 2. 状态数据管理
#### 方案一：数据在上下文
```python
class Context:
    def __init__(self):
        self._state = InitialState()
        self._data = {}  # 共享数据

class ConcreteState(State):
    def handle(self, context):
        # 通过上下文访问数据
        data = context._data
```

#### 方案二：数据在状态
```python
class State:
    def __init__(self):
        self._state_data = {}

    def handle(self, context):
        # 使用状态特定的数据
        self._state_data['count'] += 1
```

## 常见问题
### 1. 状态爆炸
**问题**：状态类数量急剧增加
**解决方案**：
- 使用组合状态
- 状态复用
- 状态机框架

### 2. 状态转换复杂性
**问题**：状态转换逻辑难以管理
**解决方案**：
```python
class StateManager:
    def __init__(self):
        self._transitions = {
            ('StateA', 'event1'): StateB,
            ('StateB', 'event2'): StateC,
        }

    def get_next_state(self, current_state, event):
        return self._transitions.get((current_state, event))
```

### 3. 性能优化
**问题**：频繁创建状态对象
**解决方案**：
```python
class StatePool:
    _states = {}

    @classmethod
    def get_state(cls, state_class):
        if state_class not in cls._states:
            cls._states[state_class] = state_class()
        return cls._states[state_class]
```

## 实践建议
1. **状态接口设计**
   - 保持状态接口简单明确
   - 考虑状态生命周期方法（进入/退出）
   - 提供状态查询方法

2. **状态转换管理**
   - 使用状态转换表或状态机
   - 记录状态转换历史
   - 实现状态转换验证

3. **测试策略**
   - 单元测试每个状态
   - 测试状态转换序列
   - 测试异常情况

4. **文档化**
   - 状态图
   - 转换条件
   - 状态职责

## 进阶主题
### 1. 分层状态机
```python
class CompositeState(State):
    def __init__(self):
        self._sub_states = []
        self._current_sub_state = None

    def add_sub_state(self, state):
        self._sub_states.append(state)
```

### 2. 状态观察者
```python
class StateObserver:
    def on_state_changed(self, old_state, new_state):
        pass

class ObservableContext(Context):
    def __init__(self):
        super().__init__()
        self._observers = []

    def change_state(self, new_state):
        old_state = self._state
        super().change_state(new_state)
        self._notify_observers(old_state, new_state)
```

## 示例应用场景
1. **工作流系统**
   - 文档状态管理
   - 审批流程控制
   - 任务状态跟踪

2. **游戏开发**
   - 角色状态管理
   - 游戏阶段控制
   - AI行为控制

3. **网络通信**
   - 连接状态管理
   - 协议状态机
   - 会话管理

## 相关资源
- [Python 状态机框架](https://github.com/pytransitions/transitions)
- [状态模式最佳实践](https://refactoring.guru/design-patterns/state)
- [状态机理论](https://en.wikipedia.org/wiki/Finite-state_machine)
