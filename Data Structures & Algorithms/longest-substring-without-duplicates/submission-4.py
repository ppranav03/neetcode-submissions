class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        indices = {}
        l, max_len = 0, 0

        for r in range(len(s)):
            if s[r] in indices and indices[s[r]] >= l:
                l = indices[s[r]] + 1
            
            # Update the character's latest position
            indices[s[r]] = r
            
            # Calculate length (inclusive of both boundaries)
            max_len = max(max_len, r - l + 1)


        return max(max_len, r-l)
