from abc import ABC, abstractmethod
from typing import List

# 抽象组件
class MenuComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def print_menu(self, indent=""):
        pass

# 叶子节点 - 菜品
class MenuItem(MenuComponent):
    def __init__(self, name: str, price: float, description: str):
        self._name = name
        self._price = price
        self._description = description

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def print_menu(self, indent=""):
        print(f"{indent}{self._name} - ¥{self._price}")
        print(f"{indent}  描述: {self._description}")

# 组合节点 - 菜单分类
class MenuCategory(MenuComponent):
    def __init__(self, name: str):
        self._name = name
        self._items: List[MenuComponent] = []

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return sum(item.get_price() for item in self._items)

    def add(self, component: MenuComponent):
        self._items.append(component)

    def remove(self, component: MenuComponent):
        self._items.remove(component)

    def print_menu(self, indent=""):
        print(f"\n{indent}=== {self._name} ===")
        for item in self._items:
            item.print_menu(indent + "  ")

# 使用示例
if __name__ == "__main__":
    # 创建菜品
    kung_pao_chicken = MenuItem("宫保鸡丁", 38.0, "经典川菜，口感麻辣鲜香")
    sweet_sour_pork = MenuItem("糖醋里脊", 42.0, "酸甜可口，外酥里嫩")
    mapo_tofu = MenuItem("麻婆豆腐", 32.0, "麻辣鲜香，豆腐嫩滑")
    fried_rice = MenuItem("扬州炒饭", 28.0, "色香味俱全，配料丰富")

    # 创建菜单分类
    main_dishes = MenuCategory("主菜")
    rice_dishes = MenuCategory("米饭类")
    restaurant_menu = MenuCategory("餐厅菜单")

    # 构建菜单结构
    main_dishes.add(kung_pao_chicken)
    main_dishes.add(sweet_sour_pork)
    main_dishes.add(mapo_tofu)
    rice_dishes.add(fried_rice)

    restaurant_menu.add(main_dishes)
    restaurant_menu.add(rice_dishes)

    # 打印完整菜单
    print("=== 今日菜单 ===")
    restaurant_menu.print_menu()
