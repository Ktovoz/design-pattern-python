from abc import ABC, abstractmethod
from typing import List

# 基础组件接口
class Phone(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_features(self) -> List[str]:
        pass

    @abstractmethod
    def get_protection_level(self) -> int:
        pass

# 具体组件
class BasicPhone(Phone):
    def get_price(self) -> float:
        return 3999.0

    def get_features(self) -> List[str]:
        return ["基本功能"]

    def get_protection_level(self) -> int:
        return 1

# 装饰器基类
class PhoneCaseDecorator(Phone):
    def __init__(self, phone: Phone):
        self._phone = phone

    def get_price(self) -> float:
        return self._phone.get_price()

    def get_features(self) -> List[str]:
        return self._phone.get_features()

    def get_protection_level(self) -> int:
        return self._phone.get_protection_level()

# 具体装饰器
class SiliconeCaseDecorator(PhoneCaseDecorator):
    def get_price(self) -> float:
        return self._phone.get_price() + 99.0

    def get_features(self) -> List[str]:
        features = self._phone.get_features()
        features.append("防滑硅胶保护")
        return features

    def get_protection_level(self) -> int:
        return self._phone.get_protection_level() + 1

class BumperCaseDecorator(PhoneCaseDecorator):
    def get_price(self) -> float:
        return self._phone.get_price() + 199.0

    def get_features(self) -> List[str]:
        features = self._phone.get_features()
        features.append("防摔边框保护")
        return features

    def get_protection_level(self) -> int:
        return self._phone.get_protection_level() + 2

class TemperedGlassDecorator(PhoneCaseDecorator):
    def get_price(self) -> float:
        return self._phone.get_price() + 49.0

    def get_features(self) -> List[str]:
        features = self._phone.get_features()
        features.append("钢化玻璃屏幕保护")
        return features

    def get_protection_level(self) -> int:
        return self._phone.get_protection_level() + 1

# 使用示例
if __name__ == "__main__":
    # 创建基础手机
    phone = BasicPhone()
    print("基础手机配置：")
    print(f"价格: ¥{phone.get_price()}")
    print(f"功能: {', '.join(phone.get_features())}")
    print(f"保护等级: {phone.get_protection_level()}")

    # 添加硅胶保护壳
    phone_with_silicone = SiliconeCaseDecorator(phone)
    print("\n添加硅胶保护壳后：")
    print(f"价格: ¥{phone_with_silicone.get_price()}")
    print(f"功能: {', '.join(phone_with_silicone.get_features())}")
    print(f"保护等级: {phone_with_silicone.get_protection_level()}")

    # 添加防摔边框
    phone_with_bumper = BumperCaseDecorator(phone_with_silicone)
    print("\n添加防摔边框后：")
    print(f"价格: ¥{phone_with_bumper.get_price()}")
    print(f"功能: {', '.join(phone_with_bumper.get_features())}")
    print(f"保护等级: {phone_with_bumper.get_protection_level()}")

    # 添加钢化玻璃膜
    phone_with_glass = TemperedGlassDecorator(phone_with_bumper)
    print("\n添加钢化玻璃膜后：")
    print(f"价格: ¥{phone_with_glass.get_price()}")
    print(f"功能: {', '.join(phone_with_glass.get_features())}")
    print(f"保护等级: {phone_with_glass.get_protection_level()}")
