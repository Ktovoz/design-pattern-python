from typing import List

class GameState:
    """游戏状态类"""
    def __init__(self, level: int, score: int, lives: int):
        self.level = level
        self.score = score
        self.lives = lives

class GameMemento:
    """游戏备忘录类"""
    def __init__(self, state: GameState):
        self.state = state

class Game:
    """游戏类"""
    def __init__(self):
        self.state = GameState(1, 0, 3)
        self.saves: List[GameMemento] = []

    def save_game(self) -> GameMemento:
        """保存游戏"""
        memento = GameMemento(GameState(
            self.state.level,
            self.state.score,
            self.state.lives
        ))
        self.saves.append(memento)
        return memento

    def load_game(self, memento: GameMemento):
        """加载游戏"""
        self.state = memento.state

    def play(self):
        """玩游戏"""
        self.state.level += 1
        self.state.score += 100
        self.state.lives -= 1

def main():
    # 创建游戏
    game = Game()
    
    # 玩游戏
    game.play()
    print(f"游戏状态: 关卡={game.state.level}, 分数={game.state.score}, 生命={game.state.lives}")
    
    # 保存游戏
    save1 = game.save_game()
    
    # 继续玩游戏
    game.play()
    print(f"游戏状态: 关卡={game.state.level}, 分数={game.state.score}, 生命={game.state.lives}")
    
    # 加载之前的存档
    game.load_game(save1)
    print(f"加载存档后: 关卡={game.state.level}, 分数={game.state.score}, 生命={game.state.lives}")

if __name__ == "__main__":
    main()
