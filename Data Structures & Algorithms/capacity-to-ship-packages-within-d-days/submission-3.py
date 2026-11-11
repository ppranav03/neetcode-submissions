class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Binary search with left being the max of weights, and right being
        sum of weights.
        """

        l, r = max(weights), sum(weights)
        mn_size = float("inf")
        while l <= r:
            mid = (l + r) // 2

            # print(mid)
            curr_mid = mid
            curr_days = days
            for w in weights:
                # print(curr_mid, w, curr_days)
                if w > curr_mid:
                    curr_days -= 1
                    curr_mid = mid - w
                else:
                    curr_mid -= w
            
            if curr_days > 0:
                mn_size = min(mn_size, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return mn_size