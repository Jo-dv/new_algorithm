class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.cords = [tuple(map(lambda i: int(i) - 1, input().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        picture = [[0] * 100 for _ in range(100)]

        for cord in self.cords:
            x1, y1, x2, y2 = cord
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    picture[y][x] += 1

        for y in range(100):
            for x in range(100):
                if picture[y][x] > self.m:
                    self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()
