from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        return (msb:=0) or [((msb:=((msb<<1)+x)%5)==0) for x in nums ]