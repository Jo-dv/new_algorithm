import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t, self.x, self.m = map(int, input().split())
        self.monsters = [list(map(int, input().split())) for _ in range(self.m)]
        self.answer = 0

    def solve(self):
        if self.m > 0:
            hq = []
            for monster in self.monsters:
                d, s = monster
                heapq.heappush(hq, [d - s, d, s])  # 거리가 가깝고 보폭이 큰 순서

            for _ in range(self.t):
                i, d, s = heapq.heappop(hq)

                if i > 0:
                    self.answer += self.x
                    heapq.heappush(hq, [i - s, d, s])
                else:
                    heapq.heappush(hq, [min(i + s, d - s), d, s])

            print(self.answer)
        else:
            print(self.t * self.x)


problem = Main()
problem.solve()