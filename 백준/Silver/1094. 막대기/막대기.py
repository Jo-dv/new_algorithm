class Main:
    def __init__(self):
        self.x = int(input())

    def solve(self):
        print(bin(self.x).count('1'))


problem = Main()
problem.solve()