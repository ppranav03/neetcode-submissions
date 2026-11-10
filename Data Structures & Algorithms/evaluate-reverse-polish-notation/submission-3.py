import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '/', '*']

        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            
            else:
                a = stack.pop()
                b = stack.pop()
                match t:
                    case "+":
                        stack.append(a+b)
                        # break
                    case "-":
                        stack.append(b-a)
                        # break
                    case "/":
                        stack.append(int(b/a))
                        # break                    
                    case "*":
                        stack.append(b*a)
                        # break
        return stack.pop()