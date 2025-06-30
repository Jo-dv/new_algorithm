from collections import deque


class Main:
    def __init__(self):
        self.r, self.c = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.r)]
        self.visited = [[False] * self.c for _ in range(self.r)]
        self.answer = 0

    def search(self, y, x):
        self.visited[y][x] = True
        dq = deque([(y, x, 1)])

        while dq:
            cy, cx, size = dq.popleft()
            if size == 2:
                return

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my, mx = cy + dy, cx + dx
                if 0 <= my < self.r and 0 <= mx < self.c and not self.visited[my][mx] and self.grid[my][mx] == "#":
                    dq.append((my, mx, size + 1))
                    self.visited[my][mx] = True

        return

    def solve(self):
        for y in range(self.r):
            for x in range(self.c):
                if not self.visited[y][x] and self.grid[y][x] == "#":
                    self.search(y, x)
                    self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()