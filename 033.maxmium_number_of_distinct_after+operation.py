class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        res = 0
        prev = -10**9
        for x in nums:
            # Compute the smallest valid number greater than prev
            val = max(x - k, prev + 1)
            if val <= x + k:
                res += 1
                prev = val
        return res
