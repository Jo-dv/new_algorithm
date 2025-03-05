class Main:
    def __init__(self):
        self.n = int(input())
        self.answer = 0

    def solve(self):
        low = high = 1
        target = 0
        while high <= self.n + 1:  # 자기 자신 포함
            if target <= self.n:
                target += high
                high += 1
            else:
                target -= low
                low += 1

            if target == self.n:
                self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()