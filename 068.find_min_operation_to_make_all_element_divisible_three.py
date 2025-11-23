from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(num % 3 != 0 for num in nums)gam