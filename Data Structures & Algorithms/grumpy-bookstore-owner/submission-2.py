class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ng_count, g_count = 0, 0

        for i in range(minutes):
            if grumpy[i] == 1:
                g_count += customers[i]
            else:
                ng_count += customers[i]
        

        l = 0
        g_count_temp = g_count
        for r in range(minutes, len(customers)):
            if grumpy[r] == 0:
                ng_count += customers[r]
            else:
                g_count_temp += customers[r]
            
            if grumpy[l] == 1:
                g_count_temp -= customers[l]
            l += 1
            g_count = max(g_count, g_count_temp)
        
        return ng_count + g_count
            

