import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

class Main:
    def __init__(self):
        self.n, self.m, self.r = map(int, input().split())
        self.info = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.answer = [0] * (self.n + 1)

    def solve(self):
        # 그래프 생성
        graph = {i: [] for i in range(1, self.n + 1)}
        for u, v in self.info:
            graph[u].append(v)
            graph[v].append(u)  # 무방향 그래프니까 반대 방향도 추가

        # 인접 정점 오름차순 정렬
        for adj in graph.values():
            adj.sort()

        visited = [False] * (self.n + 1)
        dq = deque([self.r])
        visited[self.r] = True
        order = 1
        self.answer[self.r] = order

        while dq:
            current = dq.popleft()
            for nxt in graph[current]:
                if not visited[nxt]:
                    order += 1
                    visited[nxt] = True
                    self.answer[nxt] = order
                    dq.append(nxt)

        # 결과 출력
        for i in range(1, self.n + 1):
            print(self.answer[i])

problem = Main()
problem.solve()
