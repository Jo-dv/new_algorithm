class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.bottles = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        cage = [0] * (max(self.bottles, key=lambda cord: cord[1])[1] + 1)
        for g, x in self.bottles:
            cage[x] = g

        ice = 0
        low = high = 0
        while high < len(cage):
            if high - low + 1 <= self.k * 2 + 1:
                ice += cage[high]
                high += 1
            else:
                ice -= cage[low]
                low += 1

            self.answer = max(self.answer, ice)

        print(self.answer)


problem = Main()
problem.solve()