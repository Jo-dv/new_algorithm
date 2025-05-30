import sys
sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.info = list(map(int, input().split()))
        self.connections = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.graph = {i: [] for i in range(1, self.n + 1)}
        self.answer = [0] * (self.n + 1)

    def dfs(self, current):
        for nxt in self.graph[current]:
            self.answer[nxt] += self.answer[current]  # 부모의 칭찬 전파
            self.dfs(nxt)

    def solve(self):
        for i in range(2, self.n + 1):
            boss = self.info[i - 1]
            self.graph[boss].append(i)

        for i, w in self.connections:
            self.answer[i] += w

        self.dfs(1)
        print(' '.join(map(str, self.answer[1:])))


problem = Main()
problem.solve()
