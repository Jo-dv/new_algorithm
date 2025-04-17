import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m, self.k = map(int, input().split())
        self.arr = [int(input()) for _ in range(self.n)]
        self.tree = [0] * (self.n * 4)
        self.lazy = [0] * (self.n * 4)
        self.queries = [list(map(int, input().split())) for _ in range(self.m + self.k)]
        self.answer = []

    def build(self, node, left, right):
        if left == right:
            self.tree[node] = self.arr[left]
            return

        mid = (left + right) // 2
        self.build(node * 2, left, mid)
        self.build(node * 2 + 1, mid + 1, right)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def propagate(self, node, left, right):
        if self.lazy[node] != 0:
            self.tree[node] += (right - left + 1) * self.lazy[node]
            if left != right:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, node, left, right, query_left, query_right, val):
        self.propagate(node, left, right)

        if query_right < left or right < query_left:
            return

        if query_left <= left and right <= query_right:
            self.lazy[node] += val
            self.propagate(node, left, right)
            return

        mid = (left + right) // 2
        self.update(node * 2, left, mid, query_left, query_right, val)
        self.update(node * 2 + 1, mid + 1, right, query_left, query_right, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, left, right, query_left, query_right):
        self.propagate(node, left, right)

        if query_right < left or right < query_left:
            return 0

        if query_left <= left and right <= query_right:
            return self.tree[node]

        mid = (left + right) // 2
        left_sum = self.query(node * 2, left, mid, query_left, query_right)
        right_sum = self.query(node * 2 + 1, mid + 1, right, query_left, query_right)
        return left_sum + right_sum

    def solve(self):
        self.build(1, 0, self.n - 1)

        for q in self.queries:
            if q[0] == 1:
                _, b, c, d = q
                self.update(1, 0, self.n - 1, b - 1, c - 1, d)
            else:
                _, b, c = q
                res = self.query(1, 0, self.n - 1, b - 1, c - 1)
                self.answer.append(str(res))

        print("\n".join(self.answer))


problem = Main()
problem.solve()
