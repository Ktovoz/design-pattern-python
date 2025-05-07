from abc import ABC, abstractmethod
from typing import Dict, List
import time

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

class StockSubject:
    def __init__(self):
        self._observers: Dict[str, List['StockObserver']] = {}
        self._products: Dict[str, Product] = {}

    def add_product(self, product: Product):
        self._products[product.name] = product
        self._observers[product.name] = []

    def attach(self, product_name: str, observer: 'StockObserver'):
        if product_name in self._observers:
            self._observers[product_name].append(observer)

    def detach(self, product_name: str, observer: 'StockObserver'):
        if product_name in self._observers:
            self._observers[product_name].remove(observer)

    def notify(self, product_name: str):
        if product_name in self._observers:
            product = self._products[product_name]
            for observer in self._observers[product_name]:
                observer.update(product)

    def update_stock(self, product_name: str, new_stock: int):
        if product_name in self._products:
            self._products[product_name].stock = new_stock
            self.notify(product_name)

class StockObserver(ABC):
    @abstractmethod
    def update(self, product: Product):
        pass

class CustomerApp(StockObserver):
    def __init__(self, customer_name: str):
        self.customer_name = customer_name

    def update(self, product: Product):
        if product.stock > 0:
            print(f"尊敬的{self.customer_name}用户：您关注的商品 '{product.name}' 已经到货！当前库存：{product.stock}件")
        else:
            print(f"尊敬的{self.customer_name}用户：您关注的商品 '{product.name}' 已经售罄！")

class InventorySystem(StockObserver):
    def update(self, product: Product):
        if product.stock < 10:
            print(f"库存警告：商品 '{product.name}' 库存低于10件，当前库存：{product.stock}件")

class PriceAnalytics(StockObserver):
    def update(self, product: Product):
        if product.stock < 5:
            suggested_price = product.price * 1.1
            print(f"价格建议：由于 '{product.name}' 库存紧张（{product.stock}件），建议将价格提高到 {suggested_price:.2f}")

# 使用示例
if __name__ == "__main__":
    # 创建电商平台库存系统
    ecommerce = StockSubject()
    
    # 添加商品
    iphone = Product("iPhone 14", 6999.0, 20)
    ecommerce.add_product(iphone)
    
    # 创建观察者
    customer1 = CustomerApp("张三")
    customer2 = CustomerApp("李四")
    inventory_system = InventorySystem()
    price_analytics = PriceAnalytics()
    
    # 注册观察者
    ecommerce.attach(iphone.name, customer1)
    ecommerce.attach(iphone.name, customer2)
    ecommerce.attach(iphone.name, inventory_system)
    ecommerce.attach(iphone.name, price_analytics)
    
    # 模拟库存变化
    print("模拟库存变化情况：")
    for stock in [15, 8, 3, 0]:
        print(f"\n更新库存到 {stock} 件...")
        ecommerce.update_stock(iphone.name, stock)
        time.sleep(1)  # 稍微暂停以便观察输出
