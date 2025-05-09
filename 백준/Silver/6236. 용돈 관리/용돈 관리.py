class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.amounts = [int(input()) for _ in range(self.n)]
        self.answer = 0

    def is_valid(self, k):
        cnt = 1
        current = k

        for amount in self.amounts:
            if current > k:
                return False
            if current < amount:
                cnt += 1
                current = k
            current -= amount

        return cnt <= self.m

    def solve(self):
        low = max(self.amounts)
        high = sum(self.amounts)
        self.answer = high

        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(mid):
                self.answer = mid
                high = mid - 1
            else:
                low = mid + 1

        print(self.answer)


problem = Main()
problem.solve()