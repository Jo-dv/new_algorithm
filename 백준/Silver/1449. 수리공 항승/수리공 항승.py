class Main:
    def __init__(self):
        self.n, self.l = map(int, input().split())
        self.positions = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        self.positions.sort()
        end = 0.0

        for pos in self.positions:
            if pos > end:
                self.answer += 1
                end = pos + self.l - 0.5

        print(self.answer)


problem = Main()
problem.solve()
