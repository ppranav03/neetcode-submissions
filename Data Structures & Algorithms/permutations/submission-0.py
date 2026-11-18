class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.results = []
        self.added = [False for _ in range(n)]
        def backtrack(curr):
            if len(curr) == n:
                self.results.append(curr.copy())
                return
            
            for i, num in enumerate(nums):
                if not self.added[i]:
                    curr.append(num)
                    self.added[i] = True
                    
                    backtrack(curr)
                    curr.pop()
                    self.added[i] = False
            
        

        backtrack([])
        return self.results