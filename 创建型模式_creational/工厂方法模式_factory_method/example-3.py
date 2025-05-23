# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime
import json
import re

# 抽象产品类 - 文档
class Document(ABC):
    def __init__(self, title: str = "未命名文档"):
        self.title = title
        self.content: List[str] = []
        self.metadata: Dict = {
            "created_at": datetime.now(),
            "modified_at": datetime.now(),
            "version": 1.0,
            "author": "系统",
            "tags": [],
            "word_count": 0
        }
    
    @abstractmethod
    def add_content(self, text: str) -> str:
        pass
    
    @abstractmethod
    def format_content(self) -> str:
        pass
    
    @abstractmethod
    def export_content(self) -> str:
        pass
    
    def update_metadata(self):
        """更新文档元数据"""
        self.metadata["modified_at"] = datetime.now()
        self.metadata["version"] += 0.1
        # 计算字数
        total_words = sum(len(line.split()) for line in self.content)
        self.metadata["word_count"] = total_words
    
    def add_tag(self, tag: str) -> str:
        """添加标签"""
        if tag not in self.metadata["tags"]:
            self.metadata["tags"].append(tag)
            self.update_metadata()
            return f"添加标签: {tag}"
        return f"标签 '{tag}' 已存在"
    
    def search_content(self, keyword: str) -> List[str]:
        """搜索内容"""
        results = []
        for i, line in enumerate(self.content):
            if keyword.lower() in line.lower():
                results.append(f"第{i+1}行: {line}")
        return results
    
    def get_metadata(self) -> str:
        tags_str = ", ".join(self.metadata["tags"]) if self.metadata["tags"] else "无"
        return (f"文档标题: {self.title}\n"
                f"创建时间: {self.metadata['created_at'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"修改时间: {self.metadata['modified_at'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"版本: {self.metadata['version']:.1f}\n"
                f"作者: {self.metadata['author']}\n"
                f"标签: {tags_str}\n"
                f"字数: {self.metadata['word_count']}")

# 具体产品类 - 文本文档
class TextDocument(Document):
    def __init__(self, title: str = "文本文档"):
        super().__init__(title)
        self.metadata["type"] = "text"
    
    def add_content(self, text: str) -> str:
        self.content.append(text)
        self.update_metadata()
        return f"添加文本内容: {text}"
    
    def format_content(self) -> str:
        return "\n".join(self.content)
    
    def export_content(self) -> str:
        header = f"=== {self.title} ===\n"
        footer = f"\n--- 文档信息 ---\n字数: {self.metadata['word_count']}"
        return header + self.format_content() + footer

# 具体产品类 - Markdown文档
class MarkdownDocument(Document):
    def __init__(self, title: str = "Markdown文档"):
        super().__init__(title)
        self.metadata["type"] = "markdown"
        self.toc: List[str] = []  # 目录
    
    def add_content(self, text: str) -> str:
        self.content.append(text)
        self.update_metadata()
        self._update_toc(text)
        return f"添加Markdown内容: {text}"
    
    def _update_toc(self, text: str):
        """更新目录"""
        if text.startswith('#'):
            level = len(text) - len(text.lstrip('#'))
            title = text.lstrip('# ').strip()
            indent = "  " * (level - 1)
            self.toc.append(f"{indent}- {title}")
    
    def format_content(self) -> str:
        return "\n\n".join(self.content)
    
    def export_content(self) -> str:
        toc_section = ""
        if self.toc:
            toc_section = "## 目录\n" + "\n".join(self.toc) + "\n\n"
        
        return f"# {self.title}\n\n{toc_section}{self.format_content()}"
    
    def get_toc(self) -> str:
        """获取目录"""
        if not self.toc:
            return "暂无目录"
        return "目录:\n" + "\n".join(self.toc)

# 具体产品类 - HTML文档
class HTMLDocument(Document):
    def __init__(self, title: str = "HTML文档"):
        super().__init__(title)
        self.metadata["type"] = "html"
        self.css_styles: List[str] = []
    
    def add_content(self, text: str) -> str:
        self.content.append(text)
        self.update_metadata()
        return f"添加HTML内容: {text}"
    
    def add_css_style(self, css: str) -> str:
        """添加CSS样式"""
        self.css_styles.append(css)
        self.update_metadata()
        return f"添加CSS样式: {css}"
    
    def format_content(self) -> str:
        return "".join(self.content)
    
    def export_content(self) -> str:
        css_section = ""
        if self.css_styles:
            css_section = f"<style>\n{chr(10).join(self.css_styles)}\n</style>\n"
        
        return (f"<!DOCTYPE html>\n<html>\n<head>\n"
                f"<title>{self.title}</title>\n{css_section}</head>\n"
                f"<body>\n{self.format_content()}\n</body>\n</html>")

# 具体产品类 - JSON文档
class JSONDocument(Document):
    def __init__(self, title: str = "JSON文档"):
        super().__init__(title)
        self.metadata["type"] = "json"
        self.data: Dict = {}
    
    def add_content(self, text: str) -> str:
        """对于JSON文档，text应该是key:value格式"""
        try:
            if ':' in text:
                key, value = text.split(':', 1)
                key = key.strip()
                value = value.strip()
                # 尝试解析为JSON值
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    # 如果不是有效的JSON，就作为字符串处理
                    pass
                self.data[key] = value
                self.content.append(f'"{key}": {json.dumps(value, ensure_ascii=False)}')
            else:
                # 如果不是key:value格式，作为注释添加
                self.content.append(f'// {text}')
            
            self.update_metadata()
            return f"添加JSON内容: {text}"
        except Exception as e:
            return f"添加内容失败: {str(e)}"
    
    def format_content(self) -> str:
        return json.dumps(self.data, ensure_ascii=False, indent=2)
    
    def export_content(self) -> str:
        return self.format_content()
    
    def get_value(self, key: str) -> Optional[any]:
        """获取指定键的值"""
        return self.data.get(key)

# 抽象创建者类
class DocumentCreator(ABC):
    def __init__(self):
        self._documents: List[Document] = []
    
    @abstractmethod
    def create_document(self, title: str = None) -> Document:
        pass
    
    def create_and_edit_document(self, title: str, content: List[str]) -> str:
        document = self.create_document(title)
        self._documents.append(document)
        results = []
        for text in content:
            results.append(document.add_content(text))
        return "\n".join(results)
    
    def get_formatted_document(self, index: int = -1) -> str:
        if not self._documents:
            return "没有可用的文档"
        document = self._documents[index]
        return document.format_content()
    
    def export_document(self, index: int = -1) -> str:
        if not self._documents:
            return "没有可用的文档"
        document = self._documents[index]
        return document.export_content()
    
    def get_document_info(self, index: int = -1) -> str:
        if not self._documents:
            return "没有可用的文档"
        document = self._documents[index]
        return document.get_metadata()
    
    def list_documents(self) -> str:
        if not self._documents:
            return "没有创建任何文档"
        
        result = "文档列表:\n"
        for i, doc in enumerate(self._documents):
            result += f"{i+1}. {doc.title} ({doc.metadata['type']})\n"
        return result

# 具体创建者类 - 文本文档创建者
class TextDocumentCreator(DocumentCreator):
    def create_document(self, title: str = None) -> Document:
        return TextDocument(title or "新建文本文档")

# 具体创建者类 - Markdown文档创建者
class MarkdownDocumentCreator(DocumentCreator):
    def create_document(self, title: str = None) -> Document:
        return MarkdownDocument(title or "新建Markdown文档")

# 具体创建者类 - HTML文档创建者
class HTMLDocumentCreator(DocumentCreator):
    def create_document(self, title: str = None) -> Document:
        return HTMLDocument(title or "新建HTML文档")

# 具体创建者类 - JSON文档创建者
class JSONDocumentCreator(DocumentCreator):
    def create_document(self, title: str = None) -> Document:
        return JSONDocument(title or "新建JSON文档")

def main():
    # 创建不同类型的文档创建者
    text_creator = TextDocumentCreator()
    markdown_creator = MarkdownDocumentCreator()
    html_creator = HTMLDocumentCreator()
    json_creator = JSONDocumentCreator()

    # 测试文本文档
    print("=== 测试文本文档 ===")
    content = ["这是第一行内容", "这是第二行内容", "这是第三行内容"]
    print(text_creator.create_and_edit_document("我的文本文档", content))
    doc = text_creator._documents[-1]
    print(doc.add_tag("重要"))
    print(doc.add_tag("工作"))
    print("\n导出内容:")
    print(text_creator.export_document())

    # 测试Markdown文档
    print("\n=== 测试Markdown文档 ===")
    md_content = ["# 主标题", "## 子标题1", "这是一些内容", "## 子标题2", "- 列表项1", "- 列表项2"]
    print(markdown_creator.create_and_edit_document("技术文档", md_content))
    md_doc = markdown_creator._documents[-1]
    print(md_doc.get_toc())
    print("\n导出内容:")
    print(markdown_creator.export_document())

    # 测试HTML文档
    print("\n=== 测试HTML文档 ===")
    html_content = ["<h1>欢迎页面</h1>", "<p>这是一个段落</p>", "<ul><li>列表项</li></ul>"]
    print(html_creator.create_and_edit_document("网页文档", html_content))
    html_doc = html_creator._documents[-1]
    print(html_doc.add_css_style("body { font-family: Arial; }"))
    print(html_doc.add_css_style("h1 { color: blue; }"))
    print("\n导出内容:")
    print(html_creator.export_document())

    # 测试JSON文档
    print("\n=== 测试JSON文档 ===")
    json_content = ['name: "张三"', 'age: 30', 'skills: ["Python", "Java"]', 'active: true']
    print(json_creator.create_and_edit_document("用户配置", json_content))
    json_doc = json_creator._documents[-1]
    print(f"获取name值: {json_doc.get_value('name')}")
    print("\n导出内容:")
    print(json_creator.export_document())

    # 显示所有创建者的文档列表
    print("\n=== 文档管理 ===")
    print("文本文档创建者:")
    print(text_creator.list_documents())
    print("Markdown文档创建者:")
    print(markdown_creator.list_documents())

if __name__ == "__main__":
    main() 