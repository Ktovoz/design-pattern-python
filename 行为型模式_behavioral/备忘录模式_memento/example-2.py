from typing import List, Dict
from datetime import datetime

class TextState:
    """文本状态类"""
    def __init__(self, content: str, cursor_position: int, selection: Dict[str, int]):
        self.content = content
        self.cursor_position = cursor_position
        self.selection = selection
        self.timestamp = datetime.now()

class TextMemento:
    """文本备忘录类"""
    def __init__(self, state: TextState):
        self.state = state

class TextEditor:
    """文本编辑器类"""
    def __init__(self):
        self.state = TextState("", 0, {"start": 0, "end": 0})
        self.history: List[TextMemento] = []
        self.current_index = -1

    def type_text(self, text: str):
        """输入文本"""
        content = self.state.content[:self.state.cursor_position] + text + self.state.content[self.state.cursor_position:]
        self.state = TextState(
            content,
            self.state.cursor_position + len(text),
            self.state.selection
        )
        self.save_state()

    def move_cursor(self, position: int):
        """移动光标"""
        if 0 <= position <= len(self.state.content):
            self.state = TextState(
                self.state.content,
                position,
                self.state.selection
            )
            self.save_state()

    def select_text(self, start: int, end: int):
        """选择文本"""
        if 0 <= start <= end <= len(self.state.content):
            self.state = TextState(
                self.state.content,
                self.state.cursor_position,
                {"start": start, "end": end}
            )
            self.save_state()

    def save_state(self):
        """保存状态"""
        memento = TextMemento(TextState(
            self.state.content,
            self.state.cursor_position,
            self.state.selection
        ))
        # 如果当前不在历史记录末尾，删除当前位置之后的所有记录
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]
        self.history.append(memento)
        self.current_index = len(self.history) - 1

    def undo(self):
        """撤销"""
        if self.current_index > 0:
            self.current_index -= 1
            self.state = self.history[self.current_index].state
            return True
        return False

    def redo(self):
        """重做"""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            self.state = self.history[self.current_index].state
            return True
        return False

def main():
    # 创建文本编辑器
    editor = TextEditor()
    
    # 输入文本
    editor.type_text("Hello")
    print(f"输入后: {editor.state.content}")
    
    # 移动光标并继续输入
    editor.move_cursor(5)
    editor.type_text(" World")
    print(f"继续输入后: {editor.state.content}")
    
    # 选择文本
    editor.select_text(0, 5)
    print(f"选择文本: {editor.state.content[editor.state.selection['start']:editor.state.selection['end']]}")
    
    # 撤销
    editor.undo()
    print(f"撤销后: {editor.state.content}")
    
    # 重做
    editor.redo()
    print(f"重做后: {editor.state.content}")

if __name__ == "__main__":
    main()
