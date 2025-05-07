from abc import ABC, abstractmethod

# 抽象组件
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=""):
        pass

# 叶子节点 - 文件
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=""):
        print(f"{indent}文件: {self.name}")

# 组合节点 - 文件夹
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, indent=""):
        print(f"{indent}文件夹: {self.name}")
        for child in self.children:
            child.display(indent + "  ")

# 使用示例
if __name__ == "__main__":
    # 创建文件
    file1 = File("文档.txt")
    file2 = File("图片.jpg")
    file3 = File("音乐.mp3")

    # 创建文件夹
    root = Folder("根目录")
    documents = Folder("文档")
    media = Folder("媒体")

    # 构建树形结构
    root.add(documents)
    root.add(media)
    documents.add(file1)
    media.add(file2)
    media.add(file3)

    # 显示整个结构
    print("文件系统结构：")
    root.display()
