import sys
input = lambda:sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m, self.k = map(int, input().split())
        self.grid = [[0] * self.m for _ in range(self.n)]
        self.stickers = []
        for _ in range(self.k):
            r, c = map(int, input().split())
            sticker = [list(map(int, input().split())) for _ in range(r)]
            self.stickers.append(sticker)
        self.answer = 0

    def attach(self, sticker):
        for _ in range(4):
            height = len(sticker)
            width = len(sticker[0])
            for y in range(self.n - height + 1):
                for x in range(self.m - width + 1):
                    if self.can_attach(sticker, y, x):
                        self.do_attach(sticker, y, x)
                        return

            sticker = [list(row) for row in zip(*sticker[::-1])]

    def can_attach(self, sticker, y, x):
        height = len(sticker)
        width = len(sticker[0])
        for i in range(height):
            for j in range(width):
                if sticker[i][j] == 1 and self.grid[y + i][x + j] == 1:
                    return False
        return True

    def do_attach(self, sticker, y, x):
        height = len(sticker)
        width = len(sticker[0])
        for i in range(height):
            for j in range(width):
                if sticker[i][j] == 1:
                    self.grid[y + i][x + j] = 1

    def count_space(self):
        self.answer = sum(sum(i) for i in self.grid)

    def solve(self):
        for sticker in self.stickers:
            self.attach(sticker)

        self.count_space()
        print(self.answer)


problem = Main()
problem.solve()
