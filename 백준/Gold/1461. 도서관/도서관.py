class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.pos = list(map(int, input().split()))

    def solve(self):
        neg = sorted([abs(x) for x in self.pos if x < 0], reverse=True)
        pos = sorted([x for x in self.pos if x > 0], reverse=True)

        max_distance = 0
        if neg and pos:
            max_distance = max(neg[0], pos[0])
        elif neg:
            max_distance = neg[0]
        elif pos:
            max_distance = pos[0]

        total = 0

        for i in range(0, len(neg), self.m):
            total += neg[i] * 2

        for i in range(0, len(pos), self.m):
            total += pos[i] * 2

        total -= max_distance

        print(total)

problem = Main()
problem.solve()
