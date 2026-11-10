class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen, maxFreq, l = 0, 0, 0
        counts = {}

        for r in range(len(s)):
            if s[r] not in counts:
                counts[s[r]] = 1
            else:
                counts[s[r]] += 1
            
            maxFreq = max(maxFreq, counts[s[r]])
            length = r-l + 1
            # print(maxFreq, length)
            if (length - maxFreq) <= k:
                maxLen = max(maxLen, length)
            else:
                counts[s[l]] -= 1
                l += 1
            # print(maxLen)
        return maxLen

