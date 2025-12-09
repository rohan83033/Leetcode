from typing import List
from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n < 3:
            return 0

        freq = Counter(nums)
        prev = {}

        cnt = 0
        x = nums[0]
        prev[x] = 1

        get_prev = prev.get
        get_freq = freq.get

        for i in range(1, n - 1):
            x = nums[i]
            x2 = x << 1

            left = get_prev(x2, 0)
            if left:
                right = get_freq(x2, 0) - left - (1 if x == 0 else 0)
                if right > 0:
                    cnt += left * right

            prev[x] = get_prev(x, 0) + 1

        return cnt % MOD
