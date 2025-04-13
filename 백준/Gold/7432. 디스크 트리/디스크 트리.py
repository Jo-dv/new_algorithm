from collections import defaultdict


class Node:
    def __init__(self):
        self.child = defaultdict(Node)


class Main:
    def __init__(self):
        self.n = int(input())
        self.info = [input().split("\\") for _ in range(self.n)]
        self.root = Node()

    def insert(self, path):
        current = self.root

        for nxt in path:
            current = current.child[nxt]

    def search(self, node=None, depth=0):
        if node is None:
            node = self.root

        for nxt in sorted(node.child.keys()):
            print(" "*depth + nxt)
            self.search(node.child[nxt], depth + 1)

    def solve(self):
        for i in self.info:
            self.insert(i)

        self.search()


problem = Main()
problem.solve()