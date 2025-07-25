import sys
import math
input = sys.stdin.readline


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.info = [list(map(int, input().split())) for _ in range(self.m)]
        self.k = int(math.sqrt(self.n))
        self.box = [0] * self.n
        self.cup = [0] * (self.n // self.k + 1)

    def process_day(self, berry, start_raw):
        start = start_raw - 1
        end = start + berry
        ans = 0

        # 시작 부분: 블록 경계 전까지 matchbox 처리
        while start < end and start % self.k != 0:
            self.box[start] += 1
            ans += self.box[start]
            start += 1

        # 끝 부분: 블록 경계 이전까지 matchbox 처리
        if end != self.n:
            while start < end and end % self.k != 0:
                end -= 1
                self.box[end] += 1
                ans += self.box[end]

        # 중간 부분: 블록 단위로 컵 처리
        while start < end:
            blk_idx = start // self.k
            self.cup[blk_idx] += 1
            ans += self.cup[blk_idx]
            start += self.k

        print(ans)

    def solve(self):
        for i in range(self.m):
            berry, start = self.info[i]
            self.process_day(berry, start)


problem = Main()
problem.solve()
