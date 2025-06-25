class Main:
    def __init__(self):
        self.n = int(input())
        self.numbers = [input() for _ in range(self.n)]

    def solve(self):
        length = len(self.numbers[0])

        for i in range(1, length+1):
            check = set()
            for number in self.numbers:
                check.add(number[-i:])
                if len(check) == self.n:
                    print(i)
                    return

        print(0)


problem = Main()
problem.solve()