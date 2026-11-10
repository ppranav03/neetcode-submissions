class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        count = 0
        pre_zero = False
        for n in num:
            
            while stack and stack[-1] > n and count < k:
                stack.pop()
                count += 1
            
            
            stack.append(n)
        # print(count)
        while count < k:
            stack.pop()
            count += 1

        stack_str = "".join(stack).lstrip('0')
        if len(stack_str) == 0:
            return "0"
        else:
            return stack_str