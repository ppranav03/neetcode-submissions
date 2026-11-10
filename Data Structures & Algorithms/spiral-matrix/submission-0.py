class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1 

        while l<=r and t<=b:

            for i in range(l, r + 1):
                output.append(matrix[t][i])
            t += 1
            # t is 1
            
            for i in range(t, b + 1):
                output.append(matrix[i][r])
            r -= 1
            # r is 0
            
            if t <= b:
                for i in range(r, l - 1, -1):
                    output.append(matrix[b][i])
                b -= 1
            
            if l <= r:
                for i in range(b, t - 1, -1):
                    output.append(matrix[i][l])
                l += 1

        # l r
        #       b
        #       t
        return output