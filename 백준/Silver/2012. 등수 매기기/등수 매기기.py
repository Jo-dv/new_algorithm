import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.rank = [int(input()) for _ in range(self.n)]

    def solve(self):
        answer = 0
        self.rank.sort()

        for num, i in enumerate(self.rank, 1):
            answer += abs(i - num)

        print(answer)


problem = Main()
problem.solve()