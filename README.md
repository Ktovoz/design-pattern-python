<div align="center">

# Python 设计模式实现指南

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/设计模式-23种-orange.svg" alt="Design Patterns">
  <img src="https://img.shields.io/badge/状态-持续更新-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/文档-详尽-yellow.svg" alt="Documentation">
</p>

<p align="center"><em>Python 设计模式的最佳实践与实现</em></p>

---
</div>

## 目录

- [项目概述](#项目概述)
- [快速开始](#快速开始)
- [设计模式分类](#设计模式分类)
- [学习指南](#学习指南)
- [最佳实践](#最佳实践)
- [社区支持](#社区支持)
- [参考资料](#参考资料)

## 项目概述

本项目旨在通过 Python 实现经典的设计模式，为开发者提供深入理解设计模式原理和实践应用的参考。每个模式都配备完整的说明文档和示例代码，确保学习过程的系统性和实用性。

### 项目目标

身为 Python 学习者，我曾经遇到过这些困惑：
- 掌握了基础语法，但不知如何实践
- 理解了概念，却难以应用到实际项目
- 想要提升架构能力，不知从何着手

**设计模式**正是连接理论与实践的桥梁，它能帮助我们：
- 提升代码质量和复用性
- 优化系统架构设计
- 解决实际开发问题

### 项目特点

- **完整的模式实现**：涵盖所有 23 种经典设计模式
- **详细的代码注释**：每个示例都包含完整的注释说明
- **实用的应用场景**：结合实际开发场景的示例代码
- **渐进式学习**：从简单到复杂，循序渐进的学习路径
- **最佳实践指南**：包含模式选择和应用的建议

## 快速开始

### 环境要求

- Python 3.6+
- 基本的 Python 编程基础
- 面向对象编程概念的理解

### 使用方式

1. 克隆项目到本地：
```bash
git clone https://github.com/Ktovoz/design-pattern-python.git
cd design-pattern-python
```

2. 选择感兴趣的设计模式目录
3. 阅读 README.md 了解模式原理
4. 运行示例代码：
```bash
python example.py
```

## 设计模式分类

设计模式按照其功能和目的可分为三大类：

### 创建型模式 (Creational Patterns)

创建型模式关注对象的创建机制，提供灵活的对象创建方式。

| 模式名称 | 说明 |
|:--------|:-----|
| [工厂方法模式](创建型模式_creational/工厂方法模式_factory_method/README.md) | 定义创建对象的接口，让子类决定实例化哪个类 |
| [抽象工厂模式](创建型模式_creational/抽象工厂模式_abstract_factory/README.md) | 提供创建一系列相关或相互依赖对象的接口 |
| [建造者模式](创建型模式_creational/建造者模式_builder/README.md) | 将复杂对象的构建与表示分离 |
| [原型模式](创建型模式_creational/原型模式_prototype/README.md) | 通过复制现有对象来创建新对象 |
| [单例模式](创建型模式_creational/单例模式_singleton/README.md) | 确保一个类只有一个实例 |

### 结构型模式 (Structural Patterns)

结构型模式关注类和对象的组合方式，构建灵活的系统结构。

| 模式名称 | 说明 |
|:--------|:-----|
| [适配器模式](结构型模式_structural/适配器模式_adapter/README.md) | 将一个类的接口转换成客户希望的另一个接口 |
| [桥接模式](结构型模式_structural/桥接模式_bridge/README.md) | 将抽象部分与实现部分分离 |
| [组合模式](结构型模式_structural/组合模式_composite/README.md) | 将对象组合成树形结构表示"部分-整体"层次 |
| [装饰器模式](结构型模式_structural/装饰器模式_decorator/README.md) | 动态地给对象添加额外的职责 |
| [外观模式](结构型模式_structural/外观模式_facade/README.md) | 为子系统提供统一的接口 |
| [享元模式](结构型模式_structural/享元模式_flyweight/README.md) | 通过共享技术支持大量细粒度对象 |
| [代理模式](结构型模式_structural/代理模式_proxy/README.md) | 为其他对象提供代理控制访问 |

### 行为型模式 (Behavioral Patterns)

行为型模式关注对象之间的通信和职责分配。

| 模式名称 | 说明 |
|:--------|:-----|
| [责任链模式](行为型模式_behavioral/责任链模式_chain_of_responsibility/README.md) | 将请求的发送者和接收者解耦 |
| [命令模式](行为型模式_behavioral/命令模式_command/README.md) | 将请求封装成对象 |
| [迭代器模式](行为型模式_behavioral/迭代器模式_iterator/README.md) | 提供顺序访问聚合对象的方法 |
| [中介者模式](行为型模式_behavioral/中介者模式_mediator/README.md) | 封装对象间的交互 |
| [观察者模式](行为型模式_behavioral/观察者模式_observer/README.md) | 定义对象间的一对多依赖关系 |
| [状态模式](行为型模式_behavioral/状态模式_state/README.md) | 允许对象在内部状态改变时改变行为 |
| [策略模式](行为型模式_behavioral/策略模式_strategy/README.md) | 定义一系列算法并使其可相互替换 |
| [模板方法模式](行为型模式_behavioral/模板方法模式_template_method/README.md) | 定义算法骨架，延迟步骤到子类 |
| [访问者模式](行为型模式_behavioral/访问者模式_visitor/README.md) | 表示作用于对象结构中各元素的操作 |
| [解释器模式](行为型模式_behavioral/解释器模式_interpreter/README.md) | 定义语言的文法表示和解释器 |
| [备忘录模式](行为型模式_behavioral/备忘录模式_memento/README.md) | 捕获对象内部状态并在外部保存 |

## 学习指南

### 学习路径

1. **基础掌握**
   - 理解面向对象编程基础
   - 学习基本的设计模式概念
   - 掌握常用的创建型模式

2. **深入理解**
   - 学习结构型模式的应用
   - 理解模式之间的关联
   - 掌握设计原则（SOLID）

3. **实战应用**
   - 学习行为型模式
   - 进行实际项目练习
   - 掌握模式的选择和权衡

4. **高级主题**
   - 学习模式组合使用
   - 理解反模式
   - 掌握重构技巧

### 学习建议

1. **循序渐进**：建议按照以下顺序学习：
   - 创建型模式（单例、工厂方法）
   - 结构型模式（适配器、装饰器）
   - 行为型模式（观察者、策略）

2. **实践为主**：
   - 仔细阅读示例代码
   - 尝试修改和扩展示例
   - 在实际项目中应用

3. **深入理解**：
   - 理解每个模式的适用场景
   - 掌握模式之间的关联
   - 学会权衡和选择

## 最佳实践

### 使用场景

- 当遇到重复的设计问题时
- 需要提高代码可维护性时
- 需要优化系统架构时

### 避免使用的场景

- 简单问题不需要复杂解决方案
- 过度设计会导致代码复杂化
- 团队对模式理解不足时

### 模式选择指南

1. **创建型模式**：当需要控制对象创建过程时
2. **结构型模式**：当需要处理类或对象的组合时
3. **行为型模式**：当需要处理对象之间的交互时

## 社区支持

### 交流渠道

- GitHub Issues：问题反馈
- Discussions：技术讨论
- Pull Requests：代码贡献

### 获取帮助

1. 查看文档和示例
2. 搜索 Issues
3. 提交新的 Issue
4. 参与社区讨论

### 贡献指南

欢迎贡献代码或改进文档！请遵循以下步骤：

1. Fork 本仓库
2. 创建新的分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送到分支：`git push origin feature/your-feature`
5. 提交 Pull Request

#### 贡献规范

- 代码风格遵循 PEP 8 规范
- 确保所有示例代码可以正常运行
- 添加必要的注释和文档
- 保持代码简洁和可读性

## 参考资料

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
- [Python Design Patterns](https://python-patterns.guide/)
- [Refactoring Guru](https://refactoring.guru/design-patterns)

## 更新日志

### v1.0.0 (2025-05-07)
- 初始版本发布
- 实现所有 23 种设计模式
- 提供完整的示例代码
- 添加详细文档

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢

感谢所有为本项目做出贡献的开发者！

---

<div align="center">
  <sub>由 <a href="https://github.com/Ktovoz">Ktovoz</a> 开发维护</sub>
</div>
