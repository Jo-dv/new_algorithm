from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.subjects = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.answer = [0] * (self.n + 1)

    def solve(self):
        graph = {i: [] for i in range(1, self.n + 1)}
        in_degree = [0] * (self.n + 1)

        for a, b in self.subjects:
            graph[a].append(b)
            in_degree[b] += 1

        dq = deque()
        for i in range(1, self.n + 1):
            if in_degree[i] == 0:
                dq.append(i)
                self.answer[i] = 1

        while dq:
            node = dq.popleft()
            for nxt in graph[node]:
                in_degree[nxt] -= 1
                self.answer[nxt] = max(self.answer[nxt], self.answer[node] + 1)
                if in_degree[nxt] == 0:
                    dq.append(nxt)

        print(*self.answer[1:])


problem = Main()
problem.solve()
