from abc import ABC, abstractmethod

# 支付策略接口
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 具体策略：现金支付
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"使用现金支付: {amount}元")

# 具体策略：信用卡支付
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"使用信用卡支付: {amount}元")

# 具体策略：支付宝支付
class AlipayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"使用支付宝支付: {amount}元")

# 上下文类
class ShoppingCart:
    def __init__(self):
        self._payment_strategy = None
        self.items = []

    def set_payment_strategy(self, strategy):
        self._payment_strategy = strategy

    def add_item(self, item, price):
        self.items.append((item, price))

    def checkout(self):
        total = sum(price for _, price in self.items)
        if self._payment_strategy:
            self._payment_strategy.pay(total)
        else:
            print("请选择支付方式")

# 使用示例
if __name__ == "__main__":
    # 创建购物车
    cart = ShoppingCart()
    
    # 添加商品
    cart.add_item("苹果", 5)
    cart.add_item("香蕉", 3)
    cart.add_item("橙子", 4)
    
    # 使用不同的支付方式
    print("=== 使用现金支付 ===")
    cart.set_payment_strategy(CashPayment())
    cart.checkout()
    
    print("\n=== 使用信用卡支付 ===")
    cart.set_payment_strategy(CreditCardPayment())
    cart.checkout()
    
    print("\n=== 使用支付宝支付 ===")
    cart.set_payment_strategy(AlipayPayment())
    cart.checkout()
