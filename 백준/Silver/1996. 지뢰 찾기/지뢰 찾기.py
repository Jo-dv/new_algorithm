class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(input()) for _ in range(self.n)]

    def solve(self):
        bombs = [(y, x) for x in range(self.n) for y in range(self.n) if self.grid[y][x] != "."]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        result = [[0] * self.n for _ in range(self.n)]
        for bomb in bombs:
            y, x = bomb
            result[y][x] = "*"
            for dy, dx in directions:
                my, mx = y + dy, x + dx
                if 0 <= my < self.n and 0 <= mx < self.n:
                    if result[my][mx] == "M" or result[my][mx] == "*":
                        continue
                    result[my][mx] += int(self.grid[y][x])
                    if result[my][mx] >= 10:
                        result[my][mx] = "M"

        for i in range(self.n):
            for j in range(self.n):
                result[i][j] = str(result[i][j])

        for i in result:
            print("".join(i))


problem = Main()
problem.solve()