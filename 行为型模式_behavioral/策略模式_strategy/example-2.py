from abc import ABC, abstractmethod
from datetime import datetime

# 出行策略接口
class TravelStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass
    
    @abstractmethod
    def calculate_time(self, distance):
        pass
    
    @abstractmethod
    def get_route(self, start, end):
        pass

# 具体策略：公交车
class BusStrategy(TravelStrategy):
    def calculate_cost(self, distance):
        # 假设每公里2元，起步价3元
        return max(3, distance * 2)
    
    def calculate_time(self, distance):
        # 假设平均速度30km/h，加上等车时间10分钟
        return (distance / 30) * 60 + 10
    
    def get_route(self, start, end):
        return f"从{start}乘坐公交车到{end}"

# 具体策略：出租车
class TaxiStrategy(TravelStrategy):
    def calculate_cost(self, distance):
        # 假设起步价13元，每公里2.5元
        return 13 + distance * 2.5
    
    def calculate_time(self, distance):
        # 假设平均速度40km/h
        return (distance / 40) * 60
    
    def get_route(self, start, end):
        return f"从{start}打车到{end}"

# 具体策略：共享单车
class BikeStrategy(TravelStrategy):
    def calculate_cost(self, distance):
        # 假设每30分钟1.5元
        time = self.calculate_time(distance)
        return (time / 30) * 1.5
    
    def calculate_time(self, distance):
        # 假设平均速度15km/h
        return (distance / 15) * 60
    
    def get_route(self, start, end):
        return f"从{start}骑共享单车到{end}"

# 上下文类
class TravelPlanner:
    def __init__(self):
        self._strategy = None
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def plan_trip(self, start, end, distance):
        if not self._strategy:
            print("请选择出行方式")
            return
        
        print(f"\n=== 出行方案 ===")
        print(f"路线: {self._strategy.get_route(start, end)}")
        print(f"距离: {distance}公里")
        print(f"预计费用: {self._strategy.calculate_cost(distance):.2f}元")
        print(f"预计时间: {self._strategy.calculate_time(distance):.1f}分钟")

# 使用示例
if __name__ == "__main__":
    planner = TravelPlanner()
    start = "家"
    end = "公司"
    distance = 10  # 10公里
    
    print("=== 不同出行方式对比 ===")
    
    # 公交车方案
    planner.set_strategy(BusStrategy())
    planner.plan_trip(start, end, distance)
    
    # 出租车方案
    planner.set_strategy(TaxiStrategy())
    planner.plan_trip(start, end, distance)
    
    # 共享单车方案
    planner.set_strategy(BikeStrategy())
    planner.plan_trip(start, end, distance)
