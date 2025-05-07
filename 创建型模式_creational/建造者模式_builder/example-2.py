from abc import ABC, abstractmethod
from typing import List

# 产品类
class Computer:
    def __init__(self):
        self.cpu = None
        self.motherboard = None
        self.memory = []
        self.storage = []
        self.gpu = None
        self.power_supply = None
        self.case = None

    def __str__(self):
        return f"""电脑配置：
CPU: {self.cpu}
主板: {self.motherboard}
内存: {', '.join(self.memory)}
存储: {', '.join(self.storage)}
显卡: {self.gpu}
电源: {self.power_supply}
机箱: {self.case}"""

# 抽象建造者
class ComputerBuilder(ABC):
    @abstractmethod
    def add_cpu(self):
        pass

    @abstractmethod
    def add_motherboard(self):
        pass

    @abstractmethod
    def add_memory(self):
        pass

    @abstractmethod
    def add_storage(self):
        pass

    @abstractmethod
    def add_gpu(self):
        pass

    @abstractmethod
    def add_power_supply(self):
        pass

    @abstractmethod
    def add_case(self):
        pass

# 具体建造者 - 游戏电脑
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self):
        self.computer.cpu = "Intel i9-13900K"
        return self

    def add_motherboard(self):
        self.computer.motherboard = "ASUS ROG MAXIMUS Z790"
        return self

    def add_memory(self):
        self.computer.memory = ["32GB DDR5 6000MHz", "32GB DDR5 6000MHz"]
        return self

    def add_storage(self):
        self.computer.storage = ["2TB NVMe SSD", "4TB HDD"]
        return self

    def add_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"
        return self

    def add_power_supply(self):
        self.computer.power_supply = "1200W 80+ Platinum"
        return self

    def add_case(self):
        self.computer.case = "Lian Li O11 Dynamic"
        return self

    def get_result(self):
        return self.computer

# 具体建造者 - 办公电脑
class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self):
        self.computer.cpu = "Intel i5-12400"
        return self

    def add_motherboard(self):
        self.computer.motherboard = "ASUS PRIME B660"
        return self

    def add_memory(self):
        self.computer.memory = ["16GB DDR4 3200MHz"]
        return self

    def add_storage(self):
        self.computer.storage = ["1TB NVMe SSD"]
        return self

    def add_gpu(self):
        self.computer.gpu = "集成显卡"
        return self

    def add_power_supply(self):
        self.computer.power_supply = "550W 80+ Bronze"
        return self

    def add_case(self):
        self.computer.case = "普通ATX机箱"
        return self

    def get_result(self):
        return self.computer

# 指导者
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self):
        return (self.builder
                .add_cpu()
                .add_motherboard()
                .add_memory()
                .add_storage()
                .add_gpu()
                .add_power_supply()
                .add_case()
                .get_result())

# 使用示例
if __name__ == "__main__":
    # 创建游戏电脑
    gaming_builder = GamingComputerBuilder()
    gaming_director = ComputerDirector(gaming_builder)
    gaming_computer = gaming_director.build_computer()
    print("游戏电脑配置：")
    print(gaming_computer)
    print("\n" + "="*50 + "\n")

    # 创建办公电脑
    office_builder = OfficeComputerBuilder()
    office_director = ComputerDirector(office_builder)
    office_computer = office_director.build_computer()
    print("办公电脑配置：")
    print(office_computer)