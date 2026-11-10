class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        indices = {}
        l, r, max_len = 0, 0, 0

        while l <= r and r < len(s):
            if s[r] in indices and indices[s[r]] >= l:
                l = indices[s[r]] + 1

            max_len = max(max_len, r - l + 1)
            indices[s[r]] = r
            
            r += 1

        return max_len
