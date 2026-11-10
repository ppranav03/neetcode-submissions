class Solution:
    def findMin(self, nums: List[int]) -> int:

        mn = float("inf")
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
            mn = min(mn, nums[mid])
        
        return int(mn)

        