import math
from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        first, second = -math.inf, -math.inf
        count = 0

        for interval in intervals:
            start = interval[0]
            end = interval[-1]
            if not (start <= second <= end): # no overlap
                count += 2
                first = end - 1
                second = end
            elif not (start <= first <= end): # overlap but only on last element (second)
                count += 1
                # only last element (second) of previously selected interval match
                first = min(second, end-1) # handles case where last element (second) is equal to end
                second = end
        return count

            