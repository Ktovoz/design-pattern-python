from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

# 抽象产品类 - 文档
class Document(ABC):
    def __init__(self):
        self.content: List[str] = []
        self.metadata: Dict = {
            "created_at": datetime.now(),
            "modified_at": datetime.now(),
            "version": 1.0
        }
    
    @abstractmethod
    def add_content(self, text: str) -> str:
        pass
    
    @abstractmethod
    def format_content(self) -> str:
        pass
    
    @abstractmethod
    def get_metadata(self) -> str:
        pass

# 具体产品类 - 文本文档
class TextDocument(Document):
    def add_content(self, text: str) -> str:
        self.content.append(text)
        self.metadata["modified_at"] = datetime.now()
        self.metadata["version"] += 0.1
        return f"添加文本内容: {text}"
    
    def format_content(self) -> str:
        return "\n".join(self.content)
    
    def get_metadata(self) -> str:
        return f"文本文档 - 创建时间: {self.metadata['created_at']}, 修改时间: {self.metadata['modified_at']}, 版本: {self.metadata['version']:.1f}"

# 具体产品类 - Markdown文档
class MarkdownDocument(Document):
    def add_content(self, text: str) -> str:
        self.content.append(text)
        self.metadata["modified_at"] = datetime.now()
        self.metadata["version"] += 0.1
        return f"添加Markdown内容: {text}"
    
    def format_content(self) -> str:
        return "\n\n".join(self.content)
    
    def get_metadata(self) -> str:
        return f"Markdown文档 - 创建时间: {self.metadata['created_at']}, 修改时间: {self.metadata['modified_at']}, 版本: {self.metadata['version']:.1f}"

# 具体产品类 - HTML文档
class HTMLDocument(Document):
    def add_content(self, text: str) -> str:
        self.content.append(text)
        self.metadata["modified_at"] = datetime.now()
        self.metadata["version"] += 0.1
        return f"添加HTML内容: {text}"
    
    def format_content(self) -> str:
        return f"<html><body>{''.join(self.content)}</body></html>"
    
    def get_metadata(self) -> str:
        return f"HTML文档 - 创建时间: {self.metadata['created_at']}, 修改时间: {self.metadata['modified_at']}, 版本: {self.metadata['version']:.1f}"

# 抽象创建者类
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass
    
    def create_and_edit_document(self, content: List[str]) -> str:
        document = self.create_document()
        results = []
        for text in content:
            results.append(document.add_content(text))
        return "\n".join(results)
    
    def get_formatted_document(self) -> str:
        document = self.create_document()
        return document.format_content()
    
    def get_document_info(self) -> str:
        document = self.create_document()
        return document.get_metadata()

# 具体创建者类 - 文本文档创建者
class TextDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return TextDocument()

# 具体创建者类 - Markdown文档创建者
class MarkdownDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return MarkdownDocument()

# 具体创建者类 - HTML文档创建者
class HTMLDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return HTMLDocument()

def main():
    # 创建不同类型的文档创建者
    text_creator = TextDocumentCreator()
    markdown_creator = MarkdownDocumentCreator()
    html_creator = HTMLDocumentCreator()

    # 测试文本文档
    print("=== 测试文本文档 ===")
    content = ["这是第一行", "这是第二行", "这是第三行"]
    print(text_creator.create_and_edit_document(content))
    print("\n文档内容:")
    print(text_creator.get_formatted_document())
    print("\n文档信息:")
    print(text_creator.get_document_info())

    # 测试Markdown文档
    print("\n=== 测试Markdown文档 ===")
    md_content = ["# 标题", "## 子标题", "- 列表项1", "- 列表项2"]
    print(markdown_creator.create_and_edit_document(md_content))
    print("\n文档内容:")
    print(markdown_creator.get_formatted_document())
    print("\n文档信息:")
    print(markdown_creator.get_document_info())

    # 测试HTML文档
    print("\n=== 测试HTML文档 ===")
    html_content = ["<h1>标题</h1>", "<p>段落内容</p>", "<ul><li>列表项</li></ul>"]
    print(html_creator.create_and_edit_document(html_content))
    print("\n文档内容:")
    print(html_creator.get_formatted_document())
    print("\n文档信息:")
    print(html_creator.get_document_info())

if __name__ == "__main__":
    main() 