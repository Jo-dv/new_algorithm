class Main:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        dp = [0] * 31
        dp[2] = 3

        for i in range(4, 31, 2):
            dp[i] = dp[i - 2] * dp[2]
            for j in range(i - 4, 1, -2):
                dp[i] += dp[j] * 2
            dp[i] += 2

        print(dp[self.n])


problem = Main()
problem.solve()