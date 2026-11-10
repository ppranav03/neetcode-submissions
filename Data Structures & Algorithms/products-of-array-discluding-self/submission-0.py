class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)
        prefix = 1

        for i in range (1, len(nums)):
            prefix *= nums[i-1]
            solution[i] *= prefix
            
        # print(solution)
        postfix = 1
        for i in range (len(nums)-2, -1, -1):
            postfix *= nums[i+1]
            solution[i] *= postfix
        
        return solution