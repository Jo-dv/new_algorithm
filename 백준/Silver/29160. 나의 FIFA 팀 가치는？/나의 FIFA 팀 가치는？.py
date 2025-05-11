import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.players = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        squad = {i: [] for i in range(1, 12)}
        for player in self.players:
            p, w = player
            heapq.heappush(squad[p], -w)

        best = None
        for _ in range(self.k):
            best = [0] * 12
            for i in range(1, 12):
                if squad[i] and squad[i][0] < 0:
                    heapq.heapreplace(squad[i], squad[i][0] + 1)
                    best[i] = -squad[i][0]

        print(sum(best))


problem = Main()
problem.solve()