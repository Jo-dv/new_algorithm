class Main:
    def __init__(self):
        self.n = int(input())
        self.energy = [tuple(map(int, input().split())) for _ in range(self.n - 1)]
        self.k = int(input())

    def solve(self):
        dp = [[float('inf')] * self.n for _ in range(2)]
        dp[1][0] = 0

        for i in range(self.n - 1):
            if i + 1 < self.n:
                dp[1][i + 1] = min(dp[1][i + 1], dp[1][i] + self.energy[i][0])
                dp[0][i + 1] = min(dp[0][i + 1], dp[0][i] + self.energy[i][0])
            if i + 2 < self.n:
                dp[1][i + 2] = min(dp[1][i + 2], dp[1][i] + self.energy[i][1])
                dp[0][i + 2] = min(dp[0][i + 2], dp[0][i] + self.energy[i][1])
            if i + 3 < self.n:
                dp[0][i + 3] = min(dp[0][i + 3], dp[1][i] + self.k)

        print(min(dp[0][self.n - 1], dp[1][self.n - 1]))


problem = Main()
problem.solve()
