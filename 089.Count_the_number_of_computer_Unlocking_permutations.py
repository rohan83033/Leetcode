from typing import List

class Solution:
    def countPermutations(self, x: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(x)
        first = x[0]

        for i in range(1, n):
            if x[i] <= first:
                return 0

        ans = 1
        for k in range(2, n):
            ans = (ans * k) % MOD

        return ans
