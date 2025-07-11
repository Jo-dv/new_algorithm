from collections import defaultdict


class Main:
    def __init__(self):
        self.n = int(input())
        self.nodes = [tuple(map(int, input().split())) for _ in range(self.n - 1)]
        self.answer = list(map(int, input().split()))
        self.visited = [False] * (self.n + 1)
        self.result = []

    def search(self, current, graph):
        self.visited[current] = True
        self.result.append(current)

        for nxt in graph[current]:
            if not self.visited[nxt]:
                self.search(nxt, graph)

    def solve(self):
        graph = defaultdict(list)
        for a, b in self.nodes:
            graph[a].append(b)
            graph[b].append(a)

        # 방문 순서 기반으로 인접 리스트 정렬
        order = [0] * (self.n + 1)
        for idx, num in enumerate(self.answer):
            order[num] = idx

        for key in graph.keys():
            graph[key].sort(key=lambda x: order[x])

        self.search(1, graph)

        if self.result == self.answer:
            print(1)
        else:
            print(0)


problem = Main()
problem.solve()
