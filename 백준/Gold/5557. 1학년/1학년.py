class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = list(map(int, input().split()))
        self.dp = [[0] * 21 for _ in range(self.n - 1)]

    def solve(self):
        self.dp[0][self.nums[0]] = 1  # 첫 번째 숫자로 시작

        for i in range(1, self.n - 1):  # 마지막 숫자는 목표값이므로 제외
            for total in range(21):
                if self.dp[i - 1][total] > 0:  # 이전 단계에서 가능한 값만 진행
                    if total + self.nums[i] <= 20:
                        self.dp[i][total + self.nums[i]] += self.dp[i - 1][total]
                    if total - self.nums[i] >= 0:
                        self.dp[i][total - self.nums[i]] += self.dp[i - 1][total]
        
        print(self.dp[self.n - 2][self.nums[-1]])  # 목표값에 도달하는 경우의 수 출력

problem = Main()
problem.solve()
