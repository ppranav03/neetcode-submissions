import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        """
        [1, 2, 3 ,4]
        h = 9

        Sorting and using the last number at a time.
        Binary search can help with that.
        
        math.ceil(a / b)
        """
        piles.sort()

        l, r, k = 1, piles[-1], piles[-1]
        while l <= r:

            curr_k = (l + r) // 2
            curr_hours = 0
            for p in piles:
                curr_hours += math.ceil(p/curr_k)
            if curr_hours > h:
                l = curr_k + 1
            elif curr_hours <= h:
                r = curr_k - 1
                k = curr_k

        return k




