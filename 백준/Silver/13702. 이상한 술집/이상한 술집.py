import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.containers = [int(input()) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        left = 1
        right = max(self.containers)

        while left <= right:
            mid = (left + right) // 2

            total = sum(container // mid for container in self.containers)
            if total >= self.k:
                self.answer = mid
                left = mid + 1
            else:
                right = mid - 1

        print(self.answer)


problem = Main()
problem.solve()