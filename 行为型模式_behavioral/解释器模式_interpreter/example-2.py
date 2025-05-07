from abc import ABC, abstractmethod

# 抽象表达式
class ShoppingExpression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# 数量表达式
class QuantityExpression(ShoppingExpression):
    def __init__(self, quantity):
        self.quantity = int(quantity)
    
    def interpret(self):
        return self.quantity

# 价格表达式
class PriceExpression(ShoppingExpression):
    def __init__(self, price):
        self.price = float(price)
    
    def interpret(self):
        return self.price

# 商品表达式
class ItemExpression(ShoppingExpression):
    def __init__(self, quantity_expr, price_expr, item_name):
        self.quantity_expr = quantity_expr
        self.price_expr = price_expr
        self.item_name = item_name
    
    def interpret(self):
        return {
            'item': self.item_name,
            'quantity': self.quantity_expr.interpret(),
            'price': self.price_expr.interpret(),
            'total': self.quantity_expr.interpret() * self.price_expr.interpret()
        }

# 购物清单表达式
class ShoppingListExpression(ShoppingExpression):
    def __init__(self):
        self.items = []
    
    def add_item(self, item_expr):
        self.items.append(item_expr)
    
    def interpret(self):
        total = 0
        result = []
        for item in self.items:
            item_result = item.interpret()
            total += item_result['total']
            result.append(item_result)
        return {'items': result, 'grand_total': total}

# 购物清单解释器
class ShoppingListInterpreter:
    @staticmethod
    def parse_item(item_str):
        # 格式：商品名称 x 数量 @ 单价
        parts = item_str.split(' ')
        item_name = parts[0]
        quantity = parts[2]
        price = parts[4]
        
        quantity_expr = QuantityExpression(quantity)
        price_expr = PriceExpression(price)
        return ItemExpression(quantity_expr, price_expr, item_name)

def main():
    # 创建购物清单
    shopping_list = [
        "苹果 x 5 @ 2.5",
        "面包 x 2 @ 8.0",
        "牛奶 x 3 @ 6.5"
    ]
    
    # 创建解释器
    shopping_list_expr = ShoppingListExpression()
    
    # 解析每个商品
    for item in shopping_list:
        item_expr = ShoppingListInterpreter.parse_item(item)
        shopping_list_expr.add_item(item_expr)
    
    # 解释结果
    result = shopping_list_expr.interpret()
    
    # 打印结果
    print("购物清单:")
    for item in result['items']:
        print(f"{item['item']}: {item['quantity']}个 x ¥{item['price']} = ¥{item['total']}")
    print(f"总计: ¥{result['grand_total']}")

if __name__ == "__main__":
    main()
