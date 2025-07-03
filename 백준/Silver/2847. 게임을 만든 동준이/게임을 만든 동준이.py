class Main:
    def __init__(self):
        self.n = int(input())
        self.scores = [int(input()) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        for i in range(self.n-2, -1, -1):
            diff = self.scores[i+1] - self.scores[i]
            if diff <= 0:
                diff -= 1
                self.scores[i] += diff
                self.answer += (-1 * diff)

        print(self.answer)


problem = Main()
problem.solve()