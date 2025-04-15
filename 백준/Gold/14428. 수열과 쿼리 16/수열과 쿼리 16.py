import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))
        self.m = int(input())
        self.queries = list(tuple(map(int, input().split())) for _ in range(self.m))
        self.tree = [0] * (self.n * 4)
        self.answer = []

    def build(self, node, left, right):
        if left == right:
            self.tree[node] = self.arr[left]
            return

        mid = (left + right) // 2
        self.build(node * 2 + 1, left, mid)
        self.build(node * 2 + 2, mid + 1, right)
        self.tree[node] = min(self.tree[node * 2 + 1], self.tree[node * 2 + 2], key=lambda x: (x[1], x[0]))

    def update(self, node, left, right, query_idx, val):
        if query_idx < left or right < query_idx:
            return

        if left == right:
            self.tree[node] = [query_idx + 1, val]
            return

        mid = (left + right) // 2
        self.update(node*2+1, left, mid, query_idx, val)
        self.update(node*2+2, mid+1, right, query_idx, val)
        self.tree[node] = min(self.tree[node * 2 + 1], self.tree[node * 2 + 2], key=lambda x: (x[1], x[0]))

    def query(self, node, node_left, node_right, query_left, query_right):
        if query_right < node_left or node_right < query_left:
            return [float("inf"), 10**9+1]

        if query_left <= node_left and node_right <= query_right:
            return self.tree[node]

        mid = (node_left + node_right) // 2
        left = self.query(node * 2 + 1, node_left, mid, query_left, query_right)
        right = self.query(node * 2 + 2, mid + 1, node_right, query_left, query_right)
        return min(left, right, key=lambda x: (x[1], x[0]))

    def solve(self):
        self.arr = [[i, num] for i, num in enumerate(self.arr, 1)]
        self.build(0, 0, self.n-1)

        for a, b, c in self.queries:
            if a == 2:
                val = self.query(0, 0, self.n-1, b-1, c-1)[0]
                self.answer.append(str(val))
            else:
                self.update(0, 0, self.n-1, b-1, c)

        print("\n".join(self.answer))


problem = Main()
problem.solve()
