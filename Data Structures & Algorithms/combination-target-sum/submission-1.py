class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        self.result = []

        def backtrack(remaining, curr, idx):
            if remaining == 0:
                self.result.append(curr.copy())
            
            for i in range(idx, len(nums)):
                if remaining < nums[i]:
                    break

                curr.append(nums[i])
                backtrack(remaining-nums[i], curr, i)
                curr.pop()
        

        backtrack(target, [], 0)
        return self.result