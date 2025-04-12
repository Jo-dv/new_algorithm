import sys
input = lambda: sys.stdin.readline().rstrip()


class SegmentNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.left_child = None
        self.right_child = None
        self.min_val = float('inf')
        self.max_val = float('-inf')


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = [int(input()) for _ in range(self.n)]
        self.pair = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(self.m)]
        self.root = self.build(0, self.n - 1)
        self.answer = []

    def build(self, left, right):
        node = SegmentNode(left, right)
        if left == right:
            val = self.arr[left]
            node.min_val = val
            node.max_val = val
            return node

        mid = (left + right) // 2
        node.left_child = self.build(left, mid)
        node.right_child = self.build(mid + 1, right)

        node.min_val = min(node.left_child.min_val, node.right_child.min_val)
        node.max_val = max(node.left_child.max_val, node.right_child.max_val)

        return node

    def query(self, node, ql, qr):
        if node.right < ql or node.left > qr:
            return float('inf'), float('-inf')

        if ql <= node.left and node.right <= qr:
            return node.min_val, node.max_val

        left_min, left_max = self.query(node.left_child, ql, qr)
        right_min, right_max = self.query(node.right_child, ql, qr)

        return min(left_min, right_min), max(left_max, right_max)

    def solve(self):
        for a, b in self.pair:
            min_val, max_val = self.query(self.root, a, b)
            self.answer.append(f"{min_val} {max_val}")

        print("\n".join(self.answer))


problem = Main()
problem.solve()
