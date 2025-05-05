class Earth:
    # 类变量用于存储唯一实例
    _instance = None
    
    def __new__(cls):
        # 如果实例不存在，则创建一个新实例
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # 初始化一些基本属性
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        # 确保初始化代码只执行一次
        if not self._initialized:
            self._initialized = True
            self.name = "地球"
            self.population = "约78亿"
            self.continents = 7
            self.oceans = 5
    
    def get_info(self):
        return f"这是{self.name}，人口{self.population}，拥有{self.continents}大洲和{self.oceans}大洋。"

def main():
    # 创建地球实例
    earth1 = Earth()
    print("创建第一个地球实例:")
    print(earth1.get_info())
    
    # 尝试创建第二个地球实例
    earth2 = Earth()
    print("\n尝试创建第二个地球实例:")
    print(earth2.get_info())
    
    # 验证两个实例是否相同
    print("\n验证两个实例是否是同一个对象:")
    print(f"earth1 的内存地址: {id(earth1)}")
    print(f"earth2 的内存地址: {id(earth2)}")
    print(f"earth1 和 earth2 是否是同一个对象: {earth1 is earth2}")

if __name__ == "__main__":
    main()
