class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        indices = {}
        l, r, max_len = 0, 0, 0

        while l <= r and r < len(s):
            if s[r] not in indices or indices[s[r]] < l:
                indices[s[r]] = r
            else:
                max_len = max(max_len, r - l)
                l = indices[s[r]] + 1
                indices[s[r]] = r
            r += 1

        return max(max_len, r-l)
