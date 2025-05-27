import sys
sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t = int(input())
        self.graph = None
        self.parent = None
        self.depth = None

    def dfs(self, node, d):
        self.depth[node] = d
        for child in self.graph[node]:
            if self.depth[child] == -1:
                self.parent[child] = node
                self.dfs(child, d + 1)

    def get_lca(self, a, b):
        # 깊이 같아질 때까지 위로 올리기
        while self.depth[a] > self.depth[b]:
            a = self.parent[a]
        while self.depth[b] > self.depth[a]:
            b = self.parent[b]
        # 같은 노드가 될 때까지 같이 위로 올리기
        while a != b:
            a = self.parent[a]
            b = self.parent[b]
        return a

    def solve(self):
        for _ in range(self.t):
            n = int(input())
            self.graph = {i: [] for i in range(1, n + 1)}
            has_parent = [False] * (n + 1)

            for _ in range(n - 1):
                parent, child = map(int, input().split())
                self.graph[parent].append(child)
                has_parent[child] = True

            root = -1
            for i in range(1, n + 1):
                if not has_parent[i]:
                    root = i
                    break

            self.parent = [0] * (n + 1)
            self.depth = [-1] * (n + 1)
            self.dfs(root, 0)

            a, b = map(int, input().split())
            print(self.get_lca(a, b))


solver = Main()
solver.solve()
