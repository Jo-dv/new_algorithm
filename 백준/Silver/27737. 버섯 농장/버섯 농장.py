import sys
import math
sys.setrecursionlimit(1000000)  # 재귀 깊이 증가 필요


class Main:
    def __init__(self):
        self.n, self.m, self.k = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.visited = [[False] * self.n for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(self, y, x):
        self.visited[y][x] = True
        size = 1
        for dy, dx in self.directions:
            my, mx = y + dy, x + dx
            if 0 <= my < self.n and 0 <= mx < self.n:
                if not self.visited[my][mx] and self.grid[my][mx] == 0:
                    size += self.dfs(my, mx)

        return size

    def solve(self):
        needed_spores = 0

        for i in range(self.n):
            for j in range(self.n):
                if not self.visited[i][j] and self.grid[i][j] == 0:
                    region_size = self.dfs(i, j)
                    spores = math.ceil(region_size / self.k)
                    needed_spores += spores

        if 0 < needed_spores <= self.m:
            print("POSSIBLE")
            print(self.m - needed_spores)
        else:
            print("IMPOSSIBLE")


problem = Main()
problem.solve()
