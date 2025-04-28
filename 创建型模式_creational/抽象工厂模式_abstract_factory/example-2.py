from abc import ABC, abstractmethod

# =============== 抽象产品类 ===============

class Smartphone(ABC):
    """智能手机的抽象类"""
    @abstractmethod
    def make_call(self):
        pass

    @abstractmethod
    def get_model_info(self):
        pass

class Tablet(ABC):
    """平板电脑的抽象类"""
    @abstractmethod
    def browse_internet(self):
        pass

    @abstractmethod
    def get_screen_size(self):
        pass

class Earphone(ABC):
    """耳机的抽象类"""
    @abstractmethod
    def play_music(self):
        pass

    @abstractmethod
    def get_battery_life(self):
        pass

# =============== 具体产品类 - 苹果产品 ===============

class IPhone(Smartphone):
    """苹果手机"""
    def make_call(self):
        return "使用iPhone进行FaceTime通话"

    def get_model_info(self):
        return "iPhone 14 Pro Max"

class IPad(Tablet):
    """苹果平板"""
    def browse_internet(self):
        return "在iPad上使用Safari浏览网页"

    def get_screen_size(self):
        return "12.9英寸视网膜显示屏"

class AirPods(Earphone):
    """苹果耳机"""
    def play_music(self):
        return "使用AirPods播放音乐，支持空间音频"

    def get_battery_life(self):
        return "单次充电可使用6小时"

# =============== 具体产品类 - 三星产品 ===============

class GalaxyPhone(Smartphone):
    """三星手机"""
    def make_call(self):
        return "使用Galaxy S23进行视频通话"

    def get_model_info(self):
        return "Galaxy S23 Ultra"

class GalaxyTab(Tablet):
    """三星平板"""
    def browse_internet(self):
        return "在Galaxy Tab上使用Chrome浏览网页"

    def get_screen_size(self):
        return "14.6英寸Super AMOLED显示屏"

class GalaxyBuds(Earphone):
    """三星耳机"""
    def play_music(self):
        return "使用Galaxy Buds播放音乐，支持主动降噪"

    def get_battery_life(self):
        return "单次充电可使用5小时"

# =============== 抽象工厂 ===============

class ElectronicsFactory(ABC):
    """电子产品工厂的抽象类"""
    @abstractmethod
    def create_smartphone(self) -> Smartphone:
        pass

    @abstractmethod
    def create_tablet(self) -> Tablet:
        pass

    @abstractmethod
    def create_earphone(self) -> Earphone:
        pass

# =============== 具体工厂 ===============

class AppleFactory(ElectronicsFactory):
    """苹果产品工厂"""
    def create_smartphone(self) -> Smartphone:
        return IPhone()

    def create_tablet(self) -> Tablet:
        return IPad()

    def create_earphone(self) -> Earphone:
        return AirPods()

class SamsungFactory(ElectronicsFactory):
    """三星产品工厂"""
    def create_smartphone(self) -> Smartphone:
        return GalaxyPhone()

    def create_tablet(self) -> Tablet:
        return GalaxyTab()

    def create_earphone(self) -> Earphone:
        return GalaxyBuds()

# =============== 客户端代码 ===============

def client_code(factory: ElectronicsFactory):
    """
    客户端代码 - 使用工厂创建并测试电子产品
    这段代码可以与任何工厂类一起工作，而不需要修改代码
    """
    smartphone = factory.create_smartphone()
    tablet = factory.create_tablet()
    earphone = factory.create_earphone()

    print(f"手机型号: {smartphone.get_model_info()}")
    print(f"通话功能: {smartphone.make_call()}")
    print(f"平板显示: {tablet.get_screen_size()}")
    print(f"平板功能: {tablet.browse_internet()}")
    print(f"耳机功能: {earphone.play_music()}")
    print(f"耳机续航: {earphone.get_battery_life()}")

# =============== 测试代码 ===============

if __name__ == "__main__":
    print("测试苹果产品系列:")
    client_code(AppleFactory())
    
    print("\n测试三星产品系列:")
    client_code(SamsungFactory())
