import heapq
from collections import defaultdict

class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.info = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.s, self.e = map(int, input().split())

    def solve(self):
        graph = defaultdict(list)

        for a, b, c in self.info:
            graph[a].append((b, c))
            graph[b].append((a, c))

        costs = [0] * (self.n + 1)  # 각 노드까지의 최대 bottleneck 용량 저장
        hq = [(-10**9, self.s)]     # (가능 중량(음수), 현재 노드), 매우 큰 수로 시작

        while hq:
            cur_cap, current = heapq.heappop(hq)
            cur_cap = -cur_cap

            if current == self.e:
                print(cur_cap)
                return

            if costs[current] >= cur_cap:
                continue

            costs[current] = cur_cap

            for nxt, nxt_cap in graph[current]:
                possible_cap = min(cur_cap, nxt_cap)
                if possible_cap > costs[nxt]:
                    heapq.heappush(hq, (-possible_cap, nxt))


problem = Main()
problem.solve()
