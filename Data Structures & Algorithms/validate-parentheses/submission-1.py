class Solution:
    def isValid(self, string: str) -> bool:
        matches  = {
        '}' : '{',
        ']' : '[',
        ')' : '('
        }
        stack = []
        for s in string:
            if s not in matches:
                stack.append(s)
            else:
                if stack and stack.pop() == matches[s]:
                    continue
                else:
                    return False
        
        return True and (len(stack) == 0)
