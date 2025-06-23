class Main:
    def __init__(self):
        self.string = input()
        self.answer = -1

    def solve(self):
        if self.string != self.string[::-1]:
            self.answer = len(self.string)
        elif len(set(self.string)) == 1:
            self.answer = -1
        else:
            self.answer = len(self.string) - 1

        print(self.answer)

problem = Main()
problem.solve()
