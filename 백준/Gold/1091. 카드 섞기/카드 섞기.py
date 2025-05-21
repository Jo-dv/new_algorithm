class Main:
    def __init__(self):
        self.n = int(input())
        self.p = list(map(int, input().split()))
        self.s = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        cards = list(range(self.n))
        original = cards[:]

        while True:
            if all(self.p[cards[i]] == i % 3 for i in range(self.n)):
                print(self.answer)
                return

            new_cards = [0] * self.n
            for i in range(self.n):
                new_cards[self.s[i]] = cards[i]

            cards = new_cards
            self.answer += 1

            if cards == original:
                print(-1)
                return


problem = Main()
problem.solve()