from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        power = sum(batteries)
        while power // n < batteries[-1]:
            power -= batteries.pop()
            n -= 1
        return power // n