from collections import Counter
from bisect import bisect_right
from typing import List
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)
        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]
        for i in range(1, n):
            take = freq[keys[i]] * keys[i]
            j = bisect_right(keys, keys[i] - 3) - 1
            if j >= 0:
                take += dp[j]
            dp[i] = max(dp[i - 1], take)
        return dp[-1]
