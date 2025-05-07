from abc import ABC, abstractmethod
import time
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Product:
    id: str
    name: str
    price: float
    stock: int

@dataclass
class Order:
    id: str
    products: List[Product]
    total_amount: float
    status: str
    created_at: datetime

# 抽象主题
class ShoppingSystem(ABC):
    @abstractmethod
    def search_products(self, keyword: str) -> List[Product]:
        pass
    
    @abstractmethod
    def place_order(self, product_ids: List[str]) -> Order:
        pass
    
    @abstractmethod
    def get_order_status(self, order_id: str) -> str:
        pass

# 真实主题
class RealShoppingSystem(ShoppingSystem):
    def __init__(self):
        self._products: Dict[str, Product] = {
            "1": Product("1", "笔记本电脑", 5999.0, 10),
            "2": Product("2", "智能手机", 3999.0, 20),
            "3": Product("3", "无线耳机", 999.0, 50)
        }
        self._orders: Dict[str, Order] = {}
    
    def search_products(self, keyword: str) -> List[Product]:
        # 模拟网络延迟
        time.sleep(1)
        return [p for p in self._products.values() if keyword.lower() in p.name.lower()]
    
    def place_order(self, product_ids: List[str]) -> Order:
        # 模拟网络延迟
        time.sleep(2)
        
        products = []
        total_amount = 0
        
        for pid in product_ids:
            if pid in self._products and self._products[pid].stock > 0:
                product = self._products[pid]
                products.append(product)
                total_amount += product.price
                product.stock -= 1
        
        order = Order(
            id=f"ORD{len(self._orders) + 1}",
            products=products,
            total_amount=total_amount,
            status="已创建",
            created_at=datetime.now()
        )
        self._orders[order.id] = order
        return order
    
    def get_order_status(self, order_id: str) -> str:
        # 模拟网络延迟
        time.sleep(1)
        return self._orders.get(order_id, "订单不存在").status

# 代理
class ShoppingSystemProxy(ShoppingSystem):
    def __init__(self):
        self._real_system = RealShoppingSystem()
        self._cache: Dict[str, tuple] = {}  # 缓存搜索结果
        self._cache_timeout = timedelta(minutes=5)
    
    def search_products(self, keyword: str) -> List[Product]:
        # 检查缓存
        if keyword in self._cache:
            cached_time, cached_results = self._cache[keyword]
            if datetime.now() - cached_time < self._cache_timeout:
                print("从缓存返回搜索结果")
                return cached_results
        
        # 调用真实系统
        results = self._real_system.search_products(keyword)
        self._cache[keyword] = (datetime.now(), results)
        return results
    
    def place_order(self, product_ids: List[str]) -> Order:
        # 验证库存
        for pid in product_ids:
            if pid not in self._real_system._products:
                raise ValueError(f"商品 {pid} 不存在")
            if self._real_system._products[pid].stock <= 0:
                raise ValueError(f"商品 {pid} 库存不足")
        
        # 验证订单金额
        total = sum(self._real_system._products[pid].price for pid in product_ids)
        if total > 10000:
            raise ValueError("订单金额超过10000元，请分多次下单")
        
        return self._real_system.place_order(product_ids)
    
    def get_order_status(self, order_id: str) -> str:
        return self._real_system.get_order_status(order_id)

# 使用示例
if __name__ == "__main__":
    shopping = ShoppingSystemProxy()
    
    # 搜索商品
    print("搜索商品：")
    results = shopping.search_products("手机")
    for product in results:
        print(f"- {product.name}: ¥{product.price}")
    
    # 使用缓存搜索
    print("\n再次搜索相同商品：")
    results = shopping.search_products("手机")
    for product in results:
        print(f"- {product.name}: ¥{product.price}")
    
    # 下单
    print("\n尝试下单：")
    try:
        order = shopping.place_order(["2", "3"])
        print(f"订单创建成功：{order.id}")
        print(f"订单状态：{shopping.get_order_status(order.id)}")
    except ValueError as e:
        print(f"下单失败：{e}")
    
    # 尝试超额下单
    print("\n尝试超额下单：")
    try:
        order = shopping.place_order(["1", "1", "1"])
    except ValueError as e:
        print(f"下单失败：{e}")
