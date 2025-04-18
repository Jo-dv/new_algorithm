from collections import defaultdict, deque


class Node:
    def __init__(self):
        self.child = defaultdict(Node)


class Main:
    def __init__(self):
        self.s = input()
        self.root = Node()

    def insert(self):
        n = len(self.s)
        for i in range(n):
            current = self.root
            for j in range(i, min(n, i + 5)):  # 4^6 > 2000
                nxt = self.s[j]
                current = current.child[nxt]

    def search(self):
        dna = ['A', 'C', 'G', 'T']
        queue = deque([("", self.root)])

        while queue:
            prefix, current = queue.popleft()
            for c in dna:
                if c not in current.child:
                    return prefix + c
                queue.append((prefix + c, current.child[c]))

    def solve(self):
        self.insert()
        print(self.search())


problem = Main()
problem.solve()