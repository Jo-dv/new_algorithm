class Main:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        print("SK" if self.n % 2 == 0 else "CY")


problem = Main()
problem.solve()