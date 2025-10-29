class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 0:
            return 1
        m = n
        m |= m >> 1
        m |= m >> 2
        m |= m >> 4
        m |= m >> 8
        m |= m >> 16
        m |= m >> 32
        return m
