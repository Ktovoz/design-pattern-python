from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# 访问者接口
class LibraryVisitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass
    
    @abstractmethod
    def visit_magazine(self, magazine):
        pass
    
    @abstractmethod
    def visit_dvd(self, dvd):
        pass

# 具体访问者 - 借阅检查器
class BorrowingChecker(LibraryVisitor):
    def visit_book(self, book):
        if book.is_available:
            return f"《{book.title}》可以借阅，借阅期限为30天"
        return f"《{book.title}》已被借出，预计归还日期：{book.return_date}"

    def visit_magazine(self, magazine):
        if magazine.is_available:
            return f"《{magazine.title}》可以借阅，借阅期限为7天"
        return f"《{magazine.title}》已被借出，预计归还日期：{magazine.return_date}"

    def visit_dvd(self, dvd):
        if dvd.is_available:
            return f"《{dvd.title}》可以借阅，借阅期限为14天"
        return f"《{dvd.title}》已被借出，预计归还日期：{dvd.return_date}"

# 具体访问者 - 库存统计器
class InventoryCounter(LibraryVisitor):
    def __init__(self):
        self.total_items = 0
        self.available_items = 0

    def visit_book(self, book):
        self.total_items += 1
        if book.is_available:
            self.available_items += 1

    def visit_magazine(self, magazine):
        self.total_items += 1
        if magazine.is_available:
            self.available_items += 1

    def visit_dvd(self, dvd):
        self.total_items += 1
        if dvd.is_available:
            self.available_items += 1

    def get_report(self):
        return f"总馆藏：{self.total_items}件，可借：{self.available_items}件"

# 图书馆物品接口
class LibraryItem(ABC):
    def __init__(self, title, is_available=True):
        self.title = title
        self.is_available = is_available
        self.return_date = None

    @abstractmethod
    def accept(self, visitor):
        pass

    def borrow(self):
        if self.is_available:
            self.is_available = False
            self.return_date = datetime.now() + timedelta(days=30)
            return True
        return False

# 具体物品类
class Book(LibraryItem):
    def accept(self, visitor):
        return visitor.visit_book(self)

class Magazine(LibraryItem):
    def accept(self, visitor):
        return visitor.visit_magazine(self)

class DVD(LibraryItem):
    def accept(self, visitor):
        return visitor.visit_dvd(self)

# 使用示例
if __name__ == "__main__":
    # 创建图书馆物品
    book = Book("Python编程")
    magazine = Magazine("科学美国人")
    dvd = DVD("Python教程视频")
    
    # 借出一些物品
    book.borrow()
    
    # 创建访问者
    borrowing_checker = BorrowingChecker()
    inventory_counter = InventoryCounter()
    
    # 检查借阅状态
    print("借阅状态检查：")
    print(book.accept(borrowing_checker))
    print(magazine.accept(borrowing_checker))
    print(dvd.accept(borrowing_checker))
    
    # 统计库存
    print("\n库存统计：")
    for item in [book, magazine, dvd]:
        item.accept(inventory_counter)
    print(inventory_counter.get_report())
