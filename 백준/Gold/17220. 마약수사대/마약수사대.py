from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.graph = {chr(65 + i): [] for i in range(self.n)}
        self.in_degree = {chr(65 + i): 0 for i in range(self.n)}

        for _ in range(self.m):
            u, v = input().split()
            self.graph[u].append(v)
            self.in_degree[v] += 1

        data = input().split()
        cnt = int(data[0])
        self.arrested = set(data[1:]) if cnt > 0 else set()

    def bfs(self, start):
        q = deque([start])
        visited = {start}
        while q:
            current = q.popleft()
            for nxt in self.graph[current]:
                if nxt not in self.arrested and nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        
        return visited

    def solve(self):
        sources = [node for node in self.graph if self.in_degree[node] == 0 and self.graph[node]]

        total_received = set()  # 약물을 공급 받는 노드들의 집합
        for src in sources:
            if src in self.arrested:
                continue  # 원산지가 검거되면 해당 공급망은 시작할 수 없음
            component = self.bfs(src)
            component.discard(src)  # 원산지는 공급을 받는 대상이 아니므로 제거
            total_received |= component  # 집합의 합집합 계산

        print(len(total_received))


problem = Main()
problem.solve()
