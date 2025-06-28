from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.statuses = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = []

    def solve(self):
        for i in range(self.n):
            num, soldiers = self.statuses[i][0], self.statuses[i][1:]
            cnt = sorted(Counter(soldiers).items(), key=lambda x: x[1])
            max_cnt = cnt[-1]

            if max_cnt[1] > num // 2:
                self.answer.append(str(max_cnt[0]))
            else:
                self.answer.append("SYJKGW")

        print("\n".join(self.answer))


problem = Main()
problem.solve()