class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        not_grumps, max_grumps, l = 0, 0, 0

        for r in range(minutes):
            if grumpy[r] == 0:
                not_grumps += customers[r]
            else:
                max_grumps += customers[r]
        
        curr_grumps = max_grumps
        for r in range(minutes, len(customers)):
            if grumpy[l] == 1:
                curr_grumps -= customers[l]

            if grumpy[r] == 1:
                curr_grumps += customers[r]
            else:
                not_grumps += customers[r]
            max_grumps = max(curr_grumps, max_grumps)
            l += 1
        
        return max_grumps + not_grumps
        

            