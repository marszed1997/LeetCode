import queue


class Solution:
    def __init__(self):
        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def check(self, y, x, maxy, maxx):
        if 0 <= y < maxy and 0 <= x < maxx:
            return True
        return False

    def bfs(self, y, x, flag):
        # print("111")
        ans = 0
        Q = queue.Queue()
        Q.put(tuple([y, x]))
        while Q.empty() is False:
            y, x = Q.get()
            if flag[y][x]:
                continue
            # print(y, x)
            ans += 1
            flag[y][x] = 1
            for i in range(4):
                y_ = y + self.dir[i][0]
                x_ = x + self.dir[i][1]
                if self.check(y_, x_, len(flag), len(flag[0])):
                    # print(y_, x_, len(flag), len(flag[0]))
                    if flag[y_][x_] == 0 and grid[y_][x_] != 0:
                        Q.put(tuple([y_, x_]))
        return ans

    def maxAreaOfIsland(self, grid) -> int:
        ans = 0
        flag = [[] for i in range(len(grid))]
        for i in range(len(grid)):
            for _ in range(len(grid[0])):
                flag[i].append(0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if flag[i][j] == 0 and grid[i][j] != 0:
                    ans = max(ans, self.bfs(i, j, flag))
        return ans


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    a = Solution()
    print(a.maxAreaOfIsland(grid))