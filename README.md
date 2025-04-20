<div align="center">

# 🎯 Python设计模式实现指南

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/设计模式-23种-orange.svg" alt="Design Patterns">
  <img src="https://img.shields.io/badge/状态-持续更新-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/文档-详尽-yellow.svg" alt="Documentation">
</p>

<p align="center">💫 <em>「用Python演绎设计模式的艺术」</em> 💫</p>

---
</div>

## 🌟 项目介绍

> 本项目致力于通过 Python 实现经典的设计模式，帮助开发者深入理解设计模式的精髓和实践应用。每个模式都配备详尽的说明文档和示例代码，让学习过程更加轻松愉快。

### 💡 学习动机

身为 Python 学习者，我曾经遇到过这些困惑：

- 🎯 掌握了基础语法，但不知如何实践
- 🤔 理解了概念，却难以应用到实际项目
- 📚 想要提升架构能力，不知从何着手

**设计模式**正是连接理论与实践的桥梁，它能帮助我们：
- 🚀 提升代码质量和复用性
- 🎨 优化系统架构设计
- 🔧 解决实际开发问题

---

## 📊 项目概览

<div align="center">

| 模式类型     | 数量   | 描述                 | 图标 |
|:------------:|:------:|:---------------------|:----:|
| 创建型模式   | 5个    | 关注对象的创建过程   | 🏗️  |
| 结构型模式   | 7个    | 关注类和对象的组合   | 🔨   |
| 行为型模式   | 11个   | 关注对象间的交互     | ⚡   |
| **总计**     | **23个** | 完整的设计模式体系 | 🌟   |

</div>

---

## 🎨 设计模式分类

> 按照功能和目的，设计模式可分为三大类：

---

### 🏗️ 创建型模式 (Creational Patterns)

> 这些模式提供了创建对象的机制，能够提升已有代码的灵活性和可复用性。

<table>
<thead>
<tr><th>模式名称</th><th>说明</th></tr>
</thead>
<tbody>
<tr><td><a href="创建型模式_creational/工厂方法模式_factory_method/README.md">工厂方法模式（Factory Method）</a></td><td>定义创建对象的接口，让子类决定实例化哪个类</td></tr>
<tr><td><a href="创建型模式_creational/抽象工厂模式_abstract_factory/README.md">抽象工厂模式（Abstract Factory）</a></td><td>提供创建一系列相关或相互依赖对象的接口，无需指定具体类</td></tr>
<tr><td><a href="创建型模式_creational/建造者模式_builder/README.md">建造者模式（Builder）</a></td><td>将复杂对象的构建与表示分离，使相同的构建过程可以创建不同的表示</td></tr>
<tr><td><a href="创建型模式_creational/原型模式_prototype/README.md">原型模式（Prototype）</a></td><td>通过复制现有对象来创建新对象，避免复杂的初始化过程</td></tr>
<tr><td><a href="创建型模式_creational/单例模式_singleton/README.md">单例模式（Singleton）</a></td><td>确保一个类只有一个实例，并提供全局访问点</td></tr>
</tbody>
</table>

---

### 🔨 结构型模式 (Structural Patterns)

> 这些模式解释如何将对象和类组装成更大的结构，同时保持结构的灵活和高效。

<table>
<thead>
<tr><th>模式名称</th><th>说明</th></tr>
</thead>
<tbody>
<tr><td><a href="结构型模式_structural/适配器模式_adapter/README.md">适配器模式（Adapter）</a></td><td>将一个类的接口转换成客户希望的另一个接口</td></tr>
<tr><td><a href="结构型模式_structural/桥接模式_bridge/README.md">桥接模式（Bridge）</a></td><td>将抽象部分与实现部分分离，使它们可以独立变化</td></tr>
<tr><td><a href="结构型模式_structural/组合模式_composite/README.md">组合模式（Composite）</a></td><td>将对象组合成树形结构以表示"部分-整体"的层次结构</td></tr>
<tr><td><a href="结构型模式_structural/装饰器模式_decorator/README.md">装饰器模式（Decorator）</a></td><td>动态地给一个对象添加一些额外的职责</td></tr>
<tr><td><a href="结构型模式_structural/外观模式_facade/README.md">外观模式（Facade）</a></td><td>为子系统中的一组接口提供一个统一的接口</td></tr>
<tr><td><a href="结构型模式_structural/享元模式_flyweight/README.md">享元模式（Flyweight）</a></td><td>通过共享技术来支持大量细粒度的对象</td></tr>
<tr><td><a href="结构型模式_structural/代理模式_proxy/README.md">代理模式（Proxy）</a></td><td>为其他对象提供一个代理以控制对这个对象的访问</td></tr>
</tbody>
</table>

---

### ⚡ 行为型模式 (Behavioral Patterns)

> 这些模式关注对象之间的通信，处理对象之间的交互和职责分配。

<table>
<thead>
<tr><th>模式名称</th><th>说明</th></tr>
</thead>
<tbody>
<tr><td><a href="行为型模式_behavioral/责任链模式_chain_of_responsibility/README.md">责任链模式（Chain of Responsibility）</a></td><td>将请求的发送者和接收者解耦，让多个对象都有机会处理请求</td></tr>
<tr><td><a href="行为型模式_behavioral/命令模式_command/README.md">命令模式（Command）</a></td><td>将请求封装成对象，从而可用不同的请求对客户进行参数化</td></tr>
<tr><td><a href="行为型模式_behavioral/迭代器模式_iterator/README.md">迭代器模式（Iterator）</a></td><td>提供一种方法顺序访问一个聚合对象中的各个元素，而不暴露其内部表示</td></tr>
<tr><td><a href="行为型模式_behavioral/中介者模式_mediator/README.md">中介者模式（Mediator）</a></td><td>用一个中介对象来封装一系列的对象交互</td></tr>
<tr><td><a href="行为型模式_behavioral/观察者模式_observer/README.md">观察者模式（Observer）</a></td><td>定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都会得到通知</td></tr>
<tr><td><a href="行为型模式_behavioral/状态模式_state/README.md">状态模式（State）</a></td><td>允许对象在内部状态改变时改变它的行为</td></tr>
<tr><td><a href="行为型模式_behavioral/策略模式_strategy/README.md">策略模式（Strategy）</a></td><td>定义一系列算法，把它们一个个封装起来，并且使它们可以相互替换</td></tr>
<tr><td><a href="行为型模式_behavioral/模板方法模式_template_method/README.md">模板方法模式（Template Method）</a></td><td>定义一个操作中的算法骨架，而将一些步骤延迟到子类中</td></tr>
<tr><td><a href="行为型模式_behavioral/访问者模式_visitor/README.md">访问者模式（Visitor）</a></td><td>表示一个作用于某对象结构中的各元素的操作</td></tr>
<tr><td><a href="行为型模式_behavioral/解释器模式_interpreter/README.md">解释器模式（Interpreter）</a></td><td>给定一个语言，定义它的文法的一种表示，并定义一个解释器</td></tr>
<tr><td><a href="行为型模式_behavioral/备忘录模式_memento/README.md">备忘录模式（Memento）</a></td><td>在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态</td></tr>
</tbody>
</table>

---

<div align="center">
  <sub>由 <a href="https://github.com/Ktovoz">Ktovoz</a> 倾情打造 · 欢迎 Star & Fork</sub>
</div>
