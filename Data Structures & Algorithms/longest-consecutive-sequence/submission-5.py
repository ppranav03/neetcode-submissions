class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        numsSet = sorted(list(set(nums)))
        longest = 0
        currStreak = 1
        print(numsSet)
        for i in range(1, len(numsSet)):
            if numsSet[i] == (numsSet[i-1] + 1):
                currStreak += 1
            else:
                longest = max(longest, currStreak)
                currStreak = 1
        
        return max(longest, currStreak)
