class SimpleSingleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.value = "这是一个简单的单例示例"

def main():
    # 创建实例
    singleton1 = SimpleSingleton()
    print("第一个实例:", singleton1.value)
    
    # 尝试创建第二个实例
    singleton2 = SimpleSingleton()
    print("第二个实例:", singleton2.value)
    
    # 验证是否是同一个对象
    print("\n验证是否是同一个对象:")
    print(f"singleton1 的内存地址: {id(singleton1)}")
    print(f"singleton2 的内存地址: {id(singleton2)}")
    print(f"singleton1 和 singleton2 是否是同一个对象: {singleton1 is singleton2}")

if __name__ == "__main__":
    main()
