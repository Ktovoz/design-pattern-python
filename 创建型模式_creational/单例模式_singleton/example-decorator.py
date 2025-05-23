import threading
from functools import wraps

def singleton_decorator(cls):
    """单例装饰器 - 确保类只有一个实例"""
    instances = {}
    lock = threading.Lock()
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                # 双重检查锁定
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton_decorator
class DatabaseConnection:
    """数据库连接类 - 使用装饰器实现单例"""
    
    def __init__(self, host="localhost", port=5432, database="mydb"):
        print(f"创建数据库连接: {host}:{port}/{database}")
        self.host = host
        self.port = port
        self.database = database
        self.is_connected = False
        self._connection_count = 0
    
    def connect(self):
        """连接数据库"""
        if not self.is_connected:
            print(f"连接到数据库 {self.host}:{self.port}/{self.database}")
            self.is_connected = True
            self._connection_count += 1
        else:
            print("数据库已经连接")
    
    def disconnect(self):
        """断开数据库连接"""
        if self.is_connected:
            print("断开数据库连接")
            self.is_connected = False
        else:
            print("数据库未连接")
    
    def execute_query(self, query):
        """执行查询"""
        if self.is_connected:
            print(f"执行查询: {query}")
            return f"查询结果: {query} 执行成功"
        else:
            print("请先连接数据库")
            return None
    
    def get_connection_info(self):
        """获取连接信息"""
        return {
            "host": self.host,
            "port": self.port,
            "database": self.database,
            "is_connected": self.is_connected,
            "connection_count": self._connection_count
        }

def main():
    print("=== 装饰器单例模式示例 ===\n")
    
    # 创建第一个数据库连接实例
    print("1. 创建第一个数据库连接实例:")
    db1 = DatabaseConnection()
    
    # 创建第二个数据库连接实例
    print("\n2. 创建第二个数据库连接实例:")
    db2 = DatabaseConnection("192.168.1.100", 3306, "testdb")
    
    # 验证是否是同一个实例
    print(f"\n3. 验证单例:")
    print(f"db1 的内存地址: {id(db1)}")
    print(f"db2 的内存地址: {id(db2)}")
    print(f"db1 和 db2 是否是同一个对象: {db1 is db2}")
    
    # 查看连接信息
    print(f"\n4. 连接信息:")
    print(f"db1 连接信息: {db1.get_connection_info()}")
    print(f"db2 连接信息: {db2.get_connection_info()}")
    
    # 使用数据库连接
    print(f"\n5. 使用数据库连接:")
    db1.connect()
    result = db1.execute_query("SELECT * FROM users")
    print(f"查询结果: {result}")
    
    # 通过db2也能看到连接状态
    print(f"\n6. 通过db2查看连接状态:")
    print(f"db2 连接状态: {db2.is_connected}")
    db2.execute_query("SELECT * FROM products")
    
    # 断开连接
    print(f"\n7. 断开连接:")
    db2.disconnect()
    print(f"db1 连接状态: {db1.is_connected}")

if __name__ == "__main__":
    main() 