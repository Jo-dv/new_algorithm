class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]

    def solve(self):
        dp = [[0] * self.n for _ in range(self.n)]
        dp[0][0] = 1

        for i in range(self.n):
            for j in range(self.n):
                if (i, j) == (self.n - 1, self.n - 1):
                    continue
                nxt_i = self.grid[i][j] + i
                nxt_j = self.grid[i][j] + j
                if nxt_i < self.n:
                    dp[nxt_i][j] += dp[i][j]
                if nxt_j < self.n:
                    dp[i][nxt_j] += dp[i][j]

        print(dp[-1][-1])


problem = Main()
problem.solve()
