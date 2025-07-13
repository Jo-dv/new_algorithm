import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.badges = [input().split() for _ in range(self.n)]
        self.players = [int(input()) for _ in range(self.m)]
        self.answer = []

    def solve(self):
        titles = []
        powers = []

        for i in range(self.n):
            badge, power = self.badges[i]
            titles.append(badge)
            powers.append(int(power))

        for i in range(self.m):
            idx = bisect_left(powers, self.players[i])
            self.answer.append(titles[idx])

        print("\n".join(self.answer))


problem = Main()
problem.solve()