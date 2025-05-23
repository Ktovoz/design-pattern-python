import json
import os
from typing import Any, Dict
from functools import wraps
import threading

def singleton_decorator(cls):
    """单例装饰器"""
    instances = {}
    lock = threading.Lock()
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

class SingletonMeta(type):
    """单例元类"""
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class ConfigManager(metaclass=SingletonMeta):
    """配置管理器 - 使用元类实现单例"""
    
    def __init__(self, config_file: str = "config.json"):
        if hasattr(self, '_initialized'):
            return
        
        self._initialized = True
        self._config_file = config_file
        self._config: Dict[str, Any] = {}
        self._lock = threading.Lock()
        self._load_config()
    
    def _load_config(self):
        """从文件加载配置"""
        if os.path.exists(self._config_file):
            with open(self._config_file, 'r', encoding='utf-8') as f:
                self._config = json.load(f)
        else:
            self._config = {
                "app_name": "示例应用",
                "version": "1.0.0",
                "settings": {
                    "debug": True,
                    "max_connections": 100
                }
            }
            self._save_config()
    
    def _save_config(self):
        """保存配置到文件"""
        with open(self._config_file, 'w', encoding='utf-8') as f:
            json.dump(self._config, f, indent=4, ensure_ascii=False)
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """设置配置值"""
        with self._lock:
            self._config[key] = value
            self._save_config()
    
    def update(self, config_dict: Dict[str, Any]):
        """批量更新配置"""
        with self._lock:
            self._config.update(config_dict)
            self._save_config()
    
    def reset(self):
        """重置配置"""
        with self._lock:
            # 删除配置文件
            if os.path.exists(self._config_file):
                os.remove(self._config_file)
            # 重新加载默认配置
            self._load_config()

def main():
    # 创建配置管理器实例
    config1 = ConfigManager()
    config2 = ConfigManager()
    
    # 验证单例
    print("验证单例模式:")
    print(f"config1 的内存地址: {id(config1)}")
    print(f"config2 的内存地址: {id(config2)}")
    print(f"config1 和 config2 是否是同一个对象: {config1 is config2}")
    
    # 演示配置操作
    print("\n初始配置:")
    print(f"应用名称: {config1.get('app_name')}")
    print(f"设置: {config1.get('settings')}")
    
    # 更新配置
    config1.set("app_name", "新应用名称")
    config1.update({
        "settings": {
            "debug": False,
            "max_connections": 200
        }
    })
    
    print("\n更新后的配置:")
    print(f"应用名称: {config1.get('app_name')}")
    print(f"设置: {config1.get('settings')}")
    
    # 验证第二个实例也被更新
    print(f"config2的应用名称: {config2.get('app_name')}")
    
    # 重置配置
    config1.reset()
    print("\n重置后的配置:")
    print(f"应用名称: {config1.get('app_name')}")
    print(f"设置: {config1.get('settings')}")

if __name__ == "__main__":
    main() 