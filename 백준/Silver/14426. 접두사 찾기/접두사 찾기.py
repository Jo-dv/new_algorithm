from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()


class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.end = False


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

            current.end = True

    def search(self, prefix):
        current = self.root

        for ch in prefix:
            if ch not in current.child:
                return False
            current = current.child[ch]
            if current.end:
                return True

        return True

    def solve(self):
        self.build()
        for check in self.checks:
            if self.search(check):
                self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()