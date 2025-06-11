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
        target = sum(sum(i) for i in sticker)

        for _ in range(4):
            width = len(sticker[0])
            height = len(sticker)
            for y in range(self.n - height + 1):
                for x in range(self.m - width + 1):
                    new_grid = [i[:] for i in self.grid]
                    cnt = 0
                    for i in range(height):
                        for j in range(width):
                            if sticker[i][j] == 1 and self.grid[y+i][x+j] == 0:
                                new_grid[y+i][x+j] = sticker[i][j]
                                cnt += 1

                    if cnt == target:
                        self.grid = new_grid
                        return

            rotate_sticker = []
            for i in zip(*sticker[::-1]):
                rotate_sticker.append(list(i))
            sticker = rotate_sticker

    def count_space(self):
        self.answer = sum(sum(i) for i in self.grid)

    def solve(self):
        for sticker in self.stickers:
            self.attach(sticker)

        self.count_space()
        print(self.answer)


problem = Main()
problem.solve()
