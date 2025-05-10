class Main:
    def __init__(self):
        self.n = int(input())
        self.k = int(input())

    def is_valid(self, x):
        cnt = 0

        for i in range(1, self.n + 1):
            cnt += min(x // i, self.n)

        return cnt

    def solve(self):
        low = 1
        high = self.n*self.n
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(mid) >= self.k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        print(answer)


problem = Main()
problem.solve()