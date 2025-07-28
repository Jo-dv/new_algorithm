class Main:
    def __init__(self):
        self.n = int(input())
        self.guitars = [input() for _ in range(self.n)]

    def solve(self):
        result = []
        for guitar in self.guitars:
            total = 0
            for i in guitar:
                if i.isdigit():
                    total += int(i)
            result.append((len(guitar), total, guitar))

        result.sort(key=lambda x: (x[0], x[1], x[2]))
        for i in result:
            print(i[-1])


problem = Main()
problem.solve()
