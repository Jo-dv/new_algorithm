import sys
from bisect import *
input = sys.stdin.readline


class Main:
    def __init__(self):
        self.n, self.s = map(int, input().split())
        self.arts = [tuple(map(int, input().split())) for _ in range(self.n)]

    def solve(self):
        self.arts.sort()
        dp = [0] * (self.n + 1)
        positions = [art[0] for art in self.arts]

        for i in range(self.n):
            h, c = self.arts[i]
            j = bisect_right(positions, h - self.s) - 1  # s 이상 떨어진 가장 가까운 이전 위치 찾기 (이분 탐색)
            dp[i + 1] = max(dp[i], (dp[j + 1] if j >= 0 else 0) + c)  # dp[i+1] = max(현재 예술품 선택한 경우, 이전까지의 최대 값)

        print(dp[self.n])


problem = Main()
problem.solve()
