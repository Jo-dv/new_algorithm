import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.weights = [int(input()) for _ in range(self.n)]

    def solve(self):
        answer = 0
        self.weights.sort(reverse=True)

        for i in range(self.n):
            answer = max(answer, (self.weights[i]) * (i + 1))

        print(answer)


problem = Main()
problem.solve()