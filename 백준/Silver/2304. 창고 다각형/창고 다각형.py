import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.info = [tuple(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        self.info.sort()
        max_height = max(self.info, key=lambda h: h[1])
        max_height_idx = self.info.index(max_height)

        x, y = self.info[0]
        for i in range(1, max_height_idx + 1):
            if y < self.info[i][1]:
                self.answer += ((self.info[i][0] - x) * y)
                x, y = self.info[i]

        self.answer += max_height[1]

        x, y = self.info[-1]
        for i in range(self.n-2, max_height_idx-1, -1):
            if y <= self.info[i][1]:
                self.answer += ((x - self.info[i][0]) * y)
                x, y = self.info[i]

        print(self.answer)


problem = Main()
problem.solve()
