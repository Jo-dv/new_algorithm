import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))
        self.m = int(input())
        self.queries = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.tree = [0] * (self.n * 4)
        self.answer = []

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        self.build(node * 2 + 1, start, mid)
        self.build(node * 2 + 2, mid + 1, end)
        self.tree[node] = min(self.tree[node * 2 + 1], self.tree[node * 2 + 2])

    def update(self, node, start, end, idx, value):
        if idx < start or end < idx:
            return

        if start == end:
            self.tree[node] = value
            return

        mid = (start + end) // 2
        self.update(node * 2 + 1, start, mid, idx, value)
        self.update(node * 2 + 2, mid + 1, end, idx, value)
        self.tree[node] = min(self.tree[node * 2 + 1], self.tree[node * 2 + 2])

    def query(self, node, start, end, query_start, query_end):
        if query_end < start or end < query_start:
            return float("inf")

        if query_start <= start and end <= query_end:
            return self.tree[node]

        mid = (start + end) // 2
        start_min = self.query(node * 2 + 1, start, mid, query_start, query_end)
        end_min = self.query(node * 2 + 2, mid + 1, end, query_start, query_end)
        return min(start_min, end_min)

    def solve(self):
        self.build(0, 0, self.n - 1)

        for query in self.queries:
            if query[0] == 1:
                _, i, v = query
                self.update(0, 0, self.n - 1, i - 1, v)
            else:
                _, i, j = query
                result = self.query(0, 0, self.n - 1, i - 1, j - 1)
                self.answer.append(str(result))

        print("\n".join(self.answer))


problem = Main()
problem.solve()