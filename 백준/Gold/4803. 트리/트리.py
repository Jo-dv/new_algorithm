import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.graph = None
        self.answer = []

    def search(self, node, visited, parent):
        visited[node] = True

        for nxt in self.graph[node]:
            if not visited[nxt]:
                if not self.search(nxt, visited, node):
                    return False
            elif nxt != parent:
                return False

        return True

    def solve(self):
        while True:
            n, m = map(int, input().split())
            if n == m == 0:
                break
            self.graph = {i: [] for i in range(1, n + 1)}
            for _ in range(m):
                u, v = map(int, input().split())
                self.graph[u].append(v)
                self.graph[v].append(u)

            visited = [False] * (n + 1)
            cnt = 0
            for i in range(1, n + 1):
                if not visited[i]:
                    if self.search(i, visited, -1):
                        cnt += 1

            self.answer.append("No trees." if cnt == 0 else "There is one tree." if cnt == 1 else f"A forest of {cnt} trees.")

        for i, data in enumerate(self.answer, 1):
            print(f"Case {i}: {data}")


problem = Main()
problem.solve()
