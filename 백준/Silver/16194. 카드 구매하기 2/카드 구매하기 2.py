class Main:
    def __init__(self):
        self.n = int(input())
        self.cards = [0] + list(map(int, input().split()))  # 1-based index로 편리하게 처리

    def solve(self):
        dp = [float('inf')] * (self.n + 1)
        dp[0] = 0  # 0개의 카드를 사는 데 필요한 비용은 0원

        for i in range(1, self.n + 1):
            for j in range(1, i + 1):
                dp[i] = min(dp[i], dp[i - j] + self.cards[j])

        print(dp[self.n])


problem = Main()
problem.solve()