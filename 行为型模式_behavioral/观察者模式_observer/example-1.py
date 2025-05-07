from abc import ABC, abstractmethod

class Subject:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

class WeatherStation(Subject):
    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"温度显示器: 当前温度是 {temperature}°C")

class TemperatureAlert(Observer):
    def update(self, temperature):
        if temperature > 30:
            print(f"温度警报: 温度过高 ({temperature}°C)！")

# 使用示例
if __name__ == "__main__":
    weather_station = WeatherStation()
    
    display = TemperatureDisplay()
    alert = TemperatureAlert()
    
    weather_station.attach(display)
    weather_station.attach(alert)
    
    print("天气站更新温度...")
    weather_station.set_temperature(24)
    weather_station.set_temperature(32)
