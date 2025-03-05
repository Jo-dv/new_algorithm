class Main:
    def __init__(self):
        self.n = int(input())
        self.answer = 1

    def solve(self):
        low = high = 1
        target = 1

        while low <= (self.n // 2) + 1:
            if target < self.n:
                high += 1
                target += high
            elif target > self.n:
                target -= low
                low += 1
            else:
                self.answer += 1
                high += 1
                target += high

        print(self.answer if self.n > 2 else 1)


problem = Main()
problem.solve()