class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        if self.n > 0:
            self.books = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        if self.n == 0:
            print(0)
            return

        current = 0
        for i in self.books:
            if current + i < self.m:
                current += i
            elif current + i == self.m:
                self.answer += 1
                current = 0
            else:
                self.answer += 1
                current = i

        if current != 0:
            self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()