class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mode = 0
        count = 0
        for num in nums:
            if count == 0:
                mode = num
                count += 1
            elif count != 0 and mode == num:
                count +=1
            else:
                count -= 1
        
        return mode
            