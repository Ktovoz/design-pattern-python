class SolarSystem:
    # 类变量用于存储唯一实例
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.name = "太阳系"
            self.star = "太阳"
            self.planets = [
                "水星", "金星", "地球", "火星",
                "木星", "土星", "天王星", "海王星"
            ]
            self.age = "约46亿年"
    
    def get_info(self):
        return f"这是{self.name}，中心恒星是{self.star}，年龄{self.age}，包含{len(self.planets)}颗行星。"
    
    def list_planets(self):
        return f"行星列表：{', '.join(self.planets)}"

def main():
    # 创建太阳系实例
    solar_system1 = SolarSystem()
    print("创建第一个太阳系实例:")
    print(solar_system1.get_info())
    print(solar_system1.list_planets())
    
    # 尝试创建第二个太阳系实例
    solar_system2 = SolarSystem()
    print("\n尝试创建第二个太阳系实例:")
    print(solar_system2.get_info())
    print(solar_system2.list_planets())
    
    # 验证两个实例是否相同
    print("\n验证两个实例是否是同一个对象:")
    print(f"solar_system1 的内存地址: {id(solar_system1)}")
    print(f"solar_system2 的内存地址: {id(solar_system2)}")
    print(f"solar_system1 和 solar_system2 是否是同一个对象: {solar_system1 is solar_system2}")
    
    # 修改其中一个实例的属性
    print("\n修改其中一个实例的属性:")
    solar_system1.planets.append("冥王星")
    print(f"solar_system1 的行星列表: {solar_system1.list_planets()}")
    print(f"solar_system2 的行星列表: {solar_system2.list_planets()}")

if __name__ == "__main__":
    main() 