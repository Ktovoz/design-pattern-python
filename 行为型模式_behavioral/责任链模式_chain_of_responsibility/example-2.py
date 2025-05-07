from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List

# 工单优先级
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

# 工单类型
class TicketType(Enum):
    TECHNICAL = auto()
    BILLING = auto()
    GENERAL = auto()

# 工单状态
class Status(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    RESOLVED = auto()
    ESCALATED = auto()

@dataclass
class ServiceTicket:
    id: int
    customer_name: str
    description: str
    priority: Priority
    ticket_type: TicketType
    status: Status = Status.OPEN
    resolution_notes: List[str] = None

    def __post_init__(self):
        if self.resolution_notes is None:
            self.resolution_notes = []

    def add_note(self, note: str):
        if self.resolution_notes is None:
            self.resolution_notes = []
        self.resolution_notes.append(note)

# 抽象处理者
class SupportHandler(ABC):
    def __init__(self, name: str):
        self.name = name
        self._next_handler: Optional[SupportHandler] = None

    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle_ticket(self, ticket: ServiceTicket) -> bool:
        pass

# 一线支持
class FirstLevelSupport(SupportHandler):
    def handle_ticket(self, ticket: ServiceTicket) -> bool:
        if ticket.priority in [Priority.LOW, Priority.MEDIUM] and \
           ticket.ticket_type in [TicketType.GENERAL]:
            ticket.status = Status.IN_PROGRESS
            ticket.add_note(f"{self.name} (一线支持) 正在处理此工单")
            # 模拟解决问题
            ticket.status = Status.RESOLVED
            ticket.add_note(f"{self.name} (一线支持) 已解决此工单")
            return True
        elif self._next_handler:
            ticket.add_note(f"{self.name} (一线支持) 将工单升级")
            return self._next_handler.handle_ticket(ticket)
        return False

# 技术支持
class TechnicalSupport(SupportHandler):
    def handle_ticket(self, ticket: ServiceTicket) -> bool:
        if ticket.ticket_type == TicketType.TECHNICAL and \
           ticket.priority != Priority.CRITICAL:
            ticket.status = Status.IN_PROGRESS
            ticket.add_note(f"{self.name} (技术支持) 正在处理此工单")
            # 模拟解决问题
            ticket.status = Status.RESOLVED
            ticket.add_note(f"{self.name} (技术支持) 已解决此工单")
            return True
        elif self._next_handler:
            ticket.add_note(f"{self.name} (技术支持) 将工单升级")
            return self._next_handler.handle_ticket(ticket)
        return False

# 高级技术支持
class SeniorTechnicalSupport(SupportHandler):
    def handle_ticket(self, ticket: ServiceTicket) -> bool:
        ticket.status = Status.IN_PROGRESS
        ticket.add_note(f"{self.name} (高级技术支持) 正在处理此工单")
        # 模拟解决问题
        ticket.status = Status.RESOLVED
        ticket.add_note(f"{self.name} (高级技术支持) 已解决此工单")
        return True

# 客户端代码
if __name__ == "__main__":
    # 创建支持团队
    first_level = FirstLevelSupport("小李")
    tech_support = TechnicalSupport("小王")
    senior_support = SeniorTechnicalSupport("张经理")

    # 设置责任链
    first_level.set_next(tech_support).set_next(senior_support)

    # 创建几个测试工单
    tickets = [
        ServiceTicket(1, "客户A", "无法登录网站", Priority.MEDIUM, TicketType.TECHNICAL),
        ServiceTicket(2, "客户B", "需要产品使用说明", Priority.LOW, TicketType.GENERAL),
        ServiceTicket(3, "客户C", "系统崩溃", Priority.CRITICAL, TicketType.TECHNICAL)
    ]

    # 处理工单
    for ticket in tickets:
        print(f"\n处理工单 #{ticket.id}:")
        first_level.handle_ticket(ticket)
        print(f"工单状态: {ticket.status}")
        print("处理记录:")
        for note in ticket.resolution_notes:
            print(f"- {note}")
