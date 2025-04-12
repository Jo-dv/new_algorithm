import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = [int(input()) for _ in range(self.n)]
        self.pair = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(self.m)]
        self.min_tree = [0] * (4 * self.n)
        self.max_tree = [0] * (4 * self.n)
        self.answer = []

    def min_build(self, node, left, right):
        if left == right:
            self.min_tree[node] = self.arr[left]
            return

        mid = (left + right) // 2
        self.min_build(node * 2 + 1, left, mid)
        self.min_build(node * 2 + 2, mid + 1, right)

        self.min_tree[node] = min(self.min_tree[node * 2 + 1], self.min_tree[node * 2 + 2])

    def max_build(self, node, left, right):
        if left == right:
            self.max_tree[node] = self.arr[left]
            return

        mid = (left + right) // 2
        self.max_build(node * 2 + 1, left, mid)
        self.max_build(node * 2 + 2, mid + 1, right)

        self.max_tree[node] = max(self.max_tree[node * 2 + 1], self.max_tree[node * 2 + 2])

    def min_query(self, node, node_left, node_right, query_left, query_right):
        if query_right < node_left or node_right < query_left:
            return float('inf')

        if query_left <= node_left and node_right <= query_right:
            return self.min_tree[node]

        mid = (node_left + node_right) // 2
        left_min = self.min_query(node * 2 + 1, node_left, mid, query_left, query_right)
        right_min = self.min_query(node * 2 + 2, mid + 1, node_right, query_left, query_right)
        return min(left_min, right_min)

    def max_query(self, node, node_left, node_right, query_left, query_right):
        if query_right < node_left or node_right < query_left:
            return float('-inf')

        if query_left <= node_left and node_right <= query_right:
            return self.max_tree[node]

        mid = (node_left + node_right) // 2
        left_max = self.max_query(node * 2 + 1, node_left, mid, query_left, query_right)
        right_max = self.max_query(node * 2 + 2, mid + 1, node_right, query_left, query_right)
        return max(left_max, right_max)

    def solve(self):
        self.min_build(0, 0, self.n-1)
        self.max_build(0, 0, self.n-1)

        for a, b in self.pair:
            min_val = self.min_query(0, 0, self.n-1, a, b)
            max_val = self.max_query(0, 0, self.n-1, a, b)
            self.answer.append(f"{min_val} {max_val}")

        print("\n".join(self.answer))


problem = Main()
problem.solve()
