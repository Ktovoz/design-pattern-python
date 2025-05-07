#!/usr/bin/env python
# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod

class Beverage(ABC):
    """饮料基类"""
    
    def make_beverage(self):
        """模板方法"""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
    
    def boil_water(self):
        print("将水煮沸")
    
    @abstractmethod
    def brew(self):
        """冲泡"""
        pass
    
    def pour_in_cup(self):
        print("倒入杯中")
    
    @abstractmethod
    def add_condiments(self):
        """加调料"""
        pass
    
    def customer_wants_condiments(self):
        """钩子方法"""
        return True

class Coffee(Beverage):
    """咖啡"""
    
    def brew(self):
        print("用沸水冲泡咖啡")
    
    def add_condiments(self):
        print("加入糖和牛奶")

class Tea(Beverage):
    """茶"""
    
    def brew(self):
        print("用沸水浸泡茶叶")
    
    def add_condiments(self):
        print("加入柠檬")
    
    def customer_wants_condiments(self):
        return False

def main():
    print("制作咖啡：")
    coffee = Coffee()
    coffee.make_beverage()
    
    print("\n制作茶：")
    tea = Tea()
    tea.make_beverage()

if __name__ == "__main__":
    main()
