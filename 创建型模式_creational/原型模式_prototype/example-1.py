from copy import deepcopy

class Stationery:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    def clone(self):
        return deepcopy(self)
    
    def __str__(self):
        return f"{self.name} - 颜色: {self.color}, 价格: {self.price}元"

# 使用示例
if __name__ == "__main__":
    # 创建一个铅笔原型
    pencil_prototype = Stationery("铅笔", "黑色", 2.5)
    
    # 克隆铅笔
    pencil1 = pencil_prototype.clone()
    pencil2 = pencil_prototype.clone()
    
    # 修改克隆对象的属性
    pencil1.color = "红色"
    pencil2.price = 3.0
    
    print("原始铅笔:", pencil_prototype)
    print("红色铅笔:", pencil1)
    print("高价铅笔:", pencil2)
