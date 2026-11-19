class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.results = []
        nums.sort()

        def backtrack(curr_total, curr, idx):
            if curr_total == target:
                self.results.append(curr.copy())
            
            for i in range(idx, len(nums)):
                if (curr_total + nums[i]) > target:
                    return
                curr.append(nums[i])
                backtrack(curr_total + nums[i], curr, i)
                curr.pop()

        backtrack(0, [], 0)
        return self.results