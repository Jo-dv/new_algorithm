from collections import deque


class Main:
    def __init__(self):
        self.l, self.r, self.c = None, None, None
        self.grid = None
        self.directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)]
        self.answer = []

    def init_grid(self):
        self.l, self.r, self.c = map(int, input().split())
        if self.l == self.r == self.c == 0:
            return False

        self.grid = []
        for _ in range(self.l):
            floor = []
            for _ in range(self.r + 1):
                info = list(input())
                if info:
                    floor.append(info)
                else:
                    self.grid.append(floor)

        return True

    def find_points(self):
        for z in range(self.l):
            for y in range(self.r):
                for x in range(self.c):
                    if self.grid[z][y][x] == "S":
                        return z, y, x

    def is_valid(self, z, y, x, visited):
        return 0 <= z < self.l and 0 <= y < self.r and 0 <= x < self.c and not visited[z][y][x] and self.grid[z][y][x] != "#"

    def search(self):
        start = self.find_points()
        sz, sy, sx = start
        visited = [[[False] * self.c for _ in range(self.r)] for _ in range(self.l)]
        visited[sz][sy][sx] = True
        dq = deque([(0, sz, sy, sx)])

        while dq:
            time, z, y, x = dq.popleft()
            if self.grid[z][y][x] == "E":
                return f"Escaped in {time} minute(s)."

            for dz, dy, dx in self.directions:
                mz, my, mx = z + dz, y + dy, x + dx
                if self.is_valid(mz, my, mx, visited):
                    visited[mz][my][mx] = True
                    dq.append((time + 1, mz, my, mx))

        return "Trapped!"

    def solve(self):
        while True:
            if not self.init_grid():
                print("\n".join(self.answer))
                return
            self.answer.append(self.search())


problem = Main()
problem.solve()
