class Main:
    def __init__(self):
        self.n = 251

    def solve(self):
        dp = [0] * self.n
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        for i in range(3, self.n):
            dp[i] += (dp[i - 1] + 2 * dp[i - 2])

        while True:
            try:
                test_cast = int(input())
                print(dp[int(test_cast)])
            except:
                return


problem = Main()
problem.solve()
