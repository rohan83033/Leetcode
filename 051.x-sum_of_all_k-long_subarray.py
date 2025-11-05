from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums, k, x):
        freq = Counter()
        top = SortedList()      # stores top X elements (as negative for max-heap behavior)
        rest = SortedList()     # stores the rest
        top_sum = 0
        ans = []

        def balance():
            nonlocal top_sum
            # Move from rest to top until size x is met
            while len(top) < x and rest:
                f, v = rest.pop(0)
                top.add((f, v))
                top_sum += (-f) * (-v)

            # If top is more than x, move smallest of top to rest
            while len(top) > x:
                f, v = top.pop(-1)
                top_sum -= (-f) * (-v)
                rest.add((f, v))

            # Ensure ordering: largest freq/value in top
            while rest and top and rest[0] < top[-1]:
                f1, v1 = rest.pop(0)
                f2, v2 = top.pop(-1)
                top_sum += (-f1) * (-v1) - (-f2) * (-v2)
                top.add((f1, v1))
                rest.add((f2, v2))

        def add(num):
            nonlocal top_sum
            old = (-freq[num], -num)
            if freq[num] > 0:
                if old in top:
                    top.remove(old)
                    top_sum -= freq[num] * num
                else:
                    rest.remove(old)

            freq[num] += 1
            new = (-freq[num], -num)
            rest.add(new)
            balance()

        def remove(num):
            nonlocal top_sum
            old = (-freq[num], -num)
            if old in top:
                top.remove(old)
                top_sum -= freq[num] * num
            else:
                rest.remove(old)

            freq[num] -= 1
            if freq[num] > 0:
                rest.add((-freq[num], -num))
            else:
                del freq[num]
            balance()

        # Initial window
        for i in range(k):
            add(nums[i])
        ans.append(top_sum)

        # Slide window
        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])
            ans.append(top_sum)

        return ans
