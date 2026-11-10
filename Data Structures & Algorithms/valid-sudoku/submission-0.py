class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        usedNums = [[] for _ in range(27)]

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                boxNum = (i // 3) * 3 + (j // 3) + 18
                jShifted = j + 9
                currNum = board[i][j]
                if currNum.isdigit():
                    if currNum not in usedNums[i] and currNum not in usedNums[jShifted] and currNum not in usedNums[boxNum]:
                        usedNums[i].append(currNum)
                        usedNums[jShifted].append(currNum)
                        usedNums[boxNum].append(currNum)        
                    else:
                        return False
        
        return True