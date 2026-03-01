class LeaveManager:
    """Manage leave balances for employees."""

    def __init__(self):
        self.leave_balance = {}

    def set_balance(self, employee_id, casual=5, sick=5):
        self.leave_balance[employee_id] = {
            "casual": casual,
            "sick": sick
        }

    def apply_leave(self, employee_id, leave_type, days):
        """Attempt to deduct ``days`` of ``leave_type`` for ``employee_id``.

        Returns ``True`` on success, ``False`` if the employee or leave type is
        missing or if there isn't enough balance.
        """
        if employee_id not in self.leave_balance:
            return False

        if leave_type not in self.leave_balance[employee_id]:
            return False

        if self.leave_balance[employee_id][leave_type] >= days:
            self.leave_balance[employee_id][leave_type] -= days
            return True

        return False


if __name__ == "__main__":
    lm = LeaveManager()
    lm.set_balance("emp1", casual=10, sick=8)
    print(lm.apply_leave("emp1", "casual", 3))  
    print(lm.apply_leave("emp1", "sick", 9))   
    print(lm.leave_balance)