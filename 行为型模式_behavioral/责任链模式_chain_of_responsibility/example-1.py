from abc import ABC, abstractmethod
from typing import Optional

# 抽象处理者
class Approver(ABC):
    def __init__(self, name: str):
        self.name = name
        self._next_approver: Optional[Approver] = None

    def set_next(self, approver: 'Approver') -> 'Approver':
        self._next_approver = approver
        return approver

    @abstractmethod
    def handle_request(self, amount: float) -> str:
        pass

# 具体处理者：组长（可以审批500元以下的采购）
class TeamLeader(Approver):
    def handle_request(self, amount: float) -> str:
        if amount <= 500:
            return f"{self.name}（组长）已批准采购金额：{amount}元"
        elif self._next_approver:
            return self._next_approver.handle_request(amount)
        return "采购申请被拒绝"

# 具体处理者：部门经理（可以审批5000元以下的采购）
class DepartmentManager(Approver):
    def handle_request(self, amount: float) -> str:
        if amount <= 5000:
            return f"{self.name}（部门经理）已批准采购金额：{amount}元"
        elif self._next_approver:
            return self._next_approver.handle_request(amount)
        return "采购申请被拒绝"

# 具体处理者：总经理（可以审批所有金额的采购）
class GeneralManager(Approver):
    def handle_request(self, amount: float) -> str:
        return f"{self.name}（总经理）已批准采购金额：{amount}元"

# 客户端代码
if __name__ == "__main__":
    # 创建审批人
    team_leader = TeamLeader("张三")
    department_manager = DepartmentManager("李四")
    general_manager = GeneralManager("王五")

    # 设置责任链
    team_leader.set_next(department_manager).set_next(general_manager)

    # 测试不同金额的采购申请
    print(team_leader.handle_request(300))      # 组长审批
    print(team_leader.handle_request(3000))     # 部门经理审批
    print(team_leader.handle_request(10000))    # 总经理审批
