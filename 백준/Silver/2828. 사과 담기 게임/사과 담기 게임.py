class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.j = int(input())
        self.apples = [int(input()) for _ in range(self.j)]
        self.answer = 0

    def solve(self):
        start = 1
        end = self.m

        for apple in self.apples:
            if end < apple:
                distance = apple - end
                self.answer += distance
                start += distance
                end += distance
            elif apple < start:
                distance = start - apple
                self.answer += distance
                start -= distance
                end -= distance

        print(self.answer)


problem = Main()
problem.solve()