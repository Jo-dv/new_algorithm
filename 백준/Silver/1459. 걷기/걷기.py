class Main:
    def __init__(self):
        self.x, self.y, self.w, self.s = map(int, input().split())
        self.answer = 0

    def solve(self):
        self.answer = (self.x + self.y) * self.w

        self.answer = min(self.answer, min(self.x, self.y) * self.s + abs(self.x - self.y) * self.w)

        if self.s < 2 * self.w:
            if (self.x + self.y) % 2 == 0:
                self.answer = min(self.answer, max(self.x, self.y) * self.s)
            else:
                self.answer = min(self.answer, (max(self.x, self.y) - 1) * self.s + self.w)

        print(self.answer)


problem = Main()
problem.solve()
