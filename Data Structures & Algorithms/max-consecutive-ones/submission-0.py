class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        l = 0
        mx_len = 0
        curr_len = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                curr_len += 1
            else:
                mx_len = max(mx_len, curr_len)
                curr_len = 0
                l = r
        
        return max(mx_len, curr_len)