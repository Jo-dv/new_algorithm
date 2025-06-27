class Main:
    def __init__(self):
        self.n = int(input())
        self.line = [input() for _ in range(self.n)]

    def solve(self):
        if self.line == sorted(self.line):
            print("INCREASING")
        elif self.line == sorted(self.line, reverse=True):
            print("DECREASING")
        else:
            print("NEITHER")


problem = Main()
problem.solve()