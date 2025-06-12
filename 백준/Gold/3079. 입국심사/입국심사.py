class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.times = [int(input()) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        left = 1
        right = max(self.times) * self.m

        while left <= right:
            mid = (left + right) // 2
            total = sum(mid // t for t in self.times)

            if total >= self.m:
                self.answer = mid
                right = mid - 1
            else:
                left = mid + 1

        print(self.answer)


problem = Main()
problem.solve()