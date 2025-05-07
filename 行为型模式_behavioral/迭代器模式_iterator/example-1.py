from abc import ABC, abstractmethod

# 迭代器接口
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self):
        pass

# 具体迭代器
class BookShelfIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.index = 0
    
    def has_next(self) -> bool:
        return self.index < len(self.books)
    
    def next(self):
        if self.has_next():
            book = self.books[self.index]
            self.index += 1
            return book
        return None

# 聚合接口
class Aggregate(ABC):
    @abstractmethod
    def iterator(self) -> Iterator:
        pass

# 具体聚合类
class BookShelf(Aggregate):
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def iterator(self) -> Iterator:
        return BookShelfIterator(self.books)

# 使用示例
if __name__ == "__main__":
    # 创建书架
    bookshelf = BookShelf()
    
    # 添加书籍
    bookshelf.add_book("《三体》")
    bookshelf.add_book("《活着》")
    bookshelf.add_book("《百年孤独》")
    
    # 使用迭代器遍历书架
    iterator = bookshelf.iterator()
    while iterator.has_next():
        book = iterator.next()
        print(f"正在阅读: {book}")
