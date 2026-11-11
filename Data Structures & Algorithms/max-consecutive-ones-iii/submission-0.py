class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l, mx_len, curr_k = 0, 0, k
        for r, n in enumerate(nums):

            if n == 0:
                while curr_k < 1:
                    if nums[l] == 0:
                        curr_k += 1
                    l += 1
                curr_k -= 1
            
            print(r, l)
            mx_len = max(mx_len, r - l + 1)
        
        return max(mx_len, r - l + 1)

        