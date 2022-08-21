from typing import Any


class StatisticalTest:
    def __init__(self, test_type: str, calls: list[list[Any]]):
        self.test_type = test_type
        self.calls = calls

    def do(self):
        if self.test_type == 'prop.test':
            from statstests import prop
            test_result = prop.test(self.calls)
            return test_result.result
