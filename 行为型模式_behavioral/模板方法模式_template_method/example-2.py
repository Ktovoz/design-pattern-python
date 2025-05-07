#!/usr/bin/env python
# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod
from typing import List

class ClothesWashing(ABC):
    """衣物洗涤基类"""
    
    def wash_clothes(self, temperature: float, duration: int) -> None:
        """模板方法"""
        self.check_pockets()
        self.sort_by_color()
        self.pre_treat_stains()
        self.load_clothes()
        self.add_detergent()
        self.set_water_temperature(temperature)
        self.wash(duration)
        self.rinse()
        if self.needs_special_care():
            self.special_treatment()
        self.dry()
    
    def check_pockets(self) -> None:
        print("检查口袋是否有物品")
    
    @abstractmethod
    def sort_by_color(self) -> None:
        """按颜色分类"""
        pass
    
    @abstractmethod
    def pre_treat_stains(self) -> None:
        """预处理污渍"""
        pass
    
    def load_clothes(self) -> None:
        print("放入洗衣机")
    
    @abstractmethod
    def add_detergent(self) -> None:
        """添加洗涤剂"""
        pass
    
    def set_water_temperature(self, temperature: float) -> None:
        print(f"设置水温为 {temperature}°C")
    
    def wash(self, duration: int) -> None:
        print(f"开始洗涤，时长 {duration} 分钟")
    
    def rinse(self) -> None:
        print("清洗")
    
    @abstractmethod
    def needs_special_care(self) -> bool:
        """是否需要特殊护理"""
        pass
    
    @abstractmethod
    def special_treatment(self) -> None:
        """特殊护理处理"""
        pass
    
    @abstractmethod
    def dry(self) -> None:
        """干燥方式"""
        pass

class DelicateClothes(ClothesWashing):
    """精致衣物"""
    
    def sort_by_color(self) -> None:
        print("将精致衣物按浅色和深色分开")
    
    def pre_treat_stains(self) -> None:
        print("使用专业精致衣物去渍剂处理污渍")
    
    def add_detergent(self) -> None:
        print("添加温和洗涤剂")
    
    def needs_special_care(self) -> bool:
        return True
    
    def special_treatment(self) -> None:
        print("使用柔顺剂")
        print("轻柔揉搓")
    
    def dry(self) -> None:
        print("平铺晾干")

class RegularClothes(ClothesWashing):
    """普通衣物"""
    
    def sort_by_color(self) -> None:
        print("按深浅色分类")
    
    def pre_treat_stains(self) -> None:
        print("使用普通去渍剂处理污渍")
    
    def add_detergent(self) -> None:
        print("添加普通洗衣粉")
    
    def needs_special_care(self) -> bool:
        return False
    
    def special_treatment(self) -> None:
        pass
    
    def dry(self) -> None:
        print("使用烘干机烘干")

def main():
    print("洗涤精致衣物：")
    delicate = DelicateClothes()
    delicate.wash_clothes(temperature=30.0, duration=15)
    
    print("\n洗涤普通衣物：")
    regular = RegularClothes()
    regular.wash_clothes(temperature=40.0, duration=45)

if __name__ == "__main__":
    main()
