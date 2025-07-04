from collections import deque


class Main:
    def __init__(self):
        self.w, self.h = map(int, input().split())
        self.n = int(input())
        self.blocks = [input().split() for _ in range(self.n)]
        self.grid = [[None] * self.w for _ in range(self.h)]
        self.signal = [[0] * self.w for _ in range(self.h)]

    def search(self, block):
        dq = deque([block])

        while dq:
            y, x, s = dq.popleft()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my, mx = y + dy, x + dx
                if 0 <= my < self.h and 0 <= mx < self.w and self.signal[my][mx] < s:
                    self.signal[my][mx] = s
                    if self.grid[my][mx] == "redstone_dust":
                        dq.append((my, mx, s - 1))

    def solve(self):
        lamps = []
        blocks = []

        for block in self.blocks:
            b, x, y = block
            x = int(x)
            y = int(y)
            self.grid[y][x] = b

            if b == "redstone_block":
                self.signal[y][x] = 15
                blocks.append((y, x, 15))
            if b == "redstone_lamp":
                lamps.append((y, x))

        for block in blocks:
            self.search(block)

        if all(self.signal[y][x] >= 1 for y, x in lamps):
            print("success")
        else:
            print("failed")


problem = Main()
problem.solve()