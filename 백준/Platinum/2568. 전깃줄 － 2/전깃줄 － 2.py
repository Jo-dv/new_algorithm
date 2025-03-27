import bisect
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.lines = [tuple(map(int, input().split())) for _ in range(self.n)]

    def search(self):
        self.lines.sort()
        dp = []
        tracking = []

        for i in range(self.n):
            value = self.lines[i][1]
            if not dp or dp[-1] < value:
                dp.append(value)
                tracking.append(len(dp) - 1)
            else:
                idx = bisect.bisect_left(dp, value)
                dp[idx] = value
                tracking.append(idx)

        return dp, tracking

    def trace(self, dp, tracking):
        candidates = set()
        current_len = len(dp) - 1
        for i in range(len(tracking) - 1, -1, -1):
            if tracking[i] == current_len:
                candidates.add(self.lines[i])
                current_len -= 1

        return candidates

    def solve(self):
        dp, tracking = self.search()
        candidates = self.trace(dp, tracking)

        print(self.n - len(candidates))
        for line in self.lines:
            if line not in candidates:
                print(line[0])


problem = Main()
problem.solve()
