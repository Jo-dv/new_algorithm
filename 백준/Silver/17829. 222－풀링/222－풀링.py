class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]

    def search(self, y, x, size):
        if size == 2:
            temp = [
                self.grid[y][x],
                self.grid[y+1][x],
                self.grid[y][x+1],
                self.grid[y+1][x+1]
            ]
            temp.sort()
            return temp[2]

        new_size = size // 2
        temp = [
            self.search(y, x, new_size),
            self.search(y + new_size, x, new_size),
            self.search(y, x + new_size, new_size),
            self.search(y + new_size, x + new_size, new_size)
        ]
        temp.sort()
        return temp[2]

    def solve(self):
        answer = self.search(0, 0, self.n)
        print(answer)


problem = Main()
problem.solve()