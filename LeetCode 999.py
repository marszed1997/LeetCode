class Solution:

    def checkCount(self, y, x, board):
        ans = 0
        for y_ in range(y - 1, -1, -1):
            chess = board[y_][x]
            if chess == "p":
                ans += 1
                break
            if chess == "B":
                break
        for y_ in range(y + 1, len(board)):
            chess = board[y_][x]
            if chess == "p":
                ans += 1
                break
            if chess == "B":
                break
        
        for x_ in range(x - 1, -1, -1):
            chess = board[y][x_]
            if chess == "p":
                ans += 1
                break
            if chess == "B":
                break
        for x_ in range(x + 1, len(board)):
            chess = board[y][x_]
            if chess == "p":
                ans += 1
                break
            if chess == "B":
                break
        return ans

    def numRookCaptures(self, board) -> int:    # board: List[List[str]]
        for y, yList in enumerate(board):
            for x, chess in enumerate(yList):
                if chess == "R":
                    return self.checkCount(y, x, board) 
        return 0