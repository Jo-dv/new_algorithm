import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.q = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(2**self.n)]
        self.spells = list(map(int, input().split()))
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.answer = 0

    def rotate(self, spell):
        new_grid = [[0] * self.n for _ in range(self.n)]

        for y in range(0, self.n, spell):
            for x in range(0, self.n, spell):
                for i in range(spell):
                    for j in range(spell):
                        new_grid[y+i][x+j] = self.grid[spell-1+y-j][x+i]

        self.grid = new_grid

    def melt(self):
        new_grid = [i[:] for i in self.grid]

        for y in range(self.n):
            for x in range(self.n):
                if self.grid[y][x] == 0:
                    continue

                cnt = 0
                for dy, dx in self.directions:
                    my, mx = y + dy, x + dx
                    if 0 <= my < self.n and 0 <= mx < self.n and self.grid[my][mx] != 0:
                        cnt += 1

                if cnt < 3:
                    new_grid[y][x] -= 1

        self.grid = new_grid

    def search(self):
        visited = [[False] * self.n for _ in range(self.n)]

        for y in range(self.n):
            for x in range(self.n):
                if self.grid[y][x] != 0 and not visited[y][x]:
                    dq = deque([(y, x)])
                    cnt = 0

                    while dq:
                        cy, cx = dq.popleft()

                        for dy, dx in self.directions:
                            my, mx = cy + dy, cx + dx
                            if 0 <= my < self.n and 0 <= mx < self.n and not visited[my][mx] and self.grid[my][mx] != 0:
                                dq.append((my, mx))
                                visited[my][mx] = True
                                cnt += 1

                    self.answer = max(self.answer, cnt)

    def solve(self):
        self.n = 2**self.n

        for spell in self.spells:
            self.rotate(2**spell)
            self.melt()
        self.search()

        print(sum((sum(i) for i in self.grid)))
        print(self.answer)


problem = Main()
problem.solve()