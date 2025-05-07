from abc import ABC, abstractmethod
from typing import Dict

# 抽象状态类
class VendingMachineState(ABC):
    @abstractmethod
    def insert_money(self, machine, amount: float) -> None:
        pass
    
    @abstractmethod
    def select_product(self, machine, product: str) -> None:
        pass
    
    @abstractmethod
    def dispense_product(self, machine) -> None:
        pass
    
    @abstractmethod
    def get_state_name(self) -> str:
        pass

# 待机状态
class IdleState(VendingMachineState):
    def insert_money(self, machine, amount: float) -> None:
        machine.add_money(amount)
        machine.set_state(HasMoneyState())
        print(f"投入金额：¥{amount}")
    
    def select_product(self, machine, product: str) -> None:
        print("请先投币")
    
    def dispense_product(self, machine) -> None:
        print("请先投币并选择商品")
    
    def get_state_name(self) -> str:
        return "待机状态"

# 已投币状态
class HasMoneyState(VendingMachineState):
    def insert_money(self, machine, amount: float) -> None:
        machine.add_money(amount)
        print(f"追加金额：¥{amount}")
    
    def select_product(self, machine, product: str) -> None:
        if product not in machine.products:
            print("商品不存在")
            return
        
        if machine.products[product]["price"] > machine.current_money:
            print("余额不足")
            return
        
        machine.selected_product = product
        machine.set_state(ProductSelectedState())
        print(f"已选择商品：{product}")
    
    def dispense_product(self, machine) -> None:
        print("请先选择商品")
    
    def get_state_name(self) -> str:
        return "已投币状态"

# 已选择商品状态
class ProductSelectedState(VendingMachineState):
    def insert_money(self, machine, amount: float) -> None:
        machine.add_money(amount)
        print(f"追加金额：¥{amount}")
    
    def select_product(self, machine, product: str) -> None:
        machine.selected_product = product
        print(f"更改商品选择为：{product}")
    
    def dispense_product(self, machine) -> None:
        product = machine.selected_product
        price = machine.products[product]["price"]
        if machine.products[product]["quantity"] > 0:
            machine.products[product]["quantity"] -= 1
            machine.current_money -= price
            print(f"出货：{product}")
            print(f"找零：¥{machine.current_money}")
            machine.current_money = 0
            machine.selected_product = None
            machine.set_state(IdleState())
        else:
            print("商品库存不足")
            machine.set_state(HasMoneyState())
    
    def get_state_name(self) -> str:
        return "已选择商品状态"

# 自动售货机
class VendingMachine:
    def __init__(self):
        self._state = IdleState()
        self.current_money = 0
        self.selected_product = None
        self.products: Dict[str, Dict] = {
            "可乐": {"price": 3.5, "quantity": 10},
            "矿泉水": {"price": 2.0, "quantity": 10},
            "咖啡": {"price": 10.0, "quantity": 5}
        }
    
    def set_state(self, state: VendingMachineState) -> None:
        self._state = state
    
    def get_state(self) -> str:
        return self._state.get_state_name()
    
    def add_money(self, amount: float) -> None:
        self.current_money += amount
    
    def insert_money(self, amount: float) -> None:
        self._state.insert_money(self, amount)
    
    def select_product(self, product: str) -> None:
        self._state.select_product(self, product)
    
    def dispense_product(self) -> None:
        self._state.dispense_product(self)

# 客户端代码
if __name__ == "__main__":
    # 创建售货机实例
    vm = VendingMachine()
    print(f"当前状态：{vm.get_state()}")
    
    # 测试购买流程
    vm.insert_money(5.0)
    print(f"当前状态：{vm.get_state()}")
    
    vm.select_product("可乐")
    print(f"当前状态：{vm.get_state()}")
    
    vm.dispense_product()
    print(f"当前状态：{vm.get_state()}")
    
    # 测试异常情况
    vm.select_product("可乐")  # 应该提示先投币
    vm.insert_money(2.0)
    vm.select_product("咖啡")  # 应该提示余额不足
