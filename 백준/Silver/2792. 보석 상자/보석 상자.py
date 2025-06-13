import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.jewels = [int(input()) for _ in range(self.m)]
        self.answer = 0

    def solve(self):
        left = 1
        right = max(self.jewels)

        while left <= right:
            mid = (left + right) // 2
            total = sum((jewel + mid - 1) // mid for jewel in self.jewels)

            if total <= self.n:
                self.answer = mid
                right = mid - 1
            else:
                left = mid + 1

        print(self.answer)


problem = Main()
problem.solve()