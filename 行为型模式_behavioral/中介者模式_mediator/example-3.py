"""
机场航班调度系统示例
展示了高级的中介者模式实现，包含多个组件和复杂的交互逻辑
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List
from datetime import datetime, timedelta
import random

class WeatherCondition(Enum):
    SUNNY = "晴朗"
    RAINY = "下雨"
    STORMY = "暴风"
    FOGGY = "大雾"

class RunwayStatus(Enum):
    AVAILABLE = "可用"
    OCCUPIED = "占用"
    MAINTENANCE = "维护中"

class FlightStatus(Enum):
    SCHEDULED = "计划中"
    BOARDING = "登机中"
    DELAYED = "延误"
    CANCELLED = "取消"
    IN_AIR = "飞行中"
    LANDED = "已降落"

class AirportComponent(ABC):
    def __init__(self, mediator: 'AirportMediator' = None):
        self._mediator = mediator

    @property
    def mediator(self) -> 'AirportMediator':
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: 'AirportMediator'):
        self._mediator = mediator

class WeatherStation(AirportComponent):
    def __init__(self, mediator: 'AirportMediator' = None):
        super().__init__(mediator)
        self._current_condition = WeatherCondition.SUNNY

    def update_weather(self, condition: WeatherCondition):
        self._current_condition = condition
        self.mediator.weather_changed(condition)

    @property
    def current_condition(self) -> WeatherCondition:
        return self._current_condition

class Runway(AirportComponent):
    def __init__(self, name: str, mediator: 'AirportMediator' = None):
        super().__init__(mediator)
        self.name = name
        self._status = RunwayStatus.AVAILABLE
        self._occupied_until = None

    def occupy(self, duration_minutes: int):
        self._status = RunwayStatus.OCCUPIED
        self._occupied_until = datetime.now() + timedelta(minutes=duration_minutes)
        return True

    def release(self):
        self._status = RunwayStatus.AVAILABLE
        self._occupied_until = None

    @property
    def status(self) -> RunwayStatus:
        if self._status == RunwayStatus.OCCUPIED and \
           self._occupied_until and datetime.now() > self._occupied_until:
            self.release()
        return self._status

class Flight(AirportComponent):
    def __init__(self, flight_number: str, mediator: 'AirportMediator' = None):
        super().__init__(mediator)
        self.flight_number = flight_number
        self._status = FlightStatus.SCHEDULED
        self.scheduled_time = datetime.now() + timedelta(minutes=random.randint(10, 60))

    @property
    def status(self) -> FlightStatus:
        return self._status

    @status.setter
    def status(self, new_status: FlightStatus):
        self._status = new_status
        if self.mediator:
            self.mediator.flight_status_changed(self)

    def request_landing(self):
        if self.mediator:
            return self.mediator.request_landing(self)
        return False

    def request_takeoff(self):
        if self.mediator:
            return self.mediator.request_takeoff(self)
        return False

class AirportMediator:
    def __init__(self):
        self._weather_station = WeatherStation(self)
        self._runways: Dict[str, Runway] = {}
        self._flights: Dict[str, Flight] = {}
        
        # 初始化跑道
        self.add_runway(Runway("R1", self))
        self.add_runway(Runway("R2", self))

    def add_runway(self, runway: Runway):
        runway.mediator = self
        self._runways[runway.name] = runway

    def register_flight(self, flight: Flight):
        flight.mediator = self
        self._flights[flight.flight_number] = flight
        print(f"航班 {flight.flight_number} 已注册到调度系统")

    def weather_changed(self, condition: WeatherCondition):
        print(f"\n天气状况更新: {condition.value}")
        if condition in [WeatherCondition.STORMY, WeatherCondition.FOGGY]:
            self._handle_severe_weather()

    def _handle_severe_weather(self):
        print("恶劣天气处理程序启动:")
        for flight in self._flights.values():
            if flight.status == FlightStatus.SCHEDULED:
                flight.status = FlightStatus.DELAYED
                print(f"航班 {flight.flight_number} 因天气原因延误")

    def _get_available_runway(self) -> Runway:
        for runway in self._runways.values():
            if runway.status == RunwayStatus.AVAILABLE:
                return runway
        return None

    def request_landing(self, flight: Flight) -> bool:
        if self._weather_station.current_condition in [WeatherCondition.STORMY, WeatherCondition.FOGGY]:
            print(f"航班 {flight.flight_number} 因恶劣天气无法降落")
            flight.status = FlightStatus.DELAYED
            return False

        runway = self._get_available_runway()
        if runway:
            runway.occupy(15)  # 占用跑道15分钟
            flight.status = FlightStatus.LANDED
            print(f"航班 {flight.flight_number} 正在使用跑道 {runway.name} 降落")
            return True
        else:
            print(f"航班 {flight.flight_number} 等待可用跑道")
            return False

    def request_takeoff(self, flight: Flight) -> bool:
        if self._weather_station.current_condition in [WeatherCondition.STORMY, WeatherCondition.FOGGY]:
            print(f"航班 {flight.flight_number} 因恶劣天气无法起飞")
            flight.status = FlightStatus.DELAYED
            return False

        runway = self._get_available_runway()
        if runway:
            runway.occupy(10)  # 占用跑道10分钟
            flight.status = FlightStatus.IN_AIR
            print(f"航班 {flight.flight_number} 正在使用跑道 {runway.name} 起飞")
            return True
        else:
            print(f"航班 {flight.flight_number} 等待可用跑道")
            return False

# 使用示例
if __name__ == "__main__":
    # 创建机场调度系统
    airport_system = AirportMediator()
    
    # 创建几个航班
    flights = [
        Flight("CA101"),
        Flight("MU202"),
        Flight("CZ303")
    ]
    
    # 注册航班
    for flight in flights:
        airport_system.register_flight(flight)
    
    print("\n=== 正常天气测试 ===")
    # 测试起飞和降落
    flights[0].request_takeoff()
    flights[1].request_landing()
    
    print("\n=== 恶劣天气测试 ===")
    # 更新天气状况
    airport_system._weather_station.update_weather(WeatherCondition.STORMY)
    
    # 尝试在恶劣天气起飞
    flights[2].request_takeoff()
    
    print("\n=== 天气恢复测试 ===")
    # 天气恢复
    airport_system._weather_station.update_weather(WeatherCondition.SUNNY)
    
    # 重新尝试起飞
    flights[2].request_takeoff()
