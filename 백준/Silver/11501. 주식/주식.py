class Main:
    def __init__(self):
        self.t = int(input())
        self.n = None
        self.prices = None
        self.answer = []

    def solve(self):
        for _ in range(self.t):
            self.n = int(input())
            self.prices = list(map(int, input().split()))
            max_profit = 0
            max_price = 0
            for current_price in self.prices[::-1]:
                if current_price > max_price:
                    max_price = current_price
                else:
                    max_profit += (max_price - current_price)

            self.answer.append(max_profit)

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()