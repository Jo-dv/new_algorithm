class Main:
    def __init__(self):
        self.s = input()
        self.answer = self.s[0]

    def solve(self):
        n = len(self.s)

        for i in range(1, n):
            if self.answer[i - 1] < self.s[i]:
                self.answer = self.s[i] + self.answer
            else:
                self.answer += self.s[i]

        print(self.answer[::-1])


problem = Main()
problem.solve()
