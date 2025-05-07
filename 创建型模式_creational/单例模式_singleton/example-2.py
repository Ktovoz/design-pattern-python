import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # 双重检查锁定模式
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            with self._lock:
                if not self._initialized:
                    self._initialized = True
                    self.counter = 0
                    self.data = {}
    
    def increment_counter(self):
        with self._lock:
            self.counter += 1
            return self.counter
    
    def add_data(self, key, value):
        with self._lock:
            self.data[key] = value
    
    def get_data(self):
        return self.data.copy()

def worker(singleton):
    # 模拟多线程操作
    for i in range(3):
        count = singleton.increment_counter()
        singleton.add_data(f"key_{count}", f"value_{count}")
        print(f"线程 {threading.current_thread().name} - 计数器: {count}")

def main():
    # 创建单例实例
    singleton = ThreadSafeSingleton()
    
    # 创建多个线程
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(singleton,))
        threads.append(t)
        t.start()
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    # 验证结果
    print("\n最终结果:")
    print(f"计数器最终值: {singleton.counter}")
    print(f"数据内容: {singleton.get_data()}")

if __name__ == "__main__":
    main() 