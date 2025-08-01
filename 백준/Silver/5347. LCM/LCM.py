import math


class Main:
    def __init__(self):
        self.t = int(input())
        self.answer = []

    def solve(self):
        for _ in range(self.t):
            a, b = map(int, input().split())
            self.answer.append(math.lcm(a, b))

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()