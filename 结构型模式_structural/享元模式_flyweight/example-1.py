from typing import Dict

class FontStyle:
    """字体样式享元类"""
    def __init__(self, font_family: str, size: int, is_bold: bool):
        self.font_family = font_family
        self.size = size
        self.is_bold = is_bold

    def __str__(self):
        return f"字体: {self.font_family}, 大小: {self.size}, 粗体: {self.is_bold}"

class FontStyleFactory:
    """字体样式工厂类"""
    _styles: Dict[str, FontStyle] = {}

    @classmethod
    def get_style(cls, font_family: str, size: int, is_bold: bool) -> FontStyle:
        key = f"{font_family}_{size}_{is_bold}"
        if key not in cls._styles:
            cls._styles[key] = FontStyle(font_family, size, is_bold)
        return cls._styles[key]

class Text:
    """文本类"""
    def __init__(self, content: str, font_style: FontStyle):
        self.content = content
        self.font_style = font_style

    def display(self):
        print(f"文本内容: {self.content}")
        print(f"样式: {self.font_style}")

def main():
    # 创建文本对象，共享字体样式
    text1 = Text("Hello World", FontStyleFactory.get_style("Arial", 12, True))
    text2 = Text("Python", FontStyleFactory.get_style("Arial", 12, True))
    text3 = Text("Design Pattern", FontStyleFactory.get_style("Times New Roman", 14, False))

    # 显示文本
    text1.display()
    print("-" * 30)
    text2.display()
    print("-" * 30)
    text3.display()

if __name__ == "__main__":
    main()
