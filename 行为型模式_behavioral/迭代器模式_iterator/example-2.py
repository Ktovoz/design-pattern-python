from abc import ABC, abstractmethod
from typing import List, Optional

# 歌曲类
class Song:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration  # 时长（秒）
    
    def __str__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} - {self.artist} ({minutes}:{seconds:02d})"

# 迭代器接口
class MusicIterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Optional[Song]:
        pass
    
    @abstractmethod
    def has_previous(self) -> bool:
        pass
    
    @abstractmethod
    def previous(self) -> Optional[Song]:
        pass

# 具体迭代器
class PlaylistIterator(MusicIterator):
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.current_position = -1
    
    def has_next(self) -> bool:
        return self.current_position < len(self.songs) - 1
    
    def next(self) -> Optional[Song]:
        if self.has_next():
            self.current_position += 1
            return self.songs[self.current_position]
        return None
    
    def has_previous(self) -> bool:
        return self.current_position > 0
    
    def previous(self) -> Optional[Song]:
        if self.has_previous():
            self.current_position -= 1
            return self.songs[self.current_position]
        return None

# 播放列表类
class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs: List[Song] = []
    
    def add_song(self, song: Song):
        self.songs.append(song)
    
    def iterator(self) -> MusicIterator:
        return PlaylistIterator(self.songs)

# 使用示例
if __name__ == "__main__":
    # 创建播放列表
    playlist = Playlist("我的最爱")
    
    # 添加歌曲
    playlist.add_song(Song("起风了", "买辣椒也用券", 325))
    playlist.add_song(Song("光年之外", "邓紫棋", 235))
    playlist.add_song(Song("海阔天空", "Beyond", 326))
    
    # 使用迭代器遍历播放列表
    iterator = playlist.iterator()
    
    print("正向播放：")
    while iterator.has_next():
        song = iterator.next()
        print(f"正在播放: {song}")
    
    print("\n反向播放：")
    while iterator.has_previous():
        song = iterator.previous()
        print(f"正在播放: {song}")
