class Main:
    def __init__(self):
        self.c, self.r = map(int, input().split())
        self.k = int(input())
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def solve(self):
        if self.c * self.r < self.k:
            print(0)
            return

        grid = [[0] * self.c for _ in range(self.r)]
        x, y = 0, 0
        grid[y][x] = 1
        cnt = 2
        i = 0

        while cnt <= self.k:
            dy, dx = self.directions[i]
            my, mx = y + dy, x + dx
            if 0 <= my < self.r and 0 <= mx < self.c and grid[my][mx] == 0:
                grid[my][mx] = cnt
                cnt += 1
                y = my
                x = mx
            else:
                i = (i + 1) % 4

        print(x+1, y+1)


problem = Main()
problem.solve()