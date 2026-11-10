class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        mid = (r+l) // 2

        while l <= r:
            print(l,r,nums[mid])

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
            mid = (r+l) // 2
            print(mid)
        return -1