class Solution:
    def removeDuplicates(self, string: str, k: int) -> str:
        stack = []

        for s in string:
            if stack and stack[-1][0] == s:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
                # let, count = stack.pop()
                # if count != k-1:
                #     stack.append((s, count+1))
            else:
                stack.append([s,1])
            # print(stack)

        output = [l * c for l, c in stack]
        return "".join(output)
            