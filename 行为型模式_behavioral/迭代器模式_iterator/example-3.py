from abc import ABC, abstractmethod
from typing import List, Optional, Callable
from dataclasses import dataclass
from datetime import datetime
import os

@dataclass
class FileItem:
    name: str
    path: str
    size: int
    is_directory: bool
    modified_time: datetime
    
    def __str__(self):
        type_str = "目录" if self.is_directory else "文件"
        size_str = f"{self.size / 1024:.1f}KB" if not self.is_directory else ""
        return f"{type_str}: {self.name} {size_str}"

# 迭代器接口
class FileSystemIterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Optional[FileItem]:
        pass
    
    @abstractmethod
    def reset(self):
        pass

# 具体迭代器
class RecursiveFileIterator(FileSystemIterator):
    def __init__(self, root_path: str, filter_func: Optional[Callable[[FileItem], bool]] = None):
        self.root_path = root_path
        self.filter_func = filter_func
        self.items: List[FileItem] = []
        self.current_index = -1
        self._collect_items(root_path)
    
    def _collect_items(self, path: str):
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                stats = os.stat(full_path)
                
                file_item = FileItem(
                    name=item,
                    path=full_path,
                    size=stats.st_size,
                    is_directory=os.path.isdir(full_path),
                    modified_time=datetime.fromtimestamp(stats.st_mtime)
                )
                
                if self.filter_func is None or self.filter_func(file_item):
                    self.items.append(file_item)
                
                if file_item.is_directory:
                    self._collect_items(full_path)
        except PermissionError:
            print(f"无法访问目录: {path}")
    
    def has_next(self) -> bool:
        return self.current_index < len(self.items) - 1
    
    def next(self) -> Optional[FileItem]:
        if self.has_next():
            self.current_index += 1
            return self.items[self.current_index]
        return None
    
    def reset(self):
        self.current_index = -1

# 文件系统类
class FileSystem:
    def __init__(self, root_path: str):
        self.root_path = root_path
    
    def iterator(self, filter_func: Optional[Callable[[FileItem], bool]] = None) -> FileSystemIterator:
        return RecursiveFileIterator(self.root_path, filter_func)

# 使用示例
if __name__ == "__main__":
    # 创建文件系统对象
    fs = FileSystem(".")
    
    # 定义过滤器：只显示Python文件
    def python_file_filter(item: FileItem) -> bool:
        return not item.is_directory and item.name.endswith('.py')
    
    # 使用迭代器遍历文件系统
    iterator = fs.iterator(python_file_filter)
    
    print("Python文件列表：")
    while iterator.has_next():
        item = iterator.next()
        print(f"- {item}")
    
    # 重置迭代器
    iterator.reset()
    
    # 再次遍历
    print("\n再次遍历Python文件列表：")
    while iterator.has_next():
        item = iterator.next()
        print(f"- {item}")
