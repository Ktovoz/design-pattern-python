class DVDPlayer:
    def on(self):
        print("DVD播放器开启")
    
    def play(self, movie):
        print(f"正在播放电影: {movie}")
    
    def off(self):
        print("DVD播放器关闭")

class Projector:
    def on(self):
        print("投影仪开启")
    
    def set_input(self, source):
        print(f"设置输入源为: {source}")
    
    def off(self):
        print("投影仪关闭")

class SoundSystem:
    def on(self):
        print("音响系统开启")
    
    def set_volume(self, level):
        print(f"设置音量为: {level}")
    
    def off(self):
        print("音响系统关闭")

class HomeTheaterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projector = Projector()
        self.sound = SoundSystem()
    
    def watch_movie(self, movie):
        print("准备观看电影...")
        self.dvd.on()
        self.projector.on()
        self.projector.set_input("DVD")
        self.sound.on()
        self.sound.set_volume(5)
        self.dvd.play(movie)
    
    def end_movie(self):
        print("结束观看电影...")
        self.dvd.off()
        self.projector.off()
        self.sound.off()

# 使用示例
if __name__ == "__main__":
    theater = HomeTheaterFacade()
    theater.watch_movie("泰坦尼克号")
    print("\n电影播放中...\n")
    theater.end_movie()
