class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        indices = {}
        l, max_len = 0, 0

        for r in range(len(s)):
            if s[r] in indices and indices[s[r]] >= l:
                l = indices[s[r]] + 1
            
            indices[s[r]] = r
            
            max_len = max(max_len, r - l + 1)


        return max_len
