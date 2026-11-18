class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.results = []
        
        def backtrack(curr, idx):
            self.results.append(curr.copy())

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        
        backtrack([], 0)
        return self.results