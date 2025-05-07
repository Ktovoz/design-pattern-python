"""
聊天室示例
展示了中等难度的中介者模式实现，包含多种消息类型和用户类型
"""

from abc import ABC, abstractmethod
from typing import Dict

class ChatRoom:
    def __init__(self):
        self._users: Dict[str, 'User'] = {}

    def register_user(self, user: 'User'):
        self._users[user.name] = user
        user.chat_room = self
        print(f"系统: {user.name} 加入了聊天室")

    def send_message(self, message: str, sender: 'User', to: str = None):
        if to:
            if to in self._users:
                self._users[to].receive_message(message, sender.name)
            else:
                sender.receive_system_message(f"用户 {to} 不存在")
        else:
            for user in self._users.values():
                if user != sender:
                    user.receive_message(message, sender.name)

    def send_emoji(self, emoji: str, sender: 'User'):
        print(f"\n{sender.name} 发送了表情: {emoji}")
        for user in self._users.values():
            if user != sender:
                user.receive_emoji(emoji, sender.name)

class User(ABC):
    def __init__(self, name: str):
        self.name = name
        self.chat_room = None

    def send_message(self, message: str, to: str = None):
        if self.chat_room:
            self.chat_room.send_message(message, self, to)

    def send_emoji(self, emoji: str):
        if self.chat_room:
            self.chat_room.send_emoji(emoji, self)

    @abstractmethod
    def receive_message(self, message: str, sender: str):
        pass

    @abstractmethod
    def receive_emoji(self, emoji: str, sender: str):
        pass

    def receive_system_message(self, message: str):
        print(f"\n系统消息 -> {self.name}: {message}")

class RegularUser(User):
    def receive_message(self, message: str, sender: str):
        print(f"\n{sender} -> {self.name}: {message}")

    def receive_emoji(self, emoji: str, sender: str):
        print(f"{sender} -> {self.name}: 收到表情 {emoji}")

class AdminUser(User):
    def receive_message(self, message: str, sender: str):
        print(f"\n{sender} -> 管理员{self.name}: {message}")

    def receive_emoji(self, emoji: str, sender: str):
        print(f"{sender} -> 管理员{self.name}: 收到表情 {emoji}")

    def broadcast_announcement(self, message: str):
        if self.chat_room:
            print(f"\n系统公告 (来自管理员{self.name}): {message}")
            for user in self.chat_room._users.values():
                if user != self:
                    user.receive_system_message(f"管理员公告: {message}")

# 使用示例
if __name__ == "__main__":
    # 创建聊天室
    chat_room = ChatRoom()

    # 创建用户
    alice = RegularUser("Alice")
    bob = RegularUser("Bob")
    admin = AdminUser("Admin")

    # 注册用户
    chat_room.register_user(alice)
    chat_room.register_user(bob)
    chat_room.register_user(admin)

    # 测试消息发送
    alice.send_message("大家好！", to=None)  # 群发
    bob.send_message("你好Alice", to="Alice")  # 私聊
    alice.send_emoji("😊")  # 发送表情
    admin.broadcast_announcement("今晚系统维护")  # 管理员公告
    bob.send_message("你好管理员", to="Admin")  # 给管理员发消息
