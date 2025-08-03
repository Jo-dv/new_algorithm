class Main:
    def __init__(self):
        self.n = int(input())
        self.info = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        self.info.sort()

        for arrive, waiting in self.info:
            self.answer = max(self.answer, arrive)
            self.answer += waiting

        print(self.answer)


problem = Main()
problem.solve()