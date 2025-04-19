from collections import defaultdict


class Node:
    def __init__(self):
        self.child = defaultdict(Node)


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.standards = [input() for _ in range(self.n)]
        self.checks = [input() for _ in range(self.m)]
        self.root = Node()
        self.answer = 0

    def build(self):
        for standard in self.standards:
            current = self.root
            for ch in standard:
                current = current.child[ch]

    def search(self, prefix):
        current = self.root

        for ch in prefix:
            if ch not in current.child:
                return False
            current = current.child[ch]

        return True

    def solve(self):
        self.build()
        for check in self.checks:
            if self.search(check):
                self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()