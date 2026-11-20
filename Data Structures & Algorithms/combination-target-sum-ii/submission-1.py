class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.results = []
        candidates.sort()

        def backtrack(curr_total, curr, idx):
            if curr_total == target and curr.copy() not in self.results:
                self.results.append(curr.copy())
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if (curr_total + candidates[i]) > target:
                    return
                curr.append(candidates[i])
                backtrack(curr_total + candidates[i], curr, i + 1)
                curr.pop()
        
        backtrack(0, [], 0)
        return self.results