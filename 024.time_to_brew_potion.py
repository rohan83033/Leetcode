from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        done = [0] * (n + 1)
        for j in range(m):
            costs_for_j = [0] * n 
            for k in range(n):
                costs_for_j[k] = mana[j] * skill[k]
            for i in range(n):
                done[i + 1] = max(done[i + 1], done[i]) + costs_for_j[i]
            for i in range(n - 1, 0, -1):
                done[i] = done[i + 1] - costs_for_j[i]
        return done[n]
