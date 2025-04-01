from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.n)]
        self.m = len(self.grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(self, y, x, visited, color):
        return 0 <= y < self.n and 0 <= x < len(self.grid[0]) and not visited[y][x] and self.grid[y][x] == color

    def search(self, y, x):
        visited = [[False] * len(self.grid[0]) for _ in range(self.n)]
        visited[y][x] = True
        candidates = [(y, x)]
        dq = deque([(y, x)])
        color = self.grid[y][x]

        while dq:
            cy, cx = dq.popleft()

            for dy, dx in self.directions:
                my, mx = cy + dy, cx + dx
                if self.is_valid(my, mx, visited, color):
                    visited[my][mx] = True
                    dq.append((my, mx))
                    candidates.append((my, mx))

        return candidates

    def eliminate(self, targets):
        for target in targets:
            for y, x in target:
                self.grid[y][x] = '0'

    def down(self):
        candidates = []
        for x in range(self.m):
            for y in range(self.n):
                if self.grid[y][x] != '0':
                    candidates.append(self.grid[y][x])

            for y in range(self.n-1, -1, -1):
                if candidates:
                    self.grid[y][x] = candidates.pop()
                else:
                    self.grid[y][x] = '0'

    def solve(self):
        while True:
            targets = []
            for y in range(self.n):
                for x in range(self.m):
                    if self.grid[y][x] != '0':
                        candidates = self.search(y, x)
                        if len(candidates) >= self.k:
                            targets.append(candidates)

            if not targets:
                break

            self.eliminate(targets)
            self.down()

        for i in self.grid:
            print("".join(i))


problem = Main()
problem.solve()
