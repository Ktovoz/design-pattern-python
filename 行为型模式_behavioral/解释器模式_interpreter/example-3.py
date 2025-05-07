from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import re

# 抽象表达式
class TimeExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 基础时间表达式
class BaseTimeExpression(TimeExpression):
    def __init__(self):
        self.now = datetime.now()

# 日期表达式
class DateExpression(BaseTimeExpression):
    def interpret(self, context):
        if "明天" in context:
            return self.now + timedelta(days=1)
        elif "后天" in context:
            return self.now + timedelta(days=2)
        elif "昨天" in context:
            return self.now - timedelta(days=1)
        return self.now

# 时间表达式
class TimeOfDayExpression(BaseTimeExpression):
    def interpret(self, context):
        hour_match = re.search(r'(\d{1,2})[点时]', context)
        minute_match = re.search(r'(\d{1,2})分', context)
        
        hour = int(hour_match.group(1)) if hour_match else self.now.hour
        minute = int(minute_match.group(1)) if minute_match else 0
        
        if "下午" in context or "晚上" in context:
            hour = hour + 12 if hour < 12 else hour
        
        return hour, minute

# 时间段表达式
class DurationExpression(BaseTimeExpression):
    def interpret(self, context):
        hours = 0
        minutes = 0
        
        hour_match = re.search(r'(\d+)小时', context)
        minute_match = re.search(r'(\d+)分钟', context)
        
        if hour_match:
            hours = int(hour_match.group(1))
        if minute_match:
            minutes = int(minute_match.group(1))
            
        return timedelta(hours=hours, minutes=minutes)

# 复合时间表达式
class ComplexTimeExpression(BaseTimeExpression):
    def __init__(self):
        super().__init__()
        self.date_expr = DateExpression()
        self.time_expr = TimeOfDayExpression()
        self.duration_expr = DurationExpression()
    
    def interpret(self, context):
        # 解析日期
        date = self.date_expr.interpret(context)
        
        # 解析时间
        hour, minute = self.time_expr.interpret(context)
        
        # 设置基准时间
        base_time = date.replace(hour=hour, minute=minute)
        
        # 解析持续时间
        if "持续" in context or "经过" in context:
            duration = self.duration_expr.interpret(context)
            end_time = base_time + duration
            return base_time, end_time
        
        return base_time, None

# 时间解释器
class TimeInterpreter:
    def __init__(self):
        self.complex_expr = ComplexTimeExpression()
    
    def interpret(self, time_str):
        start_time, end_time = self.complex_expr.interpret(time_str)
        
        if end_time:
            return {
                'type': 'duration',
                'start': start_time.strftime('%Y-%m-%d %H:%M'),
                'end': end_time.strftime('%Y-%m-%d %H:%M'),
                'duration': str(end_time - start_time)
            }
        else:
            return {
                'type': 'point',
                'time': start_time.strftime('%Y-%m-%d %H:%M')
            }

def main():
    interpreter = TimeInterpreter()
    
    # 测试不同的时间表达式
    expressions = [
        "明天下午3点",
        "后天上午10点30分",
        "今天晚上8点持续2小时30分钟",
        "昨天下午2点经过1小时"
    ]
    
    for expr in expressions:
        result = interpreter.interpret(expr)
        print(f"\n解析表达式: {expr}")
        if result['type'] == 'duration':
            print(f"开始时间: {result['start']}")
            print(f"结束时间: {result['end']}")
            print(f"持续时间: {result['duration']}")
        else:
            print(f"时间点: {result['time']}")

if __name__ == "__main__":
    main()
